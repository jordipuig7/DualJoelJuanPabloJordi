import Connector;
import os;
def Ranking(mycursor):
    print("RANKING")
    print("=============================")
    cont = 1
    mycursor.execute("select * from users order by puntuacio DESC")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(str(cont) + "--> " + str(x[0]) + "     " + str(x[2]) + "PUNTS" + "\n")
        cont = cont + 1
    
    opcio = (input("E for Exit --->"))
    if(opcio != "E"):
        os.system('cls')
        Ranking(mycursor)
    else:
        os.system('cls')
