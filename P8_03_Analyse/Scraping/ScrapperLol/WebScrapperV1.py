import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
#--------------------------------------------------------------------------------------

#TODO : faire le dernier paquet.

#Liste des addresse des matches inclue dans les données
listAddress = pd.read_csv("../leagueoflegends/matchinfo.csv")

#Séparation des addresse en plusieurs dataframe plus petit

# listAddress_1 = listAddress.iloc[0:1000].copy()
# listAddress_2 = listAddress.iloc[1000:2000].copy()
# listAddress_3 = listAddress.iloc[2000:3000].copy()
# listAddress_4 = listAddress.iloc[3000:4000].copy()
# listAddress_5 = listAddress.iloc[4000:5000].copy()
# listAddress_6 = listAddress.iloc[5000:6000].copy()
# listAddress_7 = listAddress.iloc[6000:6500].copy()
# listAddress_8 = listAddress.iloc[6500:7000].copy()
# listAddress_9 = listAddress.iloc[7000:7300].copy()
# listAddress_10 = listAddress.iloc[7300:7500].copy()
listAddress_11 = listAddress.iloc[7500:7550].copy()
listAddress_12 = listAddress.iloc[7550:len(listAddress)].copy()





lAdressTotal = [listAddress_11,listAddress_12]


#Chemin de l'executable requis par selenium
browser = webdriver.Chrome(executable_path='/home/kozame/Téléchargements/chromedriver_linux64/chromedriver')

#Amorce le site
browser.get ("http://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/30030?gameHash=fbb300951ad8327c")

print("Etape 1: Login")
time.sleep(5) #Temp pour ce loger

#Une fois sur la page de connection, les remplissage sont automatiser
browser.find_element_by_name("username").send_keys("LeFaucheur1971")
browser.find_element_by_name("password").send_keys("Gowenus117")
browser.find_element_by_name("region").send_keys("EUN1")

#Non utile apres verification
# print("Etape 2")
# time.sleep(10)
# browser.get ("http://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/30030?gameHash=fbb300951ad8327c")

#--------------------------------------------------------------------------------------------------
#test de la fonction
#ici on va executer le javascript de la page, puis parsser cette page a l'aide de BeautifulSoup, car si on ce sert que de selenium, le code source ne prend pas en compte le javascript
# print("Etape 3")
# time.sleep(1)
# #Execution du js
# html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
# #Parcege et recuperation de l'element voulue
# soup = BeautifulSoup(html, features="lxml")
# date = soup.find("span", {"class": "map-header-date"}).get_text()
# #On l'affiche ici avant notre boucle pour etre sur que tout va bien
# print(date)
# date=""
#--------------------------------------------------------------------------------------------------

#Dans cette partie nous parcourons les addresses contenu dans le dataframe et nous en recuperons la date. Cette date est pas la suite mis dans une nouvelle colone d'un dataframe
print("Debut boucle 3sec")
time.sleep(3)
numero = 11
for tab in lAdressTotal:

    i= tab.index.min() #Addresse de debart
    j = tab.index.max() #Addresse de fin
    print("boucle n°{}".format(numero))

    while i <= j:
        # len(listAddress)

        #Peut etre voire un system de test de chargement de la page, et un temp de pause en fct de ce qui est charger.
        adressActuelle = listAddress.loc[i,"Address"]
        browser.get (adressActuelle)
        time.sleep(2)
        html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, features="lxml")
        date = soup.find("span", {"class": "map-header-date"}).get_text()
        listAddress.loc[i,"Date"] = date
        print(date) #On s'assure de ce qu'on recuperent.
        date = ""
        #On garde en vue la progression de notre boucle
        print("{} boucles sur {} terminés".format(i,j))
        i += 1

    localisation_du_fichier = "../leagueoflegends/infomatch_date{}.csv".format(numero)
    print(" localisation du fichier :'{}'".format(localisation_du_fichier))
    #Export du dataframe qu'on a fait
    listAddress.to_csv(localisation_du_fichier)
    numero += 1

browser.quit()
