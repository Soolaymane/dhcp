import os




numeroReseau = input("numero de reseau :")
masque = input("masque :")
firstAddr = input("Premiere adresse :")
lastAddr = input("Derniere adresse :")
dns = input("Entrez un dns : ")
router = input("Adresse de votre passerelle : ")
broadcast = input("adresse broadcast du reseau : ")

if input("Voulez-vous changer le lease-time par defaut (O/N): ") == "O" :
	defaultTime = input("default-lease-time : ")

else : 
	defaultTime = "600"
if input("Voulez-vous changer le lease-time maximum (O/N): ") == "O" :
	maxTime = input("max-lease-time : ")

else : 
	maxTime = "7200"

os.system("apt-get install isc-dhcp-server")
fichier  = open('/etc/dhcp/dhcpd.conf', 'w')
fichier.write("subnet " + numeroReseau + " netmask " + masque + "{"+ "\n" )
fichier.write("range " + firstAddr + " " + lastAddr + ";\n" )
fichier.write("option domain-name-servers " + dns + ";\n")
fichier.write("option routers "+ router + ";\n" +"option broadcast-address " + broadcast + ";\n")
fichier.write("default-lease-time " + defaultTime + ";\n")
fichier.write("max-lease-time " + maxTime + ";}")
fichier.close()	
os.system("service isc-dhcp-server restart")	
