import os;
import Connector;
import OpcionsUsuari;
import IniciSessio;

# Comença el programa

mycursor = Connector.dbConnection.cursor()
def Principi():
    entrada = True
    while (entrada):
        print("     MENU")
        print("===============")
        print("1--> Crear usuari")
        print("2--> Iniciar Sessio")
        print("3--> Ranking")
        print("4--> Eliminar Usuari")
        print("5--> Sortir")
        opcio = (input("OPCIO --> "))

        if (opcio == "1"):
            os.system('cls')
            OpcionsUsuari.crearUsuari(mycursor)
        elif (opcio == "2"):
            os.system('cls')
            IniciSessio.iniciarsessio(mycursor)
        elif (opcio == "3"):
            os.system('cls')
            ranking()
        elif (opcio == "4"):
            os.system('cls')
            OpcionsUsuari.eliminarusuari(mycursor)
        elif (opcio == "5"):
            print("Adeu!")
            entrada = False
        else:
            os.system('cls')
            print("valor incorrecte")
