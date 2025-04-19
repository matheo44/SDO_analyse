# Détails du chemin vers le serveur SDO avec la date JJ/MM/YYYY souhaitéeimport os
import requests, os
from bs4 import BeautifulSoup


def fetch_img(name_of_img,year,month,day,HMSmin,HMSmax):

    base_url = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
    name_of_img = name_of_img+'.jpg'


    def intervalle(HMS, HMSmin, HMSmax):  
        heure = int(HMS[0:2])
        minutes = int(HMS[2:4])
        sec = int(HMS[4:6])

        h_min, m_min, s_min = HMSmin
        h_max, m_max, s_max = HMSmax

        return (h_min, m_min, s_min) <= (heure, minutes, sec) <= (h_max, m_max, s_max)


    # Fonction pour télécharger une image
    def download_image(url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join('rush', filename), 'wb') as file:
                file.write(response.content)
            print(f"Image téléchargée avec succès et enregistrée sous le nom {filename}")
        else:
            print(f"Échec du téléchargement de l'image depuis {url}")

    # Créer le répertoire 'rush' s'il n'existe pas
    if not os.path.exists('rush'):
        os.makedirs('rush')

       
    url = f'{base_url}{year}/{month}/{day}/'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        for a in soup.find_all('a', href=True):
            link = a['href']
            if name_of_img in link:
                if intervalle(link[9:15],HMSmin,HMSmax):
                    download_image(url + link, link)


# name_of_img = '4096_0131'
# year = '2025'
# month = '04'
# day = '01'
# HMSmin = [10,30,00]
# HMSmax = [13,00,00]

# fetch_img(name_of_img,year,month,day,HMSmin,HMSmax)
