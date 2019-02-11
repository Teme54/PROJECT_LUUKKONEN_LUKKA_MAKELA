<!DOCTYPE html> 
<html lang = "en">
 
   <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!--skaalaa näyttöä -->
      <meta charset = "utf-8"> 
      <title>CodeIgniter View Example</title> 
      <link rel = "stylesheet" type = "text/css" 
         href = "<?php echo base_url(); ?>css/tyyli.css"> 
      <script type = 'text/javascript' src = "<?php echo base_url(); 
         ?>js/sample.js"></script> 
   </head>
   <body>

   <div class ="header">
      <h1 style="display:inline">QR-Hunter</h1>
      <div class="dropdown">
      <button class="dropbtn"><?php echo $_SESSION['username']?></button>
      <div class="dropdown-content">
      <a href="http://localhost/ci/index.php/main/logout">Logout</a>
   </div>
   </div>
   </div>

<div class ="row">
   <div class = "col-3 menu">
      <ul>
      <li> Jotain dataa! </li>
      <li> Jotain dataaa myös.. </li>
      </ul>
   </div>

   <div class ="col-9">
      <h1>ASADSDSASAD</h1>
   </div>
</body>
</html>
