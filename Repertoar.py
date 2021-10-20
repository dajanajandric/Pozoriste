"""
@author: DajanaJandric
"""
import cx_Oracle
import pandas

# konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns) 
mycursor=db.cursor()  



# kreiranje novog repertoara na osnovu unijetog ID-a i naziva
# ID je kombinacija rednog broja mjeseca i godine razdvojenih "-"
def kreirajRepertoar(rep_id, rep_naziv):
    sql=('insert into TEATAR_Repertoar(rep_id, repertoar_naziv)'
         'values (:rep_id, :rep_naziv)' 
        )
    try:
        mycursor.execute(sql, [rep_id, rep_naziv])
        db.commit()
    except cx_Oracle.Error as error:
        print('Greska!')
        print(error)
        

# dodavanje izvodjenja u repertoar
def dodajRI(rep_id, izv_id):
    sql=('insert into TEATAR_IzvodiSe(Repertoar_rep_id, Izvodjenje_izv_id)'
         'values (:rep_id, :rizv_id)' 
        )
    try:
        mycursor.execute(sql, [rep_id, izv_id])
        db.commit()
    except cx_Oracle.Error as error:
        print('Greska!')
        print(error)


# prikazivanje repertoara i dodatih izvodjenja        
def repertoarIzvodjenje():
    cursor=pandas.read_sql('select * from TEATAR_IzvodiSe', db)
    print(cursor)


# prikazivanje repertoara
def prikazRepertoara():
    cursor=pandas.read_sql('select * from TEATAR_Repertoar', db)
    print(cursor)