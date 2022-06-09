# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:15:17 2022
"Wizyjna kontrola jakości"
@author: Mikołaj Ratajczak 296706
"""

import numpy as np
import cv2

"""
Funkcja ekran_podsumowania służy do wygenerowania ekranu podsumowania. Argumentami tej funkcji są: liczba zarejestrowanych obiektów,
liczba prawidłowych i wadliwych obiektów, średnia powierzchnia i odchylenie standardowe prawidłowych obiektów. Wielkości te są 
wyświetlane na czarnym ekranie o rozmiarze 200x450. Napisy są białe. Okno podsumowania można zamknąc poprzez wciśnięcie
X lub naciśnięcie dowolnego klawisza na klawiaturze. Ekran ten jest zapisywany jako Podsumowanie.jpg
"""
def ekran_podsumowania(l_obiektow,l_prawidlowych_obiektow,l_wadliwych_obiektow,sr_powierzchnia, odchylenie_standardowe):    
    img = np.zeros(shape=(200,450), dtype=np.uint8)
    cv2.putText(img, text='Przebadanych obiektow: %d' %l_obiektow, org=(30, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.putText(img, text='Prawidlowych obiektow: %d' %l_prawidlowych_obiektow, org=(30, 70), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.putText(img, text='Wadliwych obiektow: %d' %l_wadliwych_obiektow, org=(30, 90), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.putText(img, text='Srednia powierzchnia: %.2f' %sr_powierzchnia, org=(30, 120), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.putText(img, text='Odchylenie standardowe powierzchni: %.2f' %odchylenie_standardowe, org=(30, 140), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255,255,255),thickness=1)
    cv2.imshow('Podsumowanie', img)
    cv2.imwrite('Podsumowanie.jpg',img)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()




j = 0
k = True
start_point = (0, 100)
end_point = (280, 100) 
color = (0, 0, 255)
thickness = 1
suma = 0
wadliwe = 0
prawidlowe = 0
powierzchnia = [] # pusta lista do zapisywania powierzchni kolejnych prawidłowych obiektów

wideo = cv2.VideoCapture('zestaw3.avi') 

while(wideo.isOpened()):
    """
    Odczyt filmu
    """
   
    udany_odczyt, ramka = wideo.read()
    ramka2 = np.copy(ramka)

    if udany_odczyt:
        ramka2 = cv2.line(ramka2, start_point, end_point, color, thickness) # naniesienie czerwonej lini o szerokości 1px na poszczególne klatki filmu
        ramka3 = cv2.cvtColor(ramka, cv2.COLOR_BGR2GRAY)
        ramka3 = cv2.inRange(ramka3, 25, 255)               # ramka3 to zbinaryzowane poszczególne klatki filmu
        ramka4 = ramka3[100]                                # wyodrębnienie 1 linii pixeli. Używane jest do wykrywania obiektów
        cv2.imshow('ramka',ramka2)                          # wyświetlanie filmu z naniesioną czerwoną linią      
        cv2.waitKey(10)                                     # jedna klatka filmu pojawia się co 33ms
        j=j+1                                               # zliczanie ilości klatek. Potrzebne do pominięcia napisów początkowych
    else:   # Po zakończeniu wyświetlania filmu wszystkie otwarte okienka zostaną zamknięte
        wideo.release() 
        cv2.waitKey(1) 
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    
    """
    Rejestracja obiektów na filmie
    """
    
    if j>=65 and any(ramka4==255):  # pierwsza część warunku sprawdza czy napisy początkowe już zniknęły, a druga czy w wyodrębnionej linii filmu pojawił się choć 1 biały piksel co oznacza przejście obiektu przez linię
        if k==True:                 # zmienna k pozwala na jednokrątną rejestrację każdego z obiektów
            k=False                 # po rozpoczęciu rejestracji obiektu zmienna k jest ustawiana na wartość False. Zmienna przyjmuje wartość True gdy obiekt opuści wyodrębnioną linię pikseli (linia 104)
            cv2.imwrite('klatka%d.jpg' %(suma+1),ramka[30:110])                                # zapis klatki obciętej tak aby widoczny był tylko wykryty obiekt
            kl = cv2.imread('klatka%d.jpg' %(suma+1))
            klg = cv2.cvtColor(kl, cv2.COLOR_BGR2GRAY)                                  # klatka w skali szarości          
            kl2 = cv2.inRange(klg, 100, 255)                                            # binaryzowanie klatki w skali szarości tak aby widoczne były tylko obiekty o nieprawidłowej barwie
            prog, kl3 = cv2.threshold(klg,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)    # binaryzowanie klatki w skali szarości tak aby widoczne były wszystkie wykryte obiekty. Próg wyznaczany metodą Otsu          
            
            suma=suma+1     # zliczanie wykrytych obiektów
            
            # wypisywanie liczby dotychczas wykrytych obiektów na klatce
            cv2.putText(kl, text='Razem: %d' %suma, org=(170, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.35, color=(255, 255, 255),thickness=1)
            
            if any(kl2[40,0:280]==255) or np.sum(kl3 == 255)>1300: # pierwsza część warunku sprawdza czy wykryty obiekt ma nieodpowiednią barwę, a druga część sprawdza powierzchnię obiektu w celu wykrycia zniekształceń
                wadliwe = wadliwe+1 # zliczanie wadliwych obiektów
                
                # wypisywanie komunikatu o wadliwym obiekcie oraz liczby dotychczas wykrytych wadliwych obiektów
                cv2.putText(kl, text='Wadliwy', org=(30, 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255),thickness=1)
                cv2.putText(kl, text='Wadliwych: %d' %wadliwe, org=(170, 63), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.35, color=(255, 255, 255),thickness=1)
            
            else:
                prawidlowe = prawidlowe+1   # zliczanie prawidłowych obiektów
                
                # wypisywanie komunikatu o prawidłowym obiekcie oraz liczby dotychczas wykrytych prawidłowych obiektów
                cv2.putText(kl, text='Prawidlowy', org=(30, 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 255, 0),thickness=1)
                cv2.putText(kl, text='Prawidlowych: %d' %prawidlowe, org=(170, 63), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.35, color=(255, 255, 255),thickness=1)
                
                powierzchnia.append(np.sum(kl3 == 255))     # dopisanie powierzchni obiektu do listy
            
            cv2.imshow('klatka',kl)                     # wyświetlanie zarejestrowanych klatek z wypisanymi informacjami  
            cv2.imwrite('klatka%d_opis.jpg' %suma,kl)      # zapis zarejestrowanych klatek z wypisanymi informacjami                    
    else:
        k=True

"""
Podsumowanie
"""

sr_powierzchnia = np.mean(powierzchnia)                                     # obliczenie średniej powierzchni prawidłowych obiektów
odchylenie = np.std(powierzchnia)                                           # obliczenie odchylenia standardowego prawidłowych obiektów
ekran_podsumowania(suma, prawidlowe, wadliwe, sr_powierzchnia, odchylenie)  # wyświetlanie ekranu podsumowania

    

            