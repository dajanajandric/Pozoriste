"""
@author: DajanaJandric
"""

import cx_Oracle
import pandas

# konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns) 
mycursor=db.cursor()   


 
# dodavanje novog gledaoca u bazu podataka            
def dodajGledaoca(gledalac_jmbg, gledalac_ime, gledalac_prezime, gledalac_brTelefona, gledalac_email, radnik_id):
    sql=('insert into TEATAR_Gledalac(gledalac_jmbg, gledalac_ime, gledalac_prezime, gledalac_brTelefona, gledalac_email, Radnik_radnik_id)'
         'values (:gledalac_jmbg, :gledalac_ime, :gledalac_prezime, :gledalac_brTelefona, :gledalac_email, :radnik_id)')
    try:
        mycursor.execute(sql, [gledalac_jmbg, gledalac_ime, gledalac_prezime, gledalac_brTelefona, gledalac_email, radnik_id])
        db.commit()
    except cx_Oracle.Error as error:
        print(error)


# pregled imena i prezimena svih gledalaca iz baze
def pregledGledalaca():
    cursor=pandas.read_sql('select gledalac_ime, gledalac_prezime from TEATAR_Gledalac', db)
    print(cursor)


# pregled brojeva telefona gledalaca
def izdvojBrojeveTelefona():
    sql=('select gledalac_brTelefona from TEATAR_Gledalac')
    try:
       mycursor.execute(sql)
       rez=mycursor.fetchall()
       for x in rez:
          print(x)
    except cx_Oracle.Error as error:
        print('Greska!')
        print(error)
	

# ispis gledalaca po abecednom redoslijedu u opadajucem poretku na osnovu imena       
def poredjajPoImenu():
    cursor=pandas.read_sql('select * from TEATAR_Gledalac order by gledalac_ime desc', db)
    print(cursor)
	


# pronalazenje gledaoca u bazi na osnovu JMBG-a
def pronadji(gledalac_jmbg):
    mycursor.execute('select * from TEATAR_Gledalac where gledalac_jmbg=:gledalac_jmbg',[gledalac_jmbg])
    db.commit()
    rez=mycursor.fetchall()
    for x in rez:
        if x==rez[0]:
            return x
    return -1


# brisanje iz baze gledaoca sa proslijedjenim JMBG-om
def obrisiGledaoca(gledalac_jmbg):
    gl=pronadji(gledalac_jmbg)
    if gl!=-1:
        mycursor.execute('delete from TEATAR_Gledalac where gledalac_jmbg=:gledalac_jmbg',[gledalac_jmbg])
        mycursor.execute('delete from TEATAR_Ulaznica where Gledalac_gledalac_jmbg=:gledalac_jmbg',[gledalac_jmbg])
        db.commit()
    else:
        print("Ne postoji gledalac sa unesenim jmbg-om.")

   
     
        

	