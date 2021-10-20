# -*- coding: utf-8 -*-
"""
@author: DajanaJandric
"""

import Radnik
import Gledalac
import Izvodjenje
import Predstava
import Repertoar
import Ulaznica
import os
from pip._vendor.distlib.compat import raw_input


while True:
    korisnickoIme=raw_input('Unesite usename: ')
    lozinka=raw_input('Unesite password: ') 
    if Radnik.login(korisnickoIme, lozinka):
        break
    else:
        print('Pogresan unos.')            
komanda=-1
while komanda!=0:
    print('Izaberite opciju')
    print( '  1 - pregled imena i prezimena gledalaca')
    print( '  2 - dodavanje novog gledaoca')
    print( '  3 - izdvajanje brojeva telefona gledalaca')
    print( '  4 - prikaz gledalaca u abecednom redoslijedu')
    print( '  5 - brisanje gledaoca')
    print( '  6 - prikaz podataka o predstavi')
    print( '  7 - prikaz podataka o izvodjenju predstave u datom terminu')
    print( ' 8 - dodavanje novog izvodjenja u repertoar')
    print( ' 9 - kreiranje novog repertoara')
    print( ' 10 - prikaz ulaznica za dato izvodjenje')
    print( ' 11 - kupovina ulaznice')
    print( ' 12 - pregled id-a radnika sa datim username-om')
    print( '  0 - izlaz iz programa')
    komanda=int(input('Izaberite jednu od postojecih opcija: '))
    if komanda==1:
        print('Imena i prezimena gledalaca: ')
        print (Gledalac.pregledGledalaca())
    elif komanda==2:
        print("Dodavanje novog gledaoca u bazu\n")
        while True:
            jmbg=input('Unesite jmbg gledaoca:')
            if len(str(jmbg))!=13:
                print('JMBG sadrzi tacno 13 cifara!')
            else:
                break 
        Ime=input('Unesite ime gledaoca: ')
        Prezime=input('Unesite prezime gledaoca: ')
        BrTelefona=input('Unesite broj telefona gledaoca:')
        Email=input('Unesite email adresu gledacoa:')
        radnik_id=input('Unesite svoj ID: ')
        Gledalac.dodajGledaoca(jmbg, Ime, Prezime, BrTelefona, Email, radnik_id)
        print(Gledalac.pregledGledalaca())
    elif komanda==3:
        print("Brojevi telefona gledalaca su: ")
        print(Gledalac.izdvojBrojeveTelefona())
    elif komanda==4:
        print("Spisak gledalaca po abecednom redoslijedu: ")
        print(Gledalac.poredjajPoImenu())
    elif komanda==5:
        jmbg=input("Unesi jmbg gledaoca kog zelite da obrisete: ")
        Gledalac.obrisiGledaoca(jmbg)
        print(Gledalac.pregledGledalaca())
    elif komanda==6:
        naziv=input("Unesite naziv predstave: ")
        print(Predstava.prikazPredstave(naziv))
    elif komanda==7:
        termin=input("Unesite zeljeni termin: ")
        print(Izvodjenje.prikazIzvodjenja(termin))
    elif komanda==8:
        izvodjenje=input("Unesite id izvodjenja: ")
        sala=input("Unesite id sale: ")
        termin=input("Unesite id termina: ")
        predstava=input("Unesite id predstave: ")
        Izvodjenje.dodajIzvodjenje(izvodjenje, sala, termin, predstava)
        print(Izvodjenje.pregledIzvodjenja())
    elif komanda==9:
        rid=input("Unesite id novog reperotara: ")
        naziv=input("Unesite naziv repertoara: ")
        Repertoar.kreirajRepertoar(rid, naziv)
        izvodjenje=input("Unesite id izvodjenja: ")
        sala=input("Unesite id sale: ")
        termin=input("Unesite id termina: ")
        predstava=input("Unesite id predstave: ")
        Izvodjenje.dodajIzvodjenje(izvodjenje, sala, termin, predstava)
        Repertoar.dodajRI(rid, izvodjenje)
        print(Repertoar.repertoarIzvodjenje())
    elif komanda==10:
        izvodjenje=input("Unesite zeljeno izvodjenje: ")
        print(Ulaznica.ulaznicaIzvodjenje(izvodjenje))
    elif komanda==11:
        print("Moguce je kupiti ulaznicu za sledeca izvodjenja: ")
        Izvodjenje.pregledIzvodjenja()
        izvodjenje_id=input("Unesite id izvodjenja: ")
        radnik_id=input("Unesite id radnika: ")
        gledalac_jmbg=input("Unesite jmbg gledaoca: ")
        while True:
            if Gledalac.pronadji(gledalac_jmbg):
                break
            else:
                print("Gledalac nije u bazi. Molim Vas dodajte gledaoca.")
                while True:
                    if len(str(gledalac_jmbg))!=13:
                        print('JMBG sadrzi tacno 13 cifri!')
                    else:
                        break 
                Ime=input('Unesite ime gledaoca: ')
                Prezime=input('Unesite prezime gledaoca: ')
                BrTelefona=input('Unesite broj telefona gledaoca:')
                Email=input('Unesite email adresu gledacoa:')
                Gledalac.dodajGledaoca(gledalac_jmbg, Ime, Prezime, BrTelefona, Email, radnik_id)
                break
        while True:
            mjesto=input("Unesite broj mjesta u sali: ")
            if Ulaznica.pronadjiZauzeta(izvodjenje_id, mjesto):
                print("Mjesto koje ste unjeli je zauzeto.")
            else:
                break
        while True:
            ulaznica_id=input("Unesite id ulaznice: ")
            if Ulaznica.pronadji(ulaznica_id):
                print("Ulaznica je vec prodata.")
            else:
                break
        ulaznica_cijena=input("Unesite cijenu ulaznice: ")
        Ulaznica.kupi(ulaznica_id, ulaznica_cijena, izvodjenje_id, radnik_id, gledalac_jmbg, mjesto)
        print("Uspjesno ste izvrsili kupovinu ulaznice.")
        print(Ulaznica.pregledUlaznica())
    elif komanda==12:
        rUsername=input("Unesite username radnika: ")
        print(Radnik.getId(rUsername))
    elif komanda==0:
        os.system('cls')
        