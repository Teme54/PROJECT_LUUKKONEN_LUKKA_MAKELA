<?php  
 defined('BASEPATH') OR exit('No direct script access allowed');  
 class Main extends CI_Controller { 


     
      //functions  
      function login()  
      {             
           $this->load->view("login");  
      }  
      function login_validation()  
      {           
        //$this->load->helper('form');
        //$this->load->helper('url');
           $this->load->library('form_validation');
           $this->form_validation->set_rules('username', 'Username', 'required');  //Katsoo onko käyttäjä/salasana asetettu
           $this->form_validation->set_rules('password', 'Password', 'required');  
           if($this->form_validation->run())  
           {  
                //jos on niin siirtyy tänne
                $username = $this->input->post('username');  //hakee käyttäjän ja salasanan login-funktiosta
                $password = $this->input->post('password');  //ja tallettaa ne muuttujiin
                //$hashed_password = password_hash($password, PASSWORD_DEFAULT);
                  
                $this->load->model('main_model');  
                if($this->main_model->can_login($username, $password))  //siirtyy main_modeliin can_login funktioon
                {  
                     $session_data = array(  
                          'username'     =>     $username  //jos mainmodel palauttaa truen tallettaa käyttäjän sessiondataan nimellä username
                     );  
                     $this->session->set_userdata($session_data);  
                     redirect(base_url() . 'index.php/main/taulukko');  //ohjaa pääsivulle
                }  
                else  
                {  
                     $this->session->set_flashdata('error', 'Invalid Username and Password');  //jos mainmodel palauttaa falsen ohjaa se takaisin loginiin error viestin kera
                     redirect(base_url() . 'index.php/main/login');  
                }  
           }  
           else  
           {  
                //jos käyttäjää ja salasanaa ei ollu asetettu palauttaa takas login funktioon
                $this->login();  
           }  
      }  
  
      function logout()  
      {  
           $this->session->unset_userdata('username');  // tuhoaa userdatan ja ohjaa takas login
           redirect(base_url() . 'index.php/main/login');  
      }  

      function taulukko() 
      {  
        if($this->session->userdata('username') != '')  //tarkastaa onko käyttäjä asetettu jos ei ohjaa login
        {
        $this->load->model('main_model');
        $data['havainnot'] = $this->main_model->havainnot();
        $this->load->view('taulukkotesti', $data);
        }
        else
        {
        redirect(base_url() . 'index.php/main/login');
        } 
        }

        function imagetest()
        {
          $this->load->model('main_model');
          $data['havainnot'] = $this->main_model->havainnot();
          $this->load->view('image', $data);
        }

        function insertdata()
        {
          $this->load->view('insert');
        }

        function insertdatatomodel()
        {
          $lahettaja = $this->input->post('lahettaja'); 
          $vastaanottaja = $this->input->post('vastaanottaja');
          $QR_koodi = $this->input->post('QR_koodi');
          $this->load->model('main_model');
          $this->main_model->insertdata($lahettaja, $vastaanottaja, $QR_koodi);

        }
} 