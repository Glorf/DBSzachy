#Copyright: Michał Bień 2012

    #This program is free software; you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation; either version 2 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program; if not, write to the Free Software
    #Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import sqlite3
from ruchy import *
from funkcje import *

con=sqlite3.connect(':memory:')
c=con.cursor()
c.execute('''create table pionki(pionek,kolor,pole,zywy)''')
con.commit()
i=8
j=0
while i<16:
    i+=True
    j+=True
    c.execute('''insert into pionki values('pion{1}','bialy',{0},1)'''.format(i,j))
i=48
j=0
while i<56:
    i+=True
    j+=True
    c.execute('''insert into pionki values('pion{1}','czarny',{0},1)'''.format(i,j))
c.execute('''insert into pionki values('krol','bialy',4,1)''')
c.execute('''insert into pionki values('krol','czarny',60,1)''')
c.execute('''insert into pionki values('dama','bialy',5,1)''')
c.execute('''insert into pionki values('dama','czarny',61,1)''')
c.execute('''insert into pionki values('wieza1','bialy',1,1)''')
c.execute('''insert into pionki values('wieza2','bialy',8,1)''')
c.execute('''insert into pionki values('wieza1','czarny',57,1)''')
c.execute('''insert into pionki values('wieza2','czarny',64,1)''')
c.execute('''insert into pionki values('kon1','bialy',2,1)''')
c.execute('''insert into pionki values('kon2','bialy',7,1)''')
c.execute('''insert into pionki values('kon1','czarny',58,1)''')
c.execute('''insert into pionki values('kon2','czarny',63,1)''')
c.execute('''insert into pionki values('goniec1','bialy',3,1)''')
c.execute('''insert into pionki values('goniec2','bialy',6,1)''')
c.execute('''insert into pionki values('goniec1','czarny',59,1)''')
c.execute('''insert into pionki values('goniec2','czarny',62,1)''')
con.commit()
print("Witamy w szachach!")
stat=1
while True:
    if stat==1:
        kgr="bialy"
    elif stat==2:
        kgr="czarny"
    szachowrysuj(c)
    if kgr=="bialy":
        zkolor="czarny"
    if kgr=="czarny":
        zkolor="bialy"
    sprawdzszach(zkolor,c,kgr) #Odwrócone
    print("Ruch",kgr[:-1]+"ego!")
    pion=input("Którego pionka chcesz przemiescic?: ")
    c.execute('''select pole from pionki where (pionek="{0}" and kolor="{1}")'''.format(pion,kgr))
    pole=c.fetchone()[0]
    print(pole)
    if pion!="krol" and pion!="dama":
        npionka=pion[:-1]
    else:
        npionka=pion
    npole=input("Wybierz pole na które chcesz go przemieścić: ")
    out=sprawdzpole(pole,npole,npionka,kgr,c,zkolor)
    if out==1:
        print("Ruch wykonany!")
        c.execute('''insert into pionki values('{0}','{1}',{2},1)'''.format(pion,kgr,npole))
        c.execute('''delete from pionki where (pionek='{0}' and pole={1})'''.format(pion,pole))
        con.commit()
    elif out==2:
        c.execute('''select pionek from pionki where pole={0}'''.format(npole))
        zabity=c.fetchone()[0]
        c.execute('''delete from pionki where (pionek='{0}' and pole={1})'''.format(zabity,npole))
        c.execute('''delete from pionki where (pionek='{0}' and pole={1})'''.format(pion,pole))
        c.execute('''insert into pionki values('{0}','{1}',{2},1)'''.format(pion,kgr,npole))
        print("Zabiles pionka",zabity)
    elif out==0:
        print("Nie można wykonać takiego ruchu!")
    else:
        print(out)
    #if stat==1:
        #stat=2
    #elif stat==2:
        #stat=1
