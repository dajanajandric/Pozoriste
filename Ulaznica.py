"""
@author: DajanaJandric
"""
import cx_Oracle
import pandas

#konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns)
mycursor = db.cursor()



# prikaz ulaznica za dato izvodjenje
def ulaznicaIzvodjenje(izv_id):
    try:
        mycursor.execute('select ulaznica_id from TEATAR_Ulaznica WHERE Izvodjenje_izv_id=:izv_id', [izv_id])
        row=mycursor.fetchall()
        if(row):
            for row in row:
                print(row)
        else:
            print("Nema ulaznica za dato izvodjenje.")
    finally:
        db.close()


# kupovina ulaznice
def kupi(ulaznicaID, ulaznicaCijena, izvodjenjeID, radnikID, gledalacJMBG, brMjesta):
    sql=('insert into TEATAR_Ulaznica(ulaznica_id, ulaznica_cijena, Izvodjenje_izv_id, Radnik_radnik_id, Gledalac_gledalac_jmbg, brojMjestaUsali)'
         'values(:ulaznicaID, :ulaznicaCijena, :izvodjenjeID, :radnikID, :gledalacJMBG, :brMjesta)'
        )
    try:
        mycursor.execute(sql, [ulaznicaID, ulaznicaCijena, izvodjenjeID, radnikID, gledalacJMBG, brMjesta])
        db.commit()
    except cx_Oracle.Error as error:
        print('Greska!')
        print(error)
  
        
# pregled svih ulaznica  
def pregledUlaznica():
    mycursor=pandas.read_sql('select ulaznica_id from TEATAR_Ulaznica', db)
    print(mycursor)
        

# pronalazenje zauzetih mjesta u sali za dato izvodjenje
def pronadjiZauzeta(izv_id):
    mycursor.execute('select brojMjestaUsali from TEATAR_Ulaznica where Izvodjenje_izv_id=:izv_id')
    db.commit()
    rez=mycursor.fetchall()
    for x in rez:
        if x==rez[0]:
            return x
    return -1
    

# prikaz zauzetih mjesta u sali za dato izvodjenje
def prikaziZauzeta(izv_id):
    z=pronadjiZauzeta(izv_id)
    if z!=-1:
        mycursor.execute('select brojMjestaUsali from TEATAR_Ulaznica where Izvodjenje_izv_id=:izv_id', [izv_id])
        db.commit()
        rez=mycursor.fetchall()
        for x in rez:
            print(x)



    	
