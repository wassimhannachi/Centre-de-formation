import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("create database if not exists salle")

def connection():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="applicationpython")
    return(mydb)
db=connection()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Salle(id_salle INT PRIMARY KEY, capacité int, nom_salle VARCHAR(255))")
mycursor.execute("SHOW TABLES")

class Salle:
    db=connection()
    mycursor=db.cursor()
    def __init__(self,id_salle=0,capacité=0,nom_salle=""):
        self.id_salle=id_salle
        self.capacité=capacité
        self.nom_salle=nom_salle
       
        
    def ajouterSalle(self):
       sql="INSERT INTO salle (id_salle,capacité,nom_salle) VALUES (%s, %s, %s)"
       val = (self.id_salle,self.capacité,self.nom_salle)
       self.mycursor.execute(sql, val)
       self.db.commit()
       print(self.mycursor.rowcount, "Ajout avec succés.")
       
    def affichersalle(self):
        self.mycursor.execute("SELECT * FROM salle")
        result = self.mycursor.fetchall()
        return result
            
    def supprimersalle(self,id_salle):
        sql = "DELETE FROM salle WHERE id_salle = %s"
        val = (id_salle,)
        self.mycursor.execute(sql, val)
        self.db.commit()
        
    def modifiersalle(self,other):
        sql="UPDATE salle SET  id_salle =%s, capacité =%s,nom_salle=%s WHERE id_salle=%s"
        val=(self.id_salle,self.capacité,self.nom_salle,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"Salle bien modifié")
            
    def chercher(self):
        P=Salle(self.id_salle.get(),self.capacité.get())

        P.chercher(self.id_salle.get())
        print("salle a été bien trouvé! ")



#a = Salle(22422,2,"BI")
#a.ajouterSalle()
#a.affichersalle()
#print("avant suppression.....")
#a.affichersalle()
#a.supprimerSalle(2)
#print("après suppression.....")
#a.afficherSalle()
#a.modifierSalle(242)
#a.afficherSalle()
