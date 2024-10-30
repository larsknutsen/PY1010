# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:05:12 2024

@author: lars
"""

clear = "\n" * 10 #legger 10 linjeskift til variabel clear
print (clear) #printer variabel clear (linjeskiftene) for å gjøre konsollet mer lesbart ved kjøring av program

km = float(input("Hvor mange km skal du kjøre? "))
bom = int(input("Hvor mange bompasseringer har du pr år? ")) 
forsikring_el = 5000 #laget variabel da satsen kan endres med tiden
forsikring_bensin = 7500 # laget variabel da satsen kan endres med tiden
trafikkforsikring_el = 365*8.38 #utregning, da satsen kan endres med tiden
trafikkforsikring_bensin = 365*8.38 #utregning, da satsen kan endres med tiden
forbruk_el = float(0.2 * km * 2) # regner ut kostnader for forbruk elbil
forbruk_bensin = km #slurvet litt, siden det er 1,- pr km (kostnader forbruk bensinbil)
bom_el = 0.1 * km # regner ut kostnader for bompasseringer elbil
bom_bensin = 0.3 * km # regner ut kostnader for bompasseringer bensinbil

el = forsikring_el + trafikkforsikring_el + forbruk_el + bom_el # legger sammen alle kostnader for elbil
el = round(el, 2) #runder av med 2 desimaler
bensin = forsikring_bensin + trafikkforsikring_bensin + forbruk_bensin + bom_bensin #legger sammen alle kostnader for bensinbil
bensin = round(bensin, 2) #runder av med 2 desimaler

diff = bensin - el # regner ut differanse bensinbil-elbil


print ("Det koster ", el, " å kjøre elbil ett år")
print ("Det koster ", bensin, " å kjøre bensinbil ett år")
print ("Differansen er ", diff)


