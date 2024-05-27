import os

fichier=open('/etc/bind/named.conf.local', 'w')
fichier.write('zone "mon.lan" {\ntype master;\nfile "/etc/bind/db.mon.lan";\n};')
fichier.close()

os.system('touch /etc/bind/db.mon.lan')

fichier2=open('/etc/bind/db.mon.lan', 'w')
XX=str(input("Entrez votre numero de binome XX: "))
fichier2.write('$TTL 3h\n@ IN SOA ns.mon.lan. mailaddress.mon.lan. (\n2021051701\n6H\n1H\n5D\n1D)\n@ IN NS ns.mon.lan.\n@ IN MX 10 mail.mon.lan.\nns A 10.200.'+XX+'.1\nserveur A 10.200.'+XX+'.1\nclient A 10.200.'+XX+'.2\nrouteurXX A 10.200.'+XX+'.254\ncommutXX A 10.200.'+XX+'.253\nwww.site1 CNAME serveur')
fichier2.close()

os.system('named-checkconf named.conf')
os.system('named-checkzone mon.lan db.mon.lan')
os.system('service bind9 restart')
os.system('service bind9 status')