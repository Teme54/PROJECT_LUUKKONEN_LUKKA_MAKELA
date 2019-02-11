import urllib.request
import tweepy

def dl_image(qrKoodi):
        QR_koodi = qrKoodi
        #QR_koodi = "luikka"
        url = "https://chart.googleapis.com/chart?cht=qr&chs=450x450&chl="+QR_koodi+"&choe=utf-8"
        urllib.request.urlretrieve(url, "Images/testia.jpg")
        twiittaus(QR_koodi)

	
def twiittaus(tweet):

	#kirjautumistietoja
	access_token = "3411995465-o82AMN7CnaKqpg4vV3OankKKcOyswpSP47rLG0I"
	access_token_secret = "XRXtmob3zeRmumcgSwuPl30wyr7G2a0PNANLZWK9v2Ntl"
	consumer_key = "OdUX2xAE7BxwRBSPkl5jDJkiB"
	consumer_secret = "Hb294VT37O1SpqtEmj6SB8vX9yIwbFfMNfncIF0ulvoYNsx7Lr"
   
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
	auth.set_access_token(access_token, access_token_secret) 
	api = tweepy.API(auth) 
	#tweet ="Testailua" 
	image_path ="Images/testia.jpg" 
  
	# mediafilen uppaus 
	status = api.update_with_media(image_path, tweet)  
	#api.update_status(status = tweet)  
	#api.update_status(status ="Asd !")

