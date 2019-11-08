import Connector;

def Ranking():
    print("        RANKING")
    print("========================")
    cont = 1
    mycursor.execute("select * from users order by puntuacio")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(cont + "--> " + str(x[0]))

