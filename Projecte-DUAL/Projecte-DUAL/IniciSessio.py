import Connector;
import os;

# -------------------------- INICI DE SESSIÓ -------------------------------

def iniciarsessio(mycursor):
    print("Iniciar sessió       E --> Exit")
    print("================================")
    usuari = (input("Usuari: "))
    if (usuari != "E"):
        mycursor.execute("select usuari from users where usuari = \"" + usuari + "\";")
        myresult = mycursor.fetchall()
        try:
            if (str(myresult[0][0]) == usuari):
                print("Usuari Correcte")
                contras = input("Contrasenya: ")
                if (contras != "E"):
                    mycursor.execute("select contrasenya from users where contrasenya = \"" + contras + "\" AND usuari =\"" + usuari + "\"")
                    myresult = mycursor.fetchall()
                    x = myresult
                    if (str(x[0][0]) == contras ):
                        os.system('cls')
                        print("Hola " + usuari)
                        Menu3(usuari, contras, mycursor);
                else:
                    os.system('cls')
        except IndexError:
            print("Usuari o Contrasenya son incorrectes")
    else:
        os.system('cls')

# -------------------------- MENU INICI DE SESSIÓ -------------------------------

def Menu3(usuari, contras, mycursor):
    entrada = True
    while (entrada):
        punttotal = 0
        print("     MENU")
        print("===============")
        print("0 --> Reptes Fets")
        mycursor.execute("select numero from repte")
        myresult = mycursor.fetchall()
        for x in myresult:
            porfavor = Connector.dbConnection.cursor()
            porfavor.execute("select max(id) from preguntes where numero_repte =" + str(x[0]))
            maxid = porfavor.fetchone()
            segundo= Connector.dbConnection.cursor()
            segundo.execute("select users_usuari from users_repte where users_usuari = \"" + usuari + "\" AND num_repte = "+ str(x[0])+" AND id_pregunta = " + str(maxid[0]))
            sip = segundo.fetchone()
            if(sip == None):
                print(str(x[0]) +"--> Repte " + str(x[0]))
                # TANCAR CONEXIONS
        print("I --> Informacio d'usuari")
        print("R--> Ranking")
        print("T --> Tancar Sessió")
        opcio2 = (input("OPCIO -->"))
        cont = 0
        try:
            if(int(opcio2) == int(opcio2)):
                print("ENTRA")
                conector = Connector.dbConnection.cursor()
                conector.execute("select max(id_pregunta) from users_repte where users_usuari = \"" + usuari +"\" and num_repte = " + opcio2 )
                guardar = conector.fetchone()
                conector1 = Connector.dbConnection.cursor()
                conector1.execute("select enunciat, id, resposta, puntuacio from preguntes where numero_repte = " + opcio2 + "and id > " + str(guardar[0]))
                guardar1 = conector1.fetchall()
                for x in guardar1:
                    resp = ""
                    puntuacio = x[3]
                    while resp != str(x[2]):
                        resp = input(str(x[0]))
                        print("E - Exit")
                        if resp == str(x[2]):
                            print("ENCERT")
                            punttotal = punttotal + puntuacio
                            print(punttotal)
                        elif resp == "E":
                            Menu3(usuari, contras)
                        else:
                            print("FALLAT")
        except :
            os.system('cls')
            if(opcio2 == "T"):
                usuari = ""
                contras = ""
                os.system('cls')
                entrada = False;
            elif (opcio2 == "I"):
                os.system('cls')
                infousuari(usuari, contras, mycursor);
        #sql = "update users set puntuacio = puntuacio + %s where usuari = %s AND contrasenya = %s"
        #val = punttotal, usuari, contras
        #mycursor.execute(sql, val)
        #Connector.dbConnection.commit()

# -------------------------- INDORMACIO D'USUARI -------------------------------

def infousuari(usuari, contras, mycursor):
    entrada = True
    print("Informació d'usuari")
    print("===================")
    print("Nickname:  " + usuari)
    print("     Reptes")
    print("===================")
    mycursor.execute("select num_repte, count(fet) as \"LOL""\" from users_repte where fet = 1 AND users_usuari = \""+ usuari + "\"group by num_repte;")
    myresult = mycursor.fetchall()
    for x in myresult:
        mycursor.execute("select count(fet), num_repte from users_repte where users_usuari = \""+ usuari + "\" group by num_repte")
        resolt = mycursor.fetchall()
        for y in resolt:
            if(str(myresult[0][0]) == str(y[1])):
                print("Repte " + str(myresult[0][0]) +" " + str(myresult[0][1])+ "/" + str(y[0]))
    opcio = (input("E for Exit --->"))
    if(opcio != "E"):
        os.system('cls')
        infousuari(usuari, contras, mycursor)
    else:
        os.system('cls')