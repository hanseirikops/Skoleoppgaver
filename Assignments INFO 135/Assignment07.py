#1
#Big O for the function T(n) is O(n^3)

#2
#O(nlog2(2))
#The for loop will run n times. for each time this loop runs, the while loop runs log2(n). The loop therefore runs wiht the big O notation O(nlog2(n))

#3
#O(n^2)
#The first for loop will run for n-1 times. The second for loop will then run n-(k-1) times for each time the first loop runs. Then you get (n-1)(n-(k-1))=n^2-n-(nk-n-k+1), which give big O notation of O(n^2)

#4
def solve_problem(liste):
    i=len(liste)
    total=0
    for tall in range(i):
        total+=liste[tall]
    snitt=total/(i)
    print (snitt)

#The for loop goes through the problem n times. This give big O notation of O(n)