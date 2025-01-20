Farhenheit_fra=0.59783
Celcius_til= ((Farhenheit_fra-32)*5/9)
print(Farhenheit_fra,'grader Farenheit tilsvarer', Celcius_til, 'grader Celcius')

#Har blitt lagt til for å gi 2 siffer i svaret uten å konvertere Celcius_til til streng
Celcius_til1= '%1.2f' % (Celcius_til)
Farhenheit_fra1= '%1.2f' % (Farhenheit_fra)

Farhenheit_mer= '%0.2f' % ((Celcius_til*9/5)+32)
print(Farhenheit_fra, 'grader Farenheit tilsvarer', Celcius_til1, 'grader Celcius\n', Celcius_til1, 'grader Celsius tilsvarer', Farhenheit_mer, 'grader Farenheit')

# 3d)
print(Farhenheit_fra1, '\N{DEGREE SIGN}F =', Celcius_til1, '\N{degree celsius}\n', Celcius_til1, '\N{degree celsius} =', Farhenheit_mer, '\N{DEGREE SIGN}F')