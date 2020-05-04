import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
#--------------------------------------------------------------------------------------


#Liste des addresse des matches inclue dans les données
listAddress = pd.read_csv("../leagueoflegends/scrapper/matchinfo.csv")
localisation_du_fichier = "../leagueoflegends/matchinfo_date.csv"


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

#--------------------------------------------------------------------------------------------------
#test de la fonction

#Dans cette partie nous parcourons les addresses contenu dans le dataframe et nous en recuperons la date. Cette date est pas la suite mis dans une nouvelle colone d'un dataframe
print("Debut boucle 3sec")
time.sleep(10)





i= 0 #Addresse de debart
j = 3075 #Addresse de fin

while i <= j:
    #Ouvre le fichier csv que l'on utilise pour mettre les dates
    tableau = pd.read_csv(localisation_du_fichier)

    #Va a l'addresse de la boucle
    adressActuelle = tableau.loc[i,"Address"]
    browser.get (adressActuelle)
    time.sleep(2.5) # Attend que la page charge

    #Execution du Js de la page
    html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, features="lxml")

    #Trouve la date du match
    date = soup.find("span", {"class": "map-header-date"}).get_text()
    print("{} --type : {}".format(date, type(date)))


    listAddress.loc[i,"Date"] = date

    #On s'assure de ce qu'on recuperent et on l'exporte
    listAddress.to_csv(localisation_du_fichier)

    date = ""
    #On garde en vue la progression de notre boucle
    print("{} boucles sur {} terminés".format(i,j))
    i += 1


#Export du dataframe qu'on a fait


browser.quit()
