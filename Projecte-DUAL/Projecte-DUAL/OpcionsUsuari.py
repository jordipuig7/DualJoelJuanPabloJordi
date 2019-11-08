import Connector;
import os;

# -------------------------- CREACIO DE L'USUARI A LA BADE DE DADES -------------------------------

def crearUsuari(mycursor):
    print("CREACIó D'USUARI      E --> Exit")
    print("================================")
    usuari = (input("Usuari: "))
    if (usuari != "E"):
        contra = (input("Contrasenya: "))
        if (contra != "E"):
            contre = (input("Repeteix Contrasenya: "))
            if (contre != "E"):
                if(usuari == "E" or contra == "E" or contre == "E"):
                    os.system('cls')
                elif(contra == contre):
                    mycursor.execute("insert into users values(\"" + usuari + "\" ,\"" + contra + "\", 0);")
                    Connector.dbConnection.commit()
                    mycursor.execute("select numero from repte")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        mycursor.execute("select id from preguntes where numero_repte = " + str(x[0]))
                        myresult = mycursor.fetchall()
                        for m in myresult:
                            mycursor.execute("insert into users_repte values(\"" + usuari + "\", " + str(x[0]) + ", " + str(m[0]) + ", 0);" );
                            Connector.dbConnection.commit()
                else:
                    os.system('cls')
                    print("Ha hagut algun error")
            else:
                os.system('cls')
        else:
            os.system('cls')
    else:
        os.system('cls')

# -------------------------- ELIMINAR USUARI -------------------------------


def eliminarusuari(mycursor):
    print("     ELIMINAR USUARI")
    print("===========================")
    usuari = (input("Usuari: "))
    mycursor.execute("select usuari from users where usuari = \"" + usuari + "\";")
    myresult = mycursor.fetchall()
    x = myresult
    try:
        if ( str(x[0][0]) == usuari):
            print("Usuari Correcte")
            contras = (input("Contrasenya: "))
            mycursor.execute("select contrasenya from users where contrasenya = \"" + contras + "\";")
            myresult = mycursor.fetchall()
            x = myresult
            if ( str(x[0][0]) == contras):
                matar = (input("Estas segur? s/n: "))
                if (matar == "s"):
                    mycursor.execute("Delete from users_repte where users_usuari=\"" + usuari + "\";")
                    mycursor.execute("Delete from users where usuari=\"" + usuari + "\" AND contrasenya=\"" + contras + "\";")
                    Connector.dbConnection.commit()
                    print("Usuari Eliminat")
    except IndexError:
        print("ERROR")