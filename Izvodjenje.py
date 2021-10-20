"""
@author: DajanaJandric
"""
import cx_Oracle
import pandas

#  konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns) 
mycursor=db.cursor()  



# pronalazenje izvodjenja na osnovu ID-a termina koji je unijet
def pronadjiIzvodjenje(termin_id):
    mycursor.execute('select izv_id, Sala_sala_id, Predstava_predstava_id from TEATAR_Izvodjenje where Termin_termin_id=:termin_id',[termin_id])
    db.commit()
    rez=mycursor.fetchall()
    for x in rez:
        if x==rez[0]:
            return x
    print("Ne postoji predstava sa nazivom koji ste unijeli.")
    return -1


# prikaz podataka o izvodjenju na osnovu ID-a termina koji je unijet
def prikazIzvodjenja(termin_id):
    i=pronadjiIzvodjenje(termin_id)
    if i!=-1:
        mycursor.execute('select izv_id, Sala_sala_id, Predstava_predstava_id from TEATAR_Izvodjenje where Termin_termin_id=:termin_id',[termin_id])
        db.commit()
        rez=mycursor.fetchall()
        for x in rez:
            print(x)
        
       
# dodavanje novog izvodjenja predstave
def dodajIzvodjenje(izv_id, sala_id, termin_id, predstava_id):
    sql=('insert into TEATAR_Izvodjenje(izv_id, Sala_sala_id, Termin_termin_id, Predstava_predstava_id)'
         'values (:izv_id, :sala_id, :termin_id, :predstava_id)'
        )
    try:
        mycursor.execute(sql, [izv_id, sala_id, termin_id, predstava_id])
        db.commit()
    except cx_Oracle.Error as error:
        print('Greska!')
        print(error)
  
      
# prikaz svih izvodjenja  
def pregledIzvodjenja():
    cursor=pandas.read_sql('select izv_id from TEATAR_Izvodjenje', db)
    print(cursor)

