import requests
from bs4 import BeautifulSoup #pour utiliser BeautifulSoup j'ai besoin de bs4
import logging 
import unidecode 
import smtplib, ssl
from email.mime.text import MIMEText

logging.basicConfig(filename='loggings.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')

class Carpet: 
    def __init__(self):
        self.response_carpet = requests.get('https://www.maisonsdumonde.com/FR/fr/c/tapis-1559ac122904996dcae8be4c5de8fda6') #je prends les infos from mon url 
        self.maison_du_monde_carpet = self.response_carpet.text 
        self.data = BeautifulSoup(self.maison_du_monde_carpet,"html.parser") #permet de rcuprer la data de ma page sous forme HTML 
        self.carpet_name_list = []
        self.carpet_price_list = []
        self.final_carpet = []

    def name_carpet(self):
        logging.info('Getting my carpets name from HTML into a list: start')
        carpet_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            unidecodizer = unidecode.unidecode(title)
            #print(unidecodizer)
            carpet_name.append(unidecodizer)
            self.carpet_name_list.append(carpet_name[k])
        logging.info('Getting my carpets name from HTML into a list: end')

        return self.carpet_name_list

    def price_carpet(self):
        logging.info('Getting my carpets price from HTML into a list: start')
        carpet_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            carpet_price.append(price)
            self.carpet_price_list.append(carpet_price[k].split()[0])
        logging.info('Getting my carpets price from HTML into a list: end')

        return self.carpet_price_list
    
    def zip_list_carpet(self): 
        logging.info('Zipping all my lists in tuple: start')

        self.final_carpet = list(zip(self.carpet_name_list, self.carpet_price_list))
        #print(self.final_carpet)
        #print(type(self.finale_carpet))
        logging.info('Zipping all my lists in tuple: end')

        return self.final_carpet

c = Carpet()
c.name_carpet()
c.price_carpet()
c.zip_list_carpet()


class Mirror: 
    def __init__(self): 
        self.response_mirror = requests.get('https://www.maisonsdumonde.com/FR/fr/c/miroirs-484554f26aa42ef448cafd6fe7ad385e') #je prends les infos from mon url 
        self.maison_du_monde_mirror = self.response_mirror.text 
        self.data = BeautifulSoup(self.maison_du_monde_mirror,"html.parser")
        self.mirror_name_list = []
        self.mirror_price_list = []
        self.final_mirror = []

    def name_mirror(self):
        logging.info('Getting my mirros name from HTML into a list: start')
        mirror_name = []
        title_name = self.data.find_all("h2", class_= "font-weight-normal expand-link name mb-0")

        for k, item in enumerate(title_name):
            title = item.getText()
            unidecodizer = unidecode.unidecode(title)
            mirror_name.append(unidecodizer)
            self.mirror_name_list.append(mirror_name[k])
        return self.mirror_name_list
        #print(self.mirror_name_list)

        logging.info('Getting my mirrors name from HTML into a list: end')

    def price_mirror(self):
        logging.info('Getting my mirror price from HTML into a list: start')
        mirror_price = []
        price_text = self.data.find_all("div", class_="ml-auto font-weight-semibold price")

        for k, item in enumerate(price_text): 
            price = item.getText()
            mirror_price.append(price)
            self.mirror_price_list.append(mirror_price[k].split()[0])
        return self.mirror_price_list
        #print(self.mirror_price_list)

        logging.info('Getting my carpets price from HTML into a list: end')

    def zip_list_mirror(self):
        logging.info('Zipping all my lists in tuple: start')

        result_mirror= list(zip(self.mirror_name_list, self.mirror_price_list)) 
        #print("This is my result:" , result)
        #print(self.final_mirror)
        logging.info('Zipping all my lists in tuple: end')

        return result_mirror

m = Mirror()
m.name_mirror()
m.price_mirror()
m.zip_list_mirror()

'''
sender = "tminguet.simplon@gmail.com"
receivers = "tiphaine.minguet@gmail.com"
body_of_email = "Something is new on Maison du Monde, go check !"

msg = MIMEText(body_of_email, "html")
msg["Subject"] = "Scrapping Text"
msg["From"] = sender
msg["To"] = receivers

s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
s.login(user="tminguet.simplon@gmail.com", password="simplon2021")
s.sendmail(sender, receivers, msg.as_string())
s.quit()
'''
