def rwiezy(odjem,pole,npole,c,zkolor,k,l):
    if int(odjem)/8 in k:
        print("prosto")
        i=0
        p=0
        il=int(odjem)/8
        while i<il:
            i+=1
            c.execute('''select kolor from pionki where pole={0}'''.format(int(pole)+i*8))
            g=c.fetchone()
            print(g)
            if g==None:
                p=1
            elif g!=None:
                if i*8==odjem and g[0]==zkolor:
                    return 2
                else:
                    return 0
        if p==1:
            return 1
    if odjem/8 in l:
        print("tyl")
        p=0
        il=odjem/8
        i=il
        while i<0:
            c.execute('''select kolor from pionki where pole={0}'''.format(int(pole)+(i*8)))
            g=c.fetchone()
            print(g)
            if g==None:
                p=1
                i+=1
            elif g!=None:
                if i*8==-odjem and g[0]==zkolor:
                    return 2
                else:
                    return 0
        if p==1:
            return 1
    if (odjem/8 not in k) and (odjem/8 not in l):
        if odjem<8 and odjem>0:
            j=0
            p=0
            if int(pole)/8 in k:
                    return 0
            while j<odjem:
                j+=1
                c.execute('''select kolor from pionki where pole={0}'''.format(int(pole)+j))
                kl=c.fetchone()
                if ((int(pole)+j)/8 in k) and int(pole)+j!=int(npole):
                    return 0
                if kl==None:
                    p=1
                if kl!=None:
                    if int(pole)+j==int(npole) and kl[0]==zkolor:
                        return 2
                    else:
                        return 0
            if p==1:
                return 1
        elif odjem>-8 and odjem<0:
            j=0
            p=0
            if (int(pole)-1)/8 in k:
                return 0
            while j>odjem:
                j-=1
                c.execute('''select kolor from pionki where pole={0}'''.format(int(pole)+j))
                kl=c.fetchone()
                if ((int(pole)+j-1)/8 in k) and int(pole)+j!=int(npole):
                    return 0
                if kl==None:
                    p=1
                if kl!=None:
                    if int(pole)+j==int(npole) and kl[0]==zkolor:
                        return 2
                    else:
                        return 0
                if p==1:
                    return 1
def rgonca(odjem,pole,npole,c,zkolor,k,l,z,kol):
    for x in z:
        if odjem/x in k:
            ln=odjem/x
            p=0
            i=0
            if int(pole)/8 in k:
                return 0
            while ln>i:
                i+=1
                if ((int(pole)+i)/8 in k) and int(pole)+i!=int(npole):
                    return 0
                pl=pole+i*x
                c.execute('''select kolor from pionki where pole={0}'''.format(pl))
                o=c.fetchone()
                if o!=None:
                    if o[0]==zkolor and pl==int(npole):
                        return 2
                    else:
                        return 0
                else:
                    p=1
            if kol==None and p==1:
                return 1
        elif odjem/x in l:
            ln=odjem/x
            p=0
            i=0
            if (int(pole)-1)/8 in k:
                return 0
            while ln<i:
                i-=1
                if ((int(pole)+i-1)/8 in k) and int(pole)+i!=int(npole):
                    return 0
                pl=pole+i*x
                c.execute('''select kolor from pionki where pole={0}'''.format(pl))
                o=c.fetchone()
                if o!=None:
                    if o[0]==zkolor and int(npole)==pl:
                        return 2
                    else:
                        return 0
                else:
                    p=1
            if kol==None and p==1:
                return 1
