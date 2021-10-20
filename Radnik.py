"""
@author: DajanaJandric
"""
import cx_Oracle

#konekcija sa bazom podataka
dsn_tns = cx_Oracle.makedsn('localhost', '1521')
db=cx_Oracle.connect(user=r'system', password='DJ656', dsn=dsn_tns) 
mycursor=db.cursor()        



#prijava radnika 
def login(radnik_username, radnik_password):
    sql=('select * from TEATAR_Radnik'
         ' where radnik_username=:radnik_username and radnik_password=:radnik_password'
         )
    try:
       mycursor.execute(sql, [radnik_username, radnik_password])
       rez=mycursor.fetchall()
       for x in rez:
           if x==rez[0]:
               return 1
           return 0
    except cx_Oracle.Error as error:
        print('Pogresan unos!')
        print(error)    
        
    
    

#pronalazenje id-a radnika na osnovu username-a
def getId(radnik_username):
    sql = ( 'select radnik_id from TEATAR_Radnik where radnik_username = :radnik_username')
    radnik_id=None
    try:
        mycursor.execute(sql, [radnik_username])
        row=mycursor.fetchone()
        if row:
            radnik_id=row[0]
    except cx_Oracle.Error as error:
        print(error)
    return radnik_id
        




	