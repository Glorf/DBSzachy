def lista(c,wartosc):
    i=0
    lista=list()
    while i<64:
        i+=True
        lista.append('   x   ')
    j=0
    while j<64:
        j+=True
        c.execute('''select {0} from pionki where pole={1}'''.format(wartosc,j))
        proc=c.fetchone()
        if proc!=None:
            lista[j-1]=proc[0]
    return lista
def szachowrysuj(c):
    plista=lista(c,"pionek")
    klista=lista(c,"kolor")
    i=64
    j=64
    while i>6:
        i-=8
        print("|"+klista[i].ljust(7)+"|"+klista[i+1].ljust(7)+"|"+klista[i+2].ljust(7)+"|"+klista[i+3].ljust(7)+"|"+klista[i+4].ljust(7)+
              "|"+klista[i+5].ljust(7)+"|"+klista[i+6].ljust(7)+"|"+klista[i+7].ljust(7)+"|")
        print("|"+plista[i].ljust(7)+"|"+plista[i+1].ljust(7)+"|"+plista[i+2].ljust(7)+"|"+plista[i+3].ljust(7)+"|"+plista[i+4].ljust(7)+
              "|"+plista[i+5].ljust(7)+"|"+plista[i+6].ljust(7)+"|"+plista[i+7].ljust(7)+"|")
        print("|  "+str(j-7).ljust(2)+"   |  "+str(j-6).ljust(2)+"   |  "+str(j-5).ljust(2)+"   |  "+str(j-4).ljust(2)+"   |  "+str(j-3).ljust(2)+
              "   |  "+str(j-2).ljust(2)+"   |  "+str(j-1).ljust(2)+"   |  "+str(j).ljust(2)+"   |")
        j-=8
def sprawdzpole(pole,npole,pion,kolor,c,zkolor):
    k=[1,2,3,4,5,6,7,8]
    l=[-1,-2,-3,-4,-5,-6,-7,-8]
    z=[7,9]
    c.execute('''select kolor from pionki where pole={0}'''.format(npole))
    kol=c.fetchone()
    print(pole,npole,pion,kolor)
    odjem=int(npole)-int(pole)
    print(odjem)
    if kol!=None:
        kol=kol[0]
    if pion=="pion":
        if kolor=="czarny":
            dnpole=pole
            dpole=npole
        elif kolor=="bialy":
            dnpole=npole
            dpole=pole
        if kol==None and int(dnpole)-8==int(dpole):
            return 1
        elif kol==zkolor and (int(dnpole)-7==int(dpole) or int(dnpole)-9==int(dpole)):
            return 2
        else:
            return 0
    elif pion=="wieza":
        print("wieza")
        w=rwiezy(odjem,pole,npole,c,zkolor,k,l)
        if w==1:
            return 1
        elif w==2:
            return 2
        elif w==0:
            return 0
    elif pion=="kon":
        if int(odjem) in [17,15,10,6,-6,-10,-15,-17]:
            if kol==zkolor:
                return 2
            elif kol==None:
                return 1
            else:
                return 0
        else:
            return 0
    elif pion=="goniec":
        g=rgonca(odjem,pole,npole,c,zkolor,k,l,z,kol)
        if g==1:
            return 1
        elif g==2:
            return 2
        elif g==0:
            return 0
    elif pion=="dama":
        w=rwiezy(odjem,pole,npole,c,zkolor,k,l)
        g=rgonca(odjem,pole,npole,c,zkolor,k,l,z,kol)
        for x in [w,g]:
            if x==0:
                return 0
            elif x==1:
                return 1
            elif x==2:
                return 2
    elif pion=="krol":
        if int(odjem) in [9,8,7,1,-9,-8,-7,-1]:
            if kol==zkolor:
                return 2
            elif kol==None:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        print("Kild")
        return 0
def sprawdzszach(kolor,c,zkolor):
    k=[1,2,3,4,5,6,7,8]
    pola=list()
    i=0
    while i<64:
        i+=1
        pola.append('x')
    i=0
    while i<=64:
        i+=1
        c.execute('''select pionek from pionki where pole={0}'''.format(i))
        cpn=c.fetchone()
        h=i-1
        if cpn==None:
            continue
        elif cpn!=None:
            pn=cpn[0]
            c.execute('''select kolor from pionki where pole={0}'''.format(i))
            ckr=c.fetchone()
            kr=ckr[0]
            if kr==zkolor:
                if pn[:-1]=="pion":
                    if kr=="bialy":
                        if (i-1)/8 in k:
                            s=[9]
                        elif i/8 in k:
                            s=[7]
                        else:
                            s=[7,9]
                    if kr=="czarny":
                        if (i-1)/8 in k:
                            s=[-7]
                        elif i/8 in k:
                            s=[-9]
                        else:
                            s=[-7,-9]
                    for l in s:
                        try:
                            pola[h+l]="v"
                        except Exception:
                            continue
                elif pn[:-1]=="wieza":
                    f=int(h/8)
                    mnp=7-f
                    mnm=f
                    ia=0
                    while (i+ia)/8 not in k:
                        ia+=1
                        #print(i+ia)
                    pnp=ia
                    ia=0
                    while (i-ia)/8 not in k:
                        if (i-ia)/8==0:
                            ia=1
                            break
                        ia+=1
                        #print(i-ia)
                    pnl=ia-1
                    if mnp>0:
                        j=0
                        while j<mnp:
                            j+=1
                            c.execute('''select pionek from pionki where pole={0}'''.format(i+j*8))
                            if c.fetchone()==None:
                                pola[h+j*8]="v"
                            else:
                                break
                    if mnm>0:
                        j=0
                        while j<mnm:
                            j+=1
                            c.execute('''select pionek from pionki where pole={0}'''.format(i-j*8))
                            if c.fetchone()==None:
                                pola[h-j*8]="v"
                            else:
                                break
                    if pnp>0:
                        j=0
                        while j<pnp:
                            j+=1
                            c.execute('''select pionek from pionki where pole={0}'''.format(i+j))
                            if c.fetchone()==None:
                                pola[h+j]="v"
                            else:
                                break
                    if pnl>0:
                        j=0
                        while j<pnl:
                            i+=1
                            c.execute('''select pionek from pionki where pole={0}'''.format(i-j))
                            if c.fetchone()==None:
                                pola[h-j]="v"
                            else:
                                break
                elif pn[:-1]=="goniec":
                    f=int(h/8)
                    mnp=7-f
                    mnm=f
                    s=[7,9]
                    if mnp>0:
                        for l in s:
                            j=0
                            while j<mnp:
                                j+=1
                                c.execute('''select pionek from pionki where pole={0}'''.format(i+j*l))
                                cr=c.fetchone()
                                if cr!=None:
                                    break
                                else:
                                    pola[h+j*l]="v"
                                    if (i+j*l)/8 in k or ((i+j*l)-1)/8 in k:
                                        break
                    if mnm>0:
                        for l in s:
                            j=0
                            while j<mnm:
                                j+=1
                                c.execute('''select pionek from pionki where pole={0}'''.format(i-j*l))
                                cr=c.fetchone()
                                if cr!=None:
                                    break
                                else:
                                    pola[h-j*l]="v"
                                    if (i-j*l)/8 in k or ((i-j*l)-1)/8 in k:
                                        break
    num=56
    while num>=0:
        print(pola[num]+pola[1+num]+pola[2+num]+pola[3+num]+pola[4+num]+pola[5+num]+pola[6+num]+pola[7+num])
        num-=8
