import Connector;
import os;

# -------------------------- CREACIO DE L'USUARI A LA BADE DE DADES -------------------------------

def crearUsuari(mycursor):
    print("CREACIó D'USUARI      E --> Exit")
    print("================================")
    usuari = (input("Usuari: "))
    mycursor.execute("SELECT * FROM users where usuari = \"" + usuari + "\"")
    usuaris1 = mycursor.fetchall()
    if not usuaris1:
        if (usuari.casefold() != "E".casefold()):
            contra = (input("Contrasenya: "))
            if (contra.casefold() != "E".casefold()):
                contre = (input("Repeteix Contrasenya: "))
                if (contre.casefold() != "E".casefold()):
                    if(usuari.casefold() == "E".casefold() or contra.casefold() == "E".casefold() or contre.casefold() == "E".casefold()):
                        os.system('cls')
                    elif(contra == contre):
                        mycursor.execute("insert into users values(\"" + usuari + "\" ,\"" + contra + "\", 0, default);")
                        Connector.dbConnection.commit()
                        os.system('cls')
                        print("USUARI CREAT AMB EXIT")
                    else:
                        os.system('cls')
                        print("Hi ha hagut algun error\n")
                else:
                    os.system('cls')
            else:
                os.system('cls')
        else:
            os.system('cls')
    else: 
        os.system('cls')
        print("Aquest nom d'usuari ja existeix\n")
    

  #  def comprovarusuari(mysursor):
        
  #     mycursor.execute("SELECT * FROM users")
   #     usuaris = mycursor.fetchall()
    #    for usuari in usuaris:
     #       print("usuari repetit")
      #      check = true



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
            mycursor.execute("select contrasenya from users where contrasenya = \"" + contras + "\" AND usuari = \"" + usuari + "\";")
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