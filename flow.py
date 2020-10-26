import time
import os

os.system("cls")

x = 1;
c = 0;
z = 0;
e = 0;
d = 0;
q = 0;
f = 0;


while x == 1:
    print ("welkom bij mijn flowchart")
    x = input("Type 'start' om te starten en 'stop' om te stoppen : ").upper()
    print('\n''\n')

while x == 'START':
    print("oke, ik ga een praat vragen aan jou stellen en jij moet het goede antwoord raden")
    print('\n')
    time.sleep(2)
    print("je vragen worden aangepast op welke antwoorden je geeft")
    print('\n')
    time.sleep(2)
    print("laten we beginnen........")
    time.sleep(2)
    print('\n''\n''\n''\n')
    print("op welke school zit ik momenteel")
    print("A - Mediacollege Amsterdam")
    print("B - Novacollege Amsterdam")
    print('\n')
    z = input("Type hier A of B : ").upper()
    break
    

while x == 'STOP':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("----------------------------------------------------")
    print('\n')
    print("Quiting Script")
    print('\n')
    print("----------------------------------------------------")
    time.sleep(3)
    exit()
    
while z == 'A':
    print("wouw dat was het goede andwoord, ik zit inderdaat momenteel op he Mediacollege")
    time.sleep(2)
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("welke opleiding doe ik nu?")
    print("A - software dev")
    print("B - audiovisueel")
    print('\n')
    c = input("Type hier A of B : ").upper()
    break

while z == 'B':
    print("oof sorry dat was niet correct, ik zit momenteel op het Mediacollege")
    time.sleep(2)
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("doe ik een sport?")
    print("A - nee, geen sport")
    print("B - voetbal")
    print('\n')
    d = input("Type hier A of B : ").upper()
    break

while c == 'A':
    print("jaa jaa ik doe inderdaad software developement")
    time.sleep(2)
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("hoelang duurt mijn opleiding?")
    print("A - 3 jaar")
    print("B - 4 jaar")
    print('\n')
    e = input("Type hier A of B : ").upper()
    break
    

while e == 'A':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("Bijna, mijn opleiding duurt 4 jaar")
    time.sleep(2)
    q= "s"
    break

while e == 'B':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("goed geraden, het duurt inderdaad 4 jaar")
    time.sleep(2)
    q= "s"
    break

while c == 'B':
    print("helaas, ik doe software developement")
    time.sleep(2)
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("hoe oud denk je dat ik ben?")
    print("A - 16 jaar")
    print("B - 17 jaar")
    print('\n')
    f = input("Type hier A of B : ").upper()
    break
    
while d == 'A':
    print("dat heb je correct, ik doe momenteel even geen sport meer")
    time.sleep(2)
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("hoe oud denk je dat ik ben?")
    print("A - 16 jaar")
    print("B - 17 jaar")
    print('\n')
    f = input("Type hier A of B : ").upper()
    break

while d == 'B':
    print("damn sorry bro, ik vind voetbal niet leuk")
    print("en doe momenteel geen sport")
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    time.sleep(2)
    q= "s"
    break
    
while f == 'A':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("close ik ben 17 niet 16 :) ")
    time.sleep(2)
    q= "s"
    break
    
while f == 'B':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("woow goed geraden")
    time.sleep(2)
    q= "s"
    break

while q == 's':
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    print("--------------------------------------------------------")
    print("dit is het alweer het einde van mijn flowchart")
    print("het was leuk om te maken maar het kosten best veel tijd")
    print("--------------------------------------------------------")
    print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
    time.sleep(9999)
    

else:
    print("--------------------------------------------------------")
    print("That was an incorrect input :( ")
    print("--------------------------------------------------------")
    time.sleep(2)
    exit()
    