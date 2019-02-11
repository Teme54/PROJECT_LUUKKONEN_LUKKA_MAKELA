<!DOCTYPE html> 
<html lang = "en">

<head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!--skaalaa näyttöä -->
      <meta charset = "utf-8"> 
      <title>CodeIgniter View Example</title> 
      <link rel = "stylesheet" type = "text/css" 
         href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
      <link rel = "stylesheet" type = "text/css" href="<?php echo base_url(); ?>css/style.css">
</head>
<body>  
      <div class="wrapper">
        <div class="form-signin">
           <br /><br /><br />  
           <form method="post" action="login_validation">  
                <div class="form-group">
                     <label>Enter Username</label>  
                     <input type="text" name="username" class="form-control" />  
                     <span class="text-danger"><?php echo form_error('username'); ?></span>
                    
                     <!--Tulostaa form validationista erroria jos käyttäjää ei ole asetettu-->                 
                </div>  
                <div class="form-group">  
                     <label>Enter Password</label>  
                     <input type="password" name="password" class="form-control" />  
                     <span class="text-danger"><?php echo form_error('password'); ?></span> 
                     <!--Tulostaa form validationista erroria jos salasanaa ei ole asetettu-->
                </div>  
                <div class="form-group">  
                <input type="submit" name="insert" value="Login" class="button" />
                     <?php  echo '<label class="text-danger">'.$this->session->flashdata("error").'</label>'; 
                     ?> 
                </div>  
           </form>
      </div> 
      </div>  
 </body>  
 </html>  