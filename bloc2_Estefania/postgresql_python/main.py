import create_registre as cr
import read_registre as rr
import update_registre as ur
import delete_registre as dr

#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

#Trucada a read_reg
results = rr.read_reg()
for i in results:
    print('\n')
    print('Nom: ' + i[0])
    print('Adreça: ' + i[1])
    print('telèfon: ' + i[2])
    print('email: ' + i[3])
    print('naixement: ' + i[4])

#Trucada de update_reg()
ur.update_reg()

#Trucada al delete_reg()
dr.delete_reg()