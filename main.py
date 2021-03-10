from webscrap import *
from postgres import *

############# Webscrapping de mes infos depuis Maison du Monde: infos sur les Tapis 
c = Carpet()
c.name_carpet()
c.price_carpet()
c.zip_list_carpet()

m = Mirror()
m.name_mirror()
m.price_mirror()
m.zip_list_mirror()

############# Creation de ma table avec les infos de mon webscrapping 

#t = Table()
#t.erase_table()
#t.create_table()
#t.insert_info()