import time
import os

os.system("cls")

curvraag = 0;     # 0 = intro

intro = 0;
vraag1 = 1;
antwoord1 = 0;
vraag2 = 0;
antwoord2 = 0;
vraag3 = 0;
antwoord3 = 0;
vraag4 = 0;
antwoord4 = 0;
vraag5 = 0;
antwoord5 = 0;
vraag6 = 0;
antwoord6 = 0;
vraag7 = 0;
antwoord7 = 0;
vraag8 = 0;
antwoord8 = 0;
vraag9 = 0;
antwoord9 = 0;
vraag10 = 0;
antwoord10 = 0;
vraag11 = 0;
antwoord11 = 0;
vraag12 = 0;
antwoord12 = 0;
vraag13 = 0;
antwoord13 = 0;
vraag14 = 0;
antwoord14 = 0;
vraag15 = 0;
antwoord15 = 0;
vraag16 = 0;
antwoord16 = 0;
vraag17 = 0;
antwoord17 = 0;
vraag18 = 0;
antwoord18 = 0;
vraag19 = 0;

while intro == 1:
    print("Welkom in mijn tekstbased applicatie.")
    time.sleep(1)
    print("Je moet als persoon keuzes maken om te overleven, iedere keuze die je maakt heeft invloed op je volgende vragen")
    time.sleep(3)
    print("Laten we beginnen")
    input('\n'"klik op Enter om te starten..")
    os.system("cls")
    print("Story Line: "'\n''\n'"Je bent een man van 30 in iran en IS komt dicht in de beurd van je dorp en er is oorog. wat ga jij doen?")
    time.sleep(2)
    input('\n'"klik op Enter om te verder te gaan..")
    os.system("cls")
    vraag1 = 1;
    intro = 0;
    break
    
while vraag1 == 1:
    print("IS kont in de buurt van jouw drop, blijf je of ga je weg?")
    antwoord1 = input("A = blijven of B = vluchten: ").upper()
    os.system("cls")
    break

while antwoord1 == 'A':
    vraag2 = 1; 
    break

while antwoord1 == 'B':
    vraag11 = 1;
    break

while vraag11 == 1:
    os.system("cls")
    print('\n'"ga je met een smokkelaar mee of ga je zelf proberen weg te komen?")
    antwoord11 = input("A = zelf of B smokkelaar : ").upper()
    os.system("cls")
    break

while antwoord11 == 'A': 
    print('\n'"Je bent IS territorium in gereden") 
    input('\n'"klik op Enter om te verder te gaan..")
    os.system("cls")
    print("je bent gespot door IS en je komt onder vuur te liggen")
    input('\n'"klik op Enter om te verder te gaan..")
    os.system("cls")
    print("je bent geraakt en de verwonding is doodelijk"'\n''\n'"je hebt het niet overleef")
    time.sleep(5)
    exit()
    break

while antwoord11 == 'B':
    vraag12 = 1;
    break

while vraag12 == 1:
    os.system("cls")
    print('\n'"de smokkelaar geeft je een keuze tussen gaan met een auto of boot. welke kies je?")
    antwoord5 = input("A = Auto of B = Boot : ").upper()
    break

while vraag2 == 1:
    os.system("cls")
    print('\n'"IS is nu je dorp in gekomen. dit is je laaste kans om weg te komen. blijf je of ga je weg?")
    antwoord2 = input("A = Blijven of B = Vluchten : ").upper()
    break

while antwoord2 == 'A':
    os.system("cls")
    print("IS strijders hebben je je huis uit getrokken")
    input('\n'"klik op Enter om te verder te gaan..")
    os.system("cls")
    print("Je wordt openbaar geëxecuteerd omdat ze je haram vinden")
    time.sleep(5)
    exit()
    break

while antwoord2 == 'B':
    vraag3 = 1;
    break

while vraag3 == 1:
    os.system("cls")
    print('\n'"je bent net aan het drop uit gekomen")
    input('\n'"klik op Enter om te verder te gaan..")
    os.system("cls")
    print("ga je proberen je familie ook te redden of ga je alleen vuchten")
    antwoord3 = input("A = je gaat je familie ook proberen te redden of B  = Je gaat zelf proberen te vluchten : ").upper()
    break

while antwoord3 == 'A':
    vraag4 = 1;
    break

while antwoord3 == 'B':
    vraag13 = 1;
    break 

while vraag13 == 1:
    os.system("cls")
    print('\n'"je bent peronlijke over een landmine gereden.")
    time.sleep(5)
    print("je bent overleden in het ongeluk")
    time.sleep(1)
    exit()
    break

while vraag4 == 1:
    os.system("cls")
    print('\n'"je gaat terug naar het dorp maar ziet dat 90% kapot is. ga je opzoek of ga je weg?")
    antwoord4 = input("A = je gaat opzoek of B = je gaat weg voor je eigen veiligheid : ").upper()
    break

while antwoord4 == 'A': 
    vraag5 = 1;
    break

while antwoord4 == 'B':
    print("Niet slim om te blijven zoals al was gezegd zou je neergeschoten worden!")
    break

while vraag5 == 1:
    os.system("cls") 
    print('\n'"je ziet dat extreem veel mensen dood zijn. ga je alsnog door met zoeken?")
    antwoord5 = input("A = door gaan of B = weg gaan : ").upper()
    break

while antwoord5 == 'A':
    vraag14 = 1;
    break

while antwoord5 == 'B':
    vraag6 = 1;
    break

while vraag14 == 1:
    os.system("cls")
    print('\n'"je hoorde een kogel schot. dit is je laaste kans om weg te gaan. ga je of blijf je?")
    antwoord14 = input("A = je gaat weg of B je blijft toch : ").upper()
    break

while antwoord14 == 'A':
    vraag15 = 1;
    break

while antwoord14 == 'B':
    print('\n'"je wordt gespot en opgeblazen met een bazoeka")
    time.sleep(5)
    print("je overleeft dit niet")
    time.sleep(5)
    exit()
    break

while vraag15 == 1:
    os.system("cls")
    print('\n'"doordat je weg bent gegaan heb je het net aan overleeft. probeer je naar een buurland te gaan of naar europa")
    antwoord15 = input("A = buur land of B europa : ").upper()
    break

while antwoord15 == 'A':
    print('\n'"je bent onderweg gespot door IS")
    time.sleep(5)
    print("je bent omgekomen in een aanval op je door IS")
    time.sleep(5)
    exit()
    break

while antwoord15 == 'B':
    vraag16 = 1; 
    break

while vraag16 == 1:
    os.system("cls")
    print('\n'"je hebt het gered naar italië probeer je hier een verblijfsvergunning aan te vragen of ga je door europa in?")
    antwoord16 = input("A = je vraagt een verblijfsvergunning aan of B = je gaat door : ").upper()
    break 
# dsfdsfgsdhsfghdfghdfg
while antwoord16 == 'A':
    vraag17 = 1;
    break

while antwoord16 == 'B':
    vraag18 = 1;
    break

while vraag17 == 1:
    os.system("cls")
    print('\n'"je hebt een verblijfsvergunning aan gevraagd.")
    time.sleep(5)
    print("en gelukkig heb je die ook gekreken, je mag blijven in italië")
    break

while vraag18 == 1:
    os.system("cls")
    print('\n'"je hebt er voor gekozen om door te rijden naar europa. ga je naar duitsland of frankrijk?")
    antwoord18 = input("A = Duitsland of B = Frankrijk : ").upper()
    break

while antwoord18 == 'A':
    vraag19 = 1;
    break

while antwoord18 == 'B':
    print('\n'"je wordt toegang geweigerd tot Frankrijk en wordt opgepakt en terug gestuurd naar Iran")
    break

while vraag6 == 1:
    os.system("cls")
    print('\n'"je bent gaan door zoeken en gevrangen genomen door IS, ga te weg renne of wacht je op een beter moment")
    antwoord6 = input("A = weg rennen of B beter moment : ").upper()
    break

while antwoord6 == 'A':
    os.system("cls")
    print("door dat je bent weg gerend ben je gespot en direct dood geschoten")
    time.sleep(5)
    exit()
    break

while antwoord6 == 'B':
    vraag7 = 1;
    break

while vraag7 == 1:
    os.system("cls")
    print('\n'"het lijkt nu rusrig te zijn, ga je weg rennen of blijf je voor een beter moment?")
    antwoord7 = input("A = weg rennen of B = blijven : ").upper() 
    break

while antwoord7 == 'A':
    vraag8 = 1;
    break

while antwoord7 == 'B':
    print('\n'"je hebt te lang gewacht en je wordt dood geschoten")
    break

while vraag8 == 1:
    os.system("cls")
    print('\n'"je bent net aan ontsnapt maar je handen zijn nog vast gebonden. vraag je hulp aan een random persoon of ga verdere renne met je handen vast?")
    antwoord8 = input("A = vragen of B = verder gaan : ").upper()
    break

while antwoord8 == 'A':
    print('\n'"je vraagt aan een random persoon voor hulp")
    time.sleep(5)
    print("de persoon waar je hulp aan vraagt blijkt een vrijheids strijder te zijn tegen IS")
    time.sleep(5)
    print("hij helpt je veilig naar het vliegveld en geeft je geld voor vlieg tickets")
    time.sleep(5)
    print("je komt aan in belgie met het vliegtuig en een fake paspost en vraagt een verblijfsvergunning gaan")
    time.sleep(5)
    print("verblijfsvergunning krijg je maar je moet wel taakstraf uitvoeren voor het reizen met een fake pasport")
    break

while antwoord8 == 'B':
    vraag9 = 1;
    break

while vraag9 == 1:
    os.system("cls")
    print('\n'"")
    print("je bent verder de woestijn in gegaan met nog je handen vast")
    time.sleep(5)
    print("uiteindelijk ga je dood duur uitdroging")
    time.sleep(5)
    exit()
    break

while vraag19 == 1:
    os.system("cls")
    print("je hebt duitsland in gekomen")
    time.sleep(5)
    print("je heb een verblijfsvergunning aan gevraagd")
    time.sleep(5)
    print("die heb je ook gekregen. je mag in duitsland bijven")
    time.sleep(5)
    exit()