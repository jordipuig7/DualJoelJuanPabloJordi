import Connector;
import os;
import Ranking;

# -------------------------- INICI DE SESSIÓ -------------------------------

def iniciarsessio(mycursor):
    print("Iniciar sessió       E --> Exit")
    print("================================")
    usuari = (input("Usuari: "))
    if (usuari.casefold() != "E".casefold()):
        mycursor.execute("select usuari from users where usuari = \"" + usuari + "\";")
        myresult = mycursor.fetchall()
        try:
            if (str(myresult[0][0]) == usuari):
                print("Usuari Correcte")
                contras = input("Contrasenya: ")
                if (contras.casefold() != "E".casefold()):
                    mycursor.execute("select contrasenya from users where contrasenya = \"" + contras + "\" AND usuari =\"" + usuari + "\"")
                    myresult = mycursor.fetchall()
                    x = myresult
                    if (str(x[0][0]) == contras ):
                        os.system('cls')
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
                #.CASEFOLD() Minuscules mayuscules da igual preguntes
                # TANCAR CONEXIONS
        print("I--> Informacio d'usuari")
        print("R--> Ranking")
        print("T--> Tancar Sessió")
        admin = Connector.dbConnection.cursor()
        admin.execute('Select administrador from users where usuari = \"' + usuari + '\"')
        administrador = admin.fetchone()
        if administrador[0] == 1:
            print("C--> Crud de reptes")
        opcio2 = (input("OPCIO -->"))
        cont = 0
        try:
            if(opcio2.isnumeric()):
# CAMBIAR TOT PER MYCURSOR
                conector = Connector.dbConnection.cursor()
                conector.execute("select max(id_pregunta) from users_repte where users_usuari = \"" + usuari +"\" and num_repte = " + opcio2 )
                guardar = conector.fetchone()
                if(guardar[0] != None):
                    conector1 = Connector.dbConnection.cursor()
                    conector1.execute("select enunciat, id, resposta, puntuacio from preguntes where numero_repte = " + str(opcio2) + " and id >" + str(guardar[0]))
                    guardar1 = conector1.fetchall()
                else:
                    conector1 = Connector.dbConnection.cursor()
                    conector1.execute("select enunciat, id, resposta, puntuacio from preguntes where numero_repte = " + str(opcio2))
                    guardar1 = conector1.fetchall()

                for r in guardar1:
                    resp = ""
                    puntuacio = r[3]
                    while resp.casefold() != str(r[2]).casefold():
                        resp = input(str(r[0]))
                        print("E - Exit")
                        if resp.casefold() == str(r[2]).casefold():
                            print("ENCERT")
                            punttotal = punttotal + puntuacio
                            print(punttotal)
                            conector3 = Connector.dbConnection.cursor()
                            conector3.execute("insert into users_repte values('"+ usuari + "' , " + opcio2 + ", "+ str(r[1]) + ");")

                
                        elif resp.casefold() == "E".casefold():
                            Menu3(usuari, contras)
                        else:
                            print("FALLAT")
            elif(opcio2.casefold() == "T".casefold()):
                usuari = ""
                contras = ""
                os.system('cls')
                entrada = False;
            elif (opcio2.casefold() == "I".casefold()):
                os.system('cls')
                infousuari(usuari, contras, mycursor);
            elif (opcio2.casefold() == 'R'.casefold()):
                os.system('cls')
                Ranking.Ranking(mycursor);
            elif(opcio2 == 'C'.casefold() and administrador[0] == 1):
                os.system('cls')
                crudDeReptes(usuari, contras, mycursor);
        except :
            os.system('cls')
        sql = "update users set puntuacio = puntuacio + %s where usuari = %s AND contrasenya = %s"
        val = punttotal, usuari, contras
        mycursor.execute(sql, val)
        Connector.dbConnection.commit()

# -------------------------- INFORMACIO D'USUARI -------------------------------

def infousuari(usuari, contras, mycursor):
    entrada = True
    print("Informació d'usuari")
    print("===================")
    print("Nickname:  " + usuari)
    print("     Reptes")
    print("===================")
    mycursor.execute("select max(id), numero_repte from preguntes group by numero_repte;")
    myresult = mycursor.fetchall()
    for x in myresult:
        nuevo = Connector.dbConnection.cursor()
        nuevo.execute("select max(id_pregunta) from users_repte where num_repte = \""+ str(x[1]) +"\" AND users_usuari = \"" + usuari + "\" ;")
        nuevor = nuevo.fetchone()
        if nuevor[0] == None:
            print("Repte " + str(x[1]) + " 0/" + str(x[0]))
        else:
            print("Repte " + str(x[1]) + " " + str(nuevor[0]) + "/" + str(x[0]))
    nuevo.close;
    opcio = (input("EXIT --> E : "))
    if(opcio.casefold() != "E".casefold()):
        os.system('cls')
        infousuari(usuari, contras, mycursor)
    else:
        os.system('cls')

#---------------------------CRUD DE REPTES---------------------------------------------
def crudDeReptes(usuari, contras, mycursor):
    cont = 1
    print("CRUD DE REPTES")
    print("===================")
    print("1 --> Crear")
    print("2 --> Modificar")
    print("3 --> Eliminar")
    print("4 --> Sortir")
    opcio = input();
    if opcio == "1":
        mycursor.execute('select max(numero) from repte')
        idRepte = mycursor.fetchone();
        id = idRepte[0] + 1
        creadors = input('Qui es el creador/s del repte?')
        preg = input('Quantes preguntes vols inserir?')
        while (int(preg) >= cont):
            pregunta = input('Introdueix la pregunta:\n')
            resposta = input('Introdueix la resposta:\n')
            puntuacio = input('Introduieix la puntuacio:\n')
            mycursor.execute("insert into repte values(" + str(id) + ", \"" + creadors + "\");")
            mycursor.execute("insert into preguntes values(" + str(id) + ", " + str(cont) + ", \"" + pregunta + "\", \"" + resposta + "\", " + puntuacio + ");")
            cont = cont + 1