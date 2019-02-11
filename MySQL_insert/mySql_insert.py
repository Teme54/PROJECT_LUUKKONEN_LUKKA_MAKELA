import requests

def insertdata(QR_code):
    #QR_code = "Teemu_Luukkonen"
    mylist = QR_code.split("_")
    vastaanottaja = mylist[0]
    lahettaja = mylist[1]
    url = "http://172.20.248.131/codeigniter/index.php/main/insertdatatomodel"
    #url = "http://localhost/ci/index.php/main/insertdatatomodel"
    payload  = {'vastaanottaja': vastaanottaja, 'lahettaja': lahettaja, 'QR_koodi': QR_code}
    r = requests.post(url, data = payload)

#insertdata()
