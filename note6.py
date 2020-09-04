import os
import time
import sys
import socket
from telnetlib import Telnet
import wikipedia

lmao = input("do you want to review the notes? (y/n): ")

ip = ""

port = ""


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if lmao == "y":
	time.sleep(0.5)
	oof = input("""

Absolutism in some europe place
france
louis XIV
absolutism held all power
diving right
responisble only to god	example for europe


Richelieu
preserved authority of the monarch 50 years before louis XIV


Louis in power
1661 new king 23 years old
myth of the SUN KING
relocated palae to versailles
kept nobles buys w court life + rewards


Spread absolutism
spain:nobles won against kind phillip spain lost their power
prussia: frederick williams takes territory by force. 4th largest army
austrian empire: hapsburgs took over a collection of teritoris; independent of laws/traditions


IVAN IV
siezes muscovy (russia) as czar but chaos reigns after his death
1613:romanov dynasty
1689:
peter the great
absolute ruler
modernized russia
adoopted western tradition
tradition
1725: great military powers

Press Enter To Move on: """)
	time.sleep(1)
	print("""

HERE, HAVE A COOL STAR WARS EPISODE MADE ENTIRELY IN TERMINAL
 		you deserve it :)
""")
	time.sleep(1)
	with Telnet('towel.blinkenlights.nl', 23) as tn:
		tn.interact()



elif lmao == "n":
	print("hehe alright i know why ur here")
	time.sleep(1)
	with Telnet('towel.blinkenlights.nl', 23) as tn:
		tn.interact()
