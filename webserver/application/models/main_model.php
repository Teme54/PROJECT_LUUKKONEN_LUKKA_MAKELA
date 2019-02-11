 <?php  
 class Main_model extends CI_Model  
 {  
      function can_login($username, $password)  
      {  
           $this->db->where('username', $username);  
           $this->db->SELECT('hashed_password');  
           $query = $this->db->get('users');  //tekee seuraavanlaisen kyselyn 
           //SELECT hashed_password * FROM users WHERE username = '$username'  
           if($query->num_rows() > 0)  
           {  

              $row = $query->row();
              if(password_verify($password, $row->hashed_password)){
                return true;  
              }
              else
              {
                return false;
              }
           } 
           else  
           {  
                return false;       
           }  
      }


      function insertdata($vastaanottaja, $lahettaja, $QR_koodi)
      {
        $data = array(
          'Havaintoaika' => date('Y-m-d H:i:s'),
          'Vastaanottaja' => $this->input->post('vastaanottaja'),
          'Lähettäjä' => $this->input->post('lahettaja'),
          'QRkoodi' => $this->input->post('QR_koodi')
        );

        $this->db->insert('havainnot', $data);
      }


      function havainnot()
      {
        $query = $this->db->query('SELECT Havaintoaika, Vastaanottaja, Lähettäjä, QRkoodi from havainnot order by id DESC');
        if($query->num_rows() > 0)  
        {
          return $query->result();
        }
        else
        {
          return  $query->result();
        }
      }  
 }  
 