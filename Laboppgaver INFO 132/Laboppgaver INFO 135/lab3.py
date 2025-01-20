#lab3
#exercise 1
def selection_sort_one_pass(liste):
    pass_num=0
    for number in liste:
        if liste[number] < liste[pass_num]:
            liste[number], liste[pass_num]=liste[pass_num],liste[number]
    print(liste)

selection_sort_one_pass([5,2,3,4,0,1])

#exercise 2
import large_list
def filter_tuples(liste):
    filter_list=[]
    for tuppel in liste:
        if tuppel[0]+tuppel[1]==tuppel[2]:
            filter_list.append(tuppel)
    return filter_list

tuples=filter_tuples(large_list.liste)


def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j] > list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp

bubble_sort(tuples)
print(tuples)

#Exercise 3

def anagram_detector(string1, string2):
    string1=string1.lower().replace(' ','')
    string2=string2.lower().replace(' ','')
    list1=list(string1)
    list2=list(string2)
    
    bubble_sort(list1)
    bubble_sort(list2)

    if list1==list2:
        print('Anagram detected')
    else:
        print('No anagram detected')

anagram_detector('abc', 'cba')
anagram_detector('ABBA', 'baba')
anagram_detector('Astronomer', 'Moon starer')