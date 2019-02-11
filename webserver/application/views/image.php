<!DOCTYPE html> 
<html lang = "en">
 
   <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!--skaalaa näyttöä -->
      <meta charset = "utf-8"> 
      <title>CodeIgniter View Example</title> 
      <link rel = "stylesheet" type = "text/css" href = "<?php echo base_url(); ?>css/tyyli.css">
   </head>
<body>
<!-- Kuvamodaali -->
<div id="myModal" class="modal">
  <span class="close">&times;</span>
  <img class="modal-content" id="img01">
  <div id="caption"></div>
</div>



<div class="limiter">
<table id="havainnot">
  <tr>
    <th>Havaintoaika</th>
    <th>Vastaanottaja</th> 
    <th>Lähettäjä</th>
    <th>QR-koodi</th>
    </tr>
      <?php foreach ($havainnot as $row) { ?>
         <td><?php echo $row->Havaintoaika; ?></td>
         <td><?php echo $row->Vastaanottaja; ?></td>
         <td><?php echo $row->Lähettäjä; ?></td>
         <td id="myImg" href="javascript:" onclick="showimage('<?php echo $row->QRkoodi ?>')"> <?php echo $row->QRkoodi; ?> </td>
      </tr>
   <?php } ?>
</table>
</div>











<script type="text/javascript">
	// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
//var img = document.getElementById('myImg');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
function showimage(image){
	var imageholder = image;
    modal.style.display = "block";
    modalImg.src = "https://chart.googleapis.com/chart?cht=qr&chs=500x500&chl="+imageholder+"&choe=utf-8";
    captionText.innerHTML = imageholder;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
</script>
</body>
</html>