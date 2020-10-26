import time
import sys

print("Hello jij daar!, Ik ben Leon")
print("Wie ben jij?")

name = input("Typ je naam hier in : ")

print("Aangenaam te maken ",name)
time.sleep(0.5)
print('\n')
print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
time.sleep(1)
print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen")
time.sleep(1)
print('\n''\n''\n''\n')
print("Voordat ik naar het Mediacollege ging op welke school zat ik toen?")
time.sleep(1)
print("         A. Kennemercollege Mavo Heemskerk")
print("         B. Clusiuscollege Mavo Castricum")
print("         C. Kennemercollege Havo Heemskerk")

andwoord1 = input("Kies A, B of C : ").upper()

if andwoord1 == 'A':
    
    print("goed zo A was inderdaad goede andwoord")
    
if andwoord1 == 'B':
    
    print("sorry",name,"maar het goede andwoord was A niet",andwoord1)
    
if andwoord1 == 'C':
    
    print("sorry",name,"maar het goede andwoord was A niet",andwoord1,", helaas")

time.sleep(1)

print('\n''\n''\n''\n')
print("Welke opleiding doe ik momenteel?")
time.sleep(1)
print("         A. Nova College Amsterdam")
print("         B. Havo Kennemercollege")
print("         C. Mediacollege Amsterdam")

andwoord1 = input("Kies A, B of C : ").upper()

if andwoord1 == 'A':
    
    print("sorry maar het goede andwoord was C")
    
if andwoord1 == 'B':
    
    print("oof het goede andwoord was C",name)
    
if andwoord1 == 'C':
    
    print("woow goed gedaan",name,"dat heb je goed")

time.sleep(1)

exit()
