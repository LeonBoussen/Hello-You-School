import sys
import time

print('\n')
print('\n')
print('\n')
print('\n')
time.sleep(1)
print("You Need To Install pyfiglet, termcolor and colorama to be able to run this script"'\n')
time.sleep(3)
print("To Install Those Type:"'\n'"pip install pyfiglet"'\n'"and"'\n'"pip install termcolor"'\n'"and"'\n'"pip install colorama"'\n')
print('\n'"if those are installed the script will run in 5 seconds")
time.sleep(5)

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Hello You', font='doom'),
       'green', 'on_blue', attrs=['bold'])

time.sleep(1)

cprint(figlet_format('ik ben Leon', font='doom'),
       'green', 'on_blue', attrs=['bold'])

time.sleep(1.5)

cprint(figlet_format('Wie Ben Jij?', font='doom'),
       'green', 'on_blue', attrs=['bold'])
       
name = input ("type je naam hier: ")

cprint(figlet_format('Hello', font='doom'),
       'green', 'on_blue', attrs=['bold'])

cprint(figlet_format(name, font='doom'),
       'green', 'on_blue', attrs=['bold'])