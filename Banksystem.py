#Banksystem

mengde_penger = 500

def saldo():
    global mengde_penger
    
    print(mengde_penger)

def rentesats():
    global mengde_penger
    global rente
    if mengde_penger<1000000:
        rente=0.01
    else:
        rente=0.02
    print(rente)
    return rente

a=None
b=None
c=None

def husk_tre_siste(husk_dette):         
    global a
    global b
    global c
    if a==None:
        a=(husk_dette)
        return
    if b==None:
        b=a
        a=(husk_dette)
        return
    if c==None:
        c=b
        b=a
        a=(husk_dette)
        return
    else:
        c=b
        b=a
        a=(husk_dette)
        return


"""def siste_endringer(endring):
    global a, b, c
    c = b
    b = a
    a = endring"""
    
def innskudd(penger_inn):
    global mengde_penger
    if mengde_penger<1000000:
        mengde_penger=mengde_penger+penger_inn
        husk_tre_siste(penger_inn)                      
        if mengde_penger>1000000:
            print('Gratulerer, du får bonusrente!')
    else:
        mengde_penger=mengde_penger+penger_inn
        husk_tre_siste(penger_inn)                       


def uttak(penger_ut):
    global mengde_penger
    if mengde_penger<1000000 and mengde_penger>penger_ut:
        mengde_penger=mengde_penger-penger_ut
        husk_tre_siste(-penger_ut)                     
    if mengde_penger>penger_ut and mengde_penger>1000000:
        mengde_penger=mengde_penger-penger_ut
        husk_tre_siste(-penger_ut)                   
        if mengde_penger<1000000:
            print('Du har nå ordinær rente.')
    if mengde_penger<penger_ut:
        print('Overtrekk.')

def renteoppgjør():
    global mengde_penger
    global rente
    if mengde_penger<1000000:
        mengde_penger=mengde_penger+mengde_penger*0.01
        if mengde_penger>1000000:
            print('Gratulerer, du får bonusrente!')
    else:
        mengde_penger=mengde_penger+mengde_penger*0.02


mengde_penger=500
def velg():
    brukervalg=int(input('--------------------\n1 - Vis saldo\n2 - Innskudd\n3 - Uttak\n4 - Renteoppgjør\n--------------------\nVelg handling: '))
    if brukervalg==1:
        print('Saldo:'), saldo()
    elif brukervalg==2:
        brukervalg2=int(input('Beløp: '))
        innskudd(brukervalg2)
    elif brukervalg==3:
        brukervalg3=int(input('Beløp: '))
        uttak(brukervalg3)
        print('Saldo: '), saldo()
    elif brukervalg==4:
        renteoppgjør()
    else: 
        print('Whack')


def skriv_tre_siste():
    global a
    global b
    global c
    if a==None and b==None and c==None:
        print('')
    elif c==None and b==None and a!=None:
        if a>0:
            print('+',str(a))
        else:
            print (str(a))
    elif c==None and b!=None and a!=None:
        if a>0:
            if b>0:
                print ('+'+str(a)+ '\n'+ '+'+ str(b))
            else:
                print ('+'+ str(a) +'\n' + str(b))
        else:
            if b>0:
                print(str(a) +'\n'+ '+'+str(b))
            else:
                print (str(a) +'\n' + str(b))
    else:
        if a>0:
            if b>0:
                if c>0:
                    print('+'+str(c) + '\n'+ '+'+ str(b) + '\n' + '+'+str(a))
                else:
                    print(str(c) + '\n+'+ str(b) + '\n', '+'+ str(a))
            else:
                if c>0:
                    print('+'+str(c) + '\n' + str(b) + '\n +'+ str(a))
                else:
                    print(str(c) + '\n' + str(b) + '\n +' + str(a))
        else:
            if b>0:
                if c>0:
                    print('+'+str(c) + '\n'+ '+'+ str(b) + '\n' + +str(a))
                else:
                    print(str(c) + '\n+'+ str(b) + '\n'+ str(a))
            else:
                if c>0:
                    print('+'+str(c) + '\n' + str(b) + '\n'+ str(a))
                else:
                    print(str(c) + '\n' + str(b) + '\n'+ str(a))

def velg():
    brukervalg=int(input('--------------------\n1 - Vis saldo\n2 - Innskudd\n3 - Uttak\n4 - Renteoppgjør\n5 - Siste endringer\n--------------------\nVelg handling: '))
    if brukervalg==1:
        print('Saldo:'), saldo()
    elif brukervalg==2:
        brukervalg2=int(input('Beløp: '))
        innskudd(brukervalg2)
    elif brukervalg==3:
        brukervalg3=int(input('Beløp: '))
        uttak(brukervalg3)
        print('Saldo: '), saldo()
    elif brukervalg==4:
        renteoppgjør()
    elif brukervalg==5:
        skriv_tre_siste()
    else: 
        print('Whack')

velg()
velg()
velg()
velg()