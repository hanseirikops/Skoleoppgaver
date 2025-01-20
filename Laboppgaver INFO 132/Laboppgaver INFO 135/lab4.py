#Exercise 1
#a) O(log(n))
#b) O(n^2)
#c) O(n)

#Exercise 2
def one_pass(liste, index): 
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
    return liste

liste = [-4,0,1,9,0]
def selection_sort(liste):
    for index in range(len(liste)):
        one_pass(liste, index)
    print(liste)

selection_sort(liste)
# Expected output: [-4, 0, 0, 1, 9]

#Exercise 3

#Exercise 4
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']

def my_solution(nuts, bolts):
    for nut in range(len(nuts)):
        for bolt in range(len(bolts)):
            if nuts[nut]==bolts[bolt]:
                temp=bolts[bolt]
                bolts[bolt]=bolts[nut]
                bolts[nut]=temp
    print(nuts,bolts)

my_solution(nuts,bolts)