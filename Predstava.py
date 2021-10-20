"""
@author: DajanaJandric
"""
import cx_Oracle

# konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns) 
mycursor=db.cursor()  



# pronalazenje predstave u bazi na osnovu naziva
def pronadjiPredstavu(predstava_naziv):
    mycursor.execute('select * from TEATAR_Predstava where predstava_naziv=:predstava_naziv', [predstava_naziv])
    db.commit()
    rez=mycursor.fetchall()
    for x in rez:
        if x==rez[0]:
            return x
    print("Ne postoji predstava sa nazivom koji ste unijeli.")
    return -1


# prikaz podataka o predstavi na osnovu naziva koji je unijet
def prikazPredstave(predstava_naziv):
    p=pronadjiPredstavu(predstava_naziv)
    if p!=-1:
        mycursor.execute('select predstava_id, predstava_autorTeksta, predstava_naziv, Scenograf_scenograf_id, Reziser_reziser_id from TEATAR_Predstava where predstava_naziv=:predstava_naziv',[predstava_naziv])
        db.commit()
        rez=mycursor.fetchone()
        for x in rez:
            print(x)






