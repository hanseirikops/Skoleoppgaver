#Oppgave 1
print('        *\n'
'        **\n'
'        * *\n'
'*********  *\n'
'        *   *\n'
'*********  *\n'
'        * *\n'
'        **\n'
'        *')
#Oppgave 2
# i)
antall_studenter = 55
antall_kvinner = 32
kvinneandel = Antall_kvinner/antall_studenter #Antall_kvinner er skrevet med stor A
print('kvinneandelen er ', kvinneandel)
#Dette er en syntax feil
#ii)
antall_studenter = 55
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter 
print(kvinneandelen er , kvinneandel) #Kvinneandelen er er skrevet uten ''
#Dette er en syntax feil
#iii)
antall_studenter = 55 
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter 
print('kvinneandelen er ' kvinneandel) #Mangler ,
#Dette er en syntax feil
#iv)
kvinneandel = antall_kvinner/antall_studenter #antall_kvinner og antall_studenter er ikke definert enda
antall_studenter = 55
antall_kvinner = 32
print('kvinneandelen er ', kvinneandel)
#Dette er en logisk feil
#v)
kvinneandel = antall_kvinner=32/antall_studenter=55 #antall_kvinner og antall studenter trenger ikke være her
print('kvinneandelen er ', kvinneandel)
#Dette er en syntax feil
#vi)
antall_studenter = 55
antall_kvinner = 32
kvinneandel = antall_studenter/antall_kvinner #feil regnestykke
print('kvinneandelen er ', kvinneandel)
#Dette er en semantisk feil
#2b)
antall_studenter = 55
antall_kvinner = 32
kvinneandel = '%1.2f' % (antall_kvinner/antall_studenter)
print('kvinneandelen er', kvinneandel)