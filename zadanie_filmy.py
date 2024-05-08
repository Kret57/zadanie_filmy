import os
import random
from faker import Faker
from datetime import datetime


class filmy:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        
        self.liczba_odtworzen=0

    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'
    
    def play(self):
        self.liczba_odtworzen+=1
    
class seriale(filmy):
    def __init__(self,numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka=numer_odcinka
        self.numer_sezonu=numer_sezonu

    def __str__(self):
        return f'{self.tytul} S{"{:02d}".format(self.numer_sezonu)}E{"{:02d}".format(self.numer_odcinka)}'
        
    def play(self):
        self.liczba_odtworzen+=1

film1=filmy(tytul="The Shawshank Redemption", rok_wydania=1994, gatunek="Dramat")
film2=filmy(tytul="Intouchables", rok_wydania=2001, gatunek="Biograficzny / Dramat / Komedia")
film3=filmy(tytul="The Green Mile", rok_wydania=1999, gatunek="Dramat")
film4=filmy(tytul="The Godfather", rok_wydania=1972, gatunek="Dramat / Gangsterski")
film5=filmy(tytul="12 Angry Men", rok_wydania=1957, gatunek="Dramat sądowy")

serial1=seriale(tytul="Chernobyl",rok_wydania=2019, numer_odcinka=1, numer_sezonu=1, gatunek="Dramat")
serial2=seriale(tytul="Breaking Bad",rok_wydania=2008, numer_odcinka=1, numer_sezonu=1, gatunek="Dramat / Kryminał")
serial3=seriale(tytul="Game of Thrones",rok_wydania=2011, numer_odcinka=1, numer_sezonu=1, gatunek="Dramat / Fantasy / Przygodowy")
serial4=seriale(tytul="Band of Brothers",rok_wydania=2001, numer_odcinka=1, numer_sezonu=1, gatunek="Dramat / Wojenny")
serial5=seriale(tytul="Sherlock",rok_wydania=2010, numer_odcinka=1, numer_sezonu=1, gatunek="Dramat / Kryminał")

lista=[film1, film2, film3, film4, film5, serial1, serial2, serial3, serial4, serial5]

def get_movies(list):
    movie_list=[]
    for item in list:
        if item.__class__==filmy:
            movie_list+=[item]
    movie_list=sorted(movie_list, key=lambda item:item.tytul)
    
    return movie_list

def get_series(list):
    series_list=[]
    for item in list:
        if item.__class__==seriale:
            series_list+=[item]
    series_list=sorted(series_list, key=lambda item:item.tytul)
    
    return series_list

def search(list):
    szukany_film=input("Podaj nazwe serialu lub filmu: ")
    jest=False
    for item in list:
        if item.tytul==szukany_film:
            jest=True
            wynik=item
    if jest:
        print(wynik)
    else:
        print("Nie ma takiego tytulu na liscie")

def generate_views_x10(func):
    def wrapper(list):
        for i in range(10):
            func(list)
    return wrapper 

@generate_views_x10
def generate_views(list):
    item=random.choice(list)
    for i in range(random.randint(1, 100)):
        item.play()
    #print(f"{item} - {item.liczba_odtworzen}") #sprawdzanie

def top_titles_input(list):
    toplist=sorted(list, key=lambda item:item.liczba_odtworzen)
    ilosc=input("Podaj liczbe pozycji ktore chesz wyswietlic: ")
    for i in range(int(ilosc)):
        print(toplist[i])

def top_titles(list,repet):
    toplist=sorted(list, key=lambda item:item.liczba_odtworzen)
    for i in range(int(repet)):
        print(toplist[i])

def add_series(list):
    while True:
        con=input("\nCzy chesz dodac kolejny serial? t/n: ")
        if con!='t':
            break

        title=input("Podaj tytul: ")
        year=input("Rok wydania: ")
        genre=input("Gatunek: ")
        season_number=input("Numer sezonu: ")
        episode_number=input("Numer odcinka: ")

        new=seriale(tytul=title,rok_wydania=year, numer_odcinka=season_number, numer_sezonu=episode_number, gatunek=genre)
        if new:
            list+=[new]

if __name__ == "__main__":
    os.system('clear')
    print("Biblioteka filmów!")
    print("\nOto lista filmów:")
    print()
    lista_filmow=get_movies(lista)
    for item in lista_filmow:
        print(item)
    print("\nlista seriali:")
    print()
    lista_seriali=get_series(lista)
    for item in lista_seriali:
        print(item)
    add_series(lista)
    generate_views(lista)
    data=datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {data} \n")
    top_titles(lista,3)
    
