import Connector;
import os;

# -------------------------- INICI DE SESSIÓ -------------------------------

def iniciarsessio(mycursor):
    print("     Iniciar sessió")
    print("===========================")
    usuari = (input("Usuari: "))
    mycursor = Connector.dbConnection.cursor()
    mycursor.execute("select usuari from users where usuari = \"" + usuari + "\";")
    myresult = mycursor.fetchall()
    try:
        if (str(myresult[0][0]) == usuari):
            print("Usuari Correcte")
            contras = input("Contrasenya: ")
            mycursor.execute("select contrasenya from users where contrasenya = \"" + contras + "\";")
            myresult = mycursor.fetchall()
            x = myresult
            if (str(x[0][0]) == contras ):
                os.system('cls')
                print("Hola " + usuari)
                Menu3(usuari, contras, mycursor);
    except IndexError:
        print("Usuari o Contrasenya son incorrectes")

# -------------------------- MENU INICI DE SESSIÓ -------------------------------

def Menu3(usuari, contras, mycursor):
    entrada = True
    while (entrada):
        punttotal = 0
        print("     MENU")
        print("===============")
        mycursor.execute("select numero from repte")
        myresult = mycursor.fetchall()
        for x in myresult:
            porfavor = Connector.dbConnection.cursor()
            porfavor.execute("select fet from users_repte where users_usuari =\"" + usuari + "\" AND num_repte = " + str(x[0]) + " group by fet order by fet")
            sipo = porfavor.fetchall()
            for y in sipo:
                if (str(y[0]) == "0"):
                    print(str(x[0]) + "--> Repte " + str(x[0]))
        print("R--> Ranking")
        print("T --> Tancar Sessió")
        opcio2 = (input("OPCIO -->"))
        cont = 0 
        mycursor.execute("select numero from repte")
        myresult = mycursor.fetchall()
        for x in myresult:
            if opcio2 == str(x[0]):
                mycursor.execute("select enunciat, id, resposta, puntuacio from preguntes where numero_repte = " + opcio2)
                resolt = mycursor.fetchall()
                resp = ""
                for a in resolt:
                    puntuacio = a[3]
                    while resp != str(a[2]):
                        resp = input(str(a[0]))
                        print("E - Exit")
                        if resp == str(a[2]):
                            print("ENCERT")
                            punttotal = punttotal + puntuacio
                            print(punttotal)
                        elif resp == "E":
                            Menu3(usuari, contras)
                        else:
                            print("FALLAT")
            elif(opcio2 == "T"):
                usuari = ""
                contras = ""
                os.system('cls')
                entrada = False;
        sql = "update users set puntuacio = puntuacio + %s where usuari = %s AND contrasenya = %s"
        val = punttotal, usuari, contras
        mycursor.execute(sql, val)
        Connector.dbConnection.commit()

            #sql = "update users set puntuacio = puntuacio + %s where usuari = %s AND contrasenya = %s"
    #val = punttotal, usuari, contras
    # mycursor.execute(sql, val)
   # Connector.dbConnection.commit()