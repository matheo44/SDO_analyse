# Détails du chemin vers le serveur SDO avec la date JJ/MM/YYYY souhaitéeimport os
import requests
from bs4 import BeautifulSoup

base_url = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
name_of_img = '4096_0131.jpg'

# Détails du chemin vers le serveur SDO avec la date JJ/MM/YYYY souhaitée
year = '2025'
month = '04'
days = ['01']
HMSmin = [10,30,00]
HMSmax = [13,00,00]
day_sample = True

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

# Boucle à travers les jours et télécharge les images correspondantes
if day_sample:
        for day in days:
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
                        # print(f"Image trouvée et téléchargée : {url + link}")
            else:
                print(f"Erreur lors de la récupération de la page : {response.status_code}")

else:
    for day in days:
        url = f'{base_url}{year}/{month}/{day}/'
        # print(f"Accès à l'URL: {url}")

        response = requests.get(url)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            
            for a in soup.find_all('a', href=True):
                link = a['href']
                if name_of_img in link:
                    download_image(url + link, link)
                    # print(f"Image trouvée et téléchargée : {url + link}")
        else:
            print(f"Erreur lors de la récupération de la page : {response.status_code}")


