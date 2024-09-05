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

x = input("1-kea /n 2-isc : ")
if x == "isc":
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

elif x == "kea":
	print("sah y a r pour l'instant")
	#fichier = open('/etc/kea/kea-dhcp4.conf')
	#fichier.write('{\n   "Dhcp4" : {\n   "valid-lifetime": ' + maxTime + ',\n   "renew-timer": '+defaultTime + ',\n "subnet4": [\n   "subnet":\n   "' +numeroReseau+'/24",\n   "pools": [\n{\n   "pool":\n"'+ firstAddr + '-' + lastAddr+'"\n}\n],\n"option-data": [\n{\n"name":\n"routers",\n   "data":\n"' + router + '",\n   },\n{\n   "name":\n"domain-name-servers",\n   "data":\n"' + dns + '}]}]}}')





