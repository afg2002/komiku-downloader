import requests 
import wget
import os
from PIL import Image
from bs4 import BeautifulSoup


def check_all_manga():
    url = 'https://komiku.co.id/daftar-komik/'
    main_page = requests.get(url)
    soup = BeautifulSoup(main_page.content,'lxml')
    card = soup.findAll('li',class_="ranking1")

    print("---------List Manga/Komik---------")
    
    nama_manga_array = []


    for p in card :
        nama_manga = p.find('h4')
        link = p.find('a')['href']
        nama_manga_array.append(nama_manga)

        print(nama_manga.text + " || " + link)
        
    print("Total manga yang tersedia : " + str(len(nama_manga_array)))


def search_manga(link):
    url = "https://komiku.co.id/manga/"+link.replace(" ","-")
    main_page = requests.get(url)
    soup = BeautifulSoup(main_page.content,'lxml')
    td = soup.findAll('td',class_="judulseries")

    for x in td :
        link_chapter = x.find('a')
        print(link_chapter.text + " || " + link_chapter['href'])
    
def download_manga(link_chapter):
    url = link_chapter
    main_page = requests.get(url,verify=False)
    soup = BeautifulSoup(main_page.content,'lxml')
    os.mkdir(soup.title.text)
    image = []
    
    
    for divdata in soup.findAll('div',id="Baca_Komik"): 
        for img in divdata.findAll('img'):
            url = img['src']
            image_name = url.strip('https://i0.wp.com/cdn.komiku.co.id/wp-content/uploads/')
            image.append(image_name)
            wget.download(url,'./'+soup.title.text)
            
        
    
    print("Download Sucessfully")
    print("Made with love by afghan eka pangestu ")

            
    

ans = True
while ans:
    print("""
    1. List Manga
    2. Search Manga
    3. Download Manga
    4. Exit/Quit

    NOTE : LINK HARUS BERASAL DARI : https://komiku.co.id/

    """)

    ans = input("Pilih menu :")

    if ans == "1":
        check_all_manga()
    elif ans == "2":
        search_manga(input("Masukkan nama manga : "))
    elif ans == "3":
        download_manga(input("Masukkan link chapter manga : "))
    elif ans=="4":
        print("\n Goodbye")
        ans = None
    else:
        print("\n Not Valid Choice Try Again")


# 'cek_manga' : check_all_manga(),
#     'search_manga' : search_manga(input("Masukkan link manga (source : https://komiku.co.id/) : ")),
#     'download_manga' : download_manga(input("Masukkan link chapter manga (source : https://komiku.co.id/) : "))
