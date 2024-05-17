import os



os.system("apt-get install isc-dhcp-server")
fichier  = open('/etc/dhcp/dhcpd.conf', 'w')
fichier.write("subnet" + input("numero de reseau :") + input("masque :") + "{"+ "\n" )
firstAddr = input("Premiere adresse :")
lastAddr = input("Derniere adresse :")
fichier.write("range " + firstAddr + " " + lastAddr + ";\n" )
fichier.write("option domain-name-servers" + input("Entrez un dns : ") + ";\n")
domainName = input("Domaine name (O/N):")
if domainName == "O" :
	fichier.write("option domain-name " + input("Entrez un nom de domaine : ") + ";\n")

fichier.write("option routers "+ input("Adresse de votre passerelle : ") + "\n" +"option broadcast-address " + input("adresse broadcast du reseau : ") + ";\n")
if input("Voulez-vous changer le lease-time par defaut (O/N): ") == "O" :
	fichier.write("default-lease-time " + input("default-lease-time : ") + ";\n")
else : 
	fichier.write("default-lease-time 600;\n")
if input("Voulez-vous changer le lease-time maximum (O/N): ") == "O" :
	fichier.write("max-lease-time " + input("max-lease-time : ") + ";\n")
else : 
	fichier.write("default-lease-time 7200;\n}")


fichier.close()	
os.system("service isc-dhcp-server restart")	



