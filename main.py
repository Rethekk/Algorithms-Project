from tkinter import *
import sys
INT_MIN = -32767

#A. Longest Common Subsequence
def LCS(X, Y, l1, l2):

    if l1 == 0 or l2 == 0:
        return 0
    elif X[l1 - 1] == Y[l2 - 1]:
        return 1 + LCS(X, Y, l1 - 1, l2 - 1)
    else:
        return max(LCS(X, Y, l1, l2 - 1), LCS(X, Y, l1 - 1, l2))


#B. Shortest Common Supersequence
def SCS(str1, str2, s1, s2):
    if s1 == 0 or s2 == 0:
        return s2 + s1
    if str1[s1 - 1] == str2[s2 - 1]:
        return SCS(str1, str2, s1 - 1, s2 - 1) + 1
    return min(SCS(str1, str2, s1, s2 - 1) + 1, SCS(str1, str2, s1 - 1, s2) + 1)


#C. Edit Distance
def editDistance(string1,string2,s1,s2):
    subprobs=[[0 for x in range(s2 + 1)] for x in range(s1 + 1)]
    for i in range(s1 + 1):
        for j in range(s2 + 1):
            if i == 0:
                subprobs[i][j] = j
            elif j == 0:
                subprobs[i][j] = i
            elif string1[i-1] == string2[j-1]:
                subprobs[i][j] = subprobs[i-1][j-1]
            else:
                subprobs[i][j] = 1 + min(subprobs[i][j-1], subprobs[i-1][j], subprobs[i-1][j-1])
    return subprobs[s1][s2]



#D. Longest Increasing Subsequence
global maximum
def _LIS(array, size):
   global maximum
   if size==1:
      return 1
   maxx=1
   for i in range(1, size):
      res = _LIS(array, i)
      if array[i-1] < array[size-1] and res + 1 > maxx:
         maxx = res + 1
   maximum = max(maximum, maxx)
   return maxx
def LIS(array):
   global maximum
   size = len(array)
   maximum = 1
   _LIS(array, size)
   return maximum
#LIS ending


#E. Matrix Chain Mult
def Order(x, i, j):
    if i == j:
        return 0
    min = sys.maxsize
    for k in range(i, j):
        count = (Order(x, i, k) + Order(x, k + 1, j) + x[i - 1] * x[k] * x[j])
        if count < min:
            min=count
    return min


#F. 0-1 knapsack
def knapSack(Y, wat, value, n):
   Ke = [[0 for x in range(Y + 1)] for x in range(n + 1)]

   for i in range(n + 1):
      for w in range(Y + 1):
         if i == 0 or w == 0:
            Ke[i][w] = 0
         elif wat[i-1] <= w:
            Ke[i][w] = max(value[i-1] + Ke[i-1][w-wat[i-1]], Ke[i-1][w])
         else:
            Ke[i][w] = Ke[i-1][w]

   return Ke[n][Y]

#G. Partition Problem
def findPartition(array, n):
   sum = 0
   i, j = 0, 0

   for i in range(n):
      sum += array[i]

   if sum % 2 != 0:
      return False

   side = [[True for i in range(n + 1)]
         for j in range(sum // 2 + 1)]

   for i in range(0, n + 1):
      side[0][i] = True

   for i in range(1, sum // 2 + 1):
      side[i][0] = False

   for i in range(1, sum // 2 + 1):

      for j in range(1, n + 1):
         side[i][j] = side[i][j - 1]

         if i >= array[j - 1]:
            side[i][j] = (side[i][j] or
                     side[i - array[j - 1]][j - 1])

   return side[sum // 2][n]

#H. Cut Rod
def cutRod(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]

#I. Coin-Change-Making-Problem

def coins(So, mo, no):
    tab = [0 for k in range(no + 1)]

    tab[0] = 1

    for i in range(0, mo):
        for j in range(So[i], no + 1):
            tab[j] += tab[j - So[i]]

    return tab[no]

#J. Work Break
def wordBreak(worddict, wordstr,wordout = ""):

    if not wordstr:
        print(wordout)
        return

    for i in range(1, len(wordstr) + 1):
        pre = wordstr[:i]

        if pre in worddict:
            wordBreak(worddict, wordstr[i:], wordout + " " + pre)


#END OF ALGORITHMS


def A():
    #LCS calling
    user = "A"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('A'):
            a2=next(E)
            a3=next(E)
    print("A. The Longest Common Subsequence length is:", LCS(a2,a3,len(a2),len(a3)))
    E.close()

def B():
    #SCS calling
    user = "B"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('B'):
            a2 = next(E)
            a3 = next(E)

    E.close()
    scss1 = len(a2)
    scss2 = len(a3)
    #print(a2,a3,scss1,scss2)
    print("B. The length of shortest Common supersequence is",SCS(a2,a3,scss1,scss2))

def C():
    #Edit Distance calling
    user = "C"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('C'):
            a2 = next(E)
            a3 = next(E)
    E.close()
    #edit distance calling
    print("C. The Edit Distance is: ",editDistance(a2,a3, len(a2), len(a3)))

def D():
    user = "D"
    f = open("algoproj.txt")
    for line in f:
        if line.startswith('D'):
            d2 = next(f)
            d2 = d2.split(',')
            field2= list(d2)
    input1 = []
    for xs in field2:
        input1.append(int(xs))
    lissize=len(input1)
    print ("D. Longest Increasing Subsequence's length is", LIS(input1))
    f.close()

def E():
    user = "E"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('E'):
            d2 = next(E)
            d2 = d2.split(',')
            field2 = list(d2)

    E.close()
    input1 = []
    for xs in field2:
        input1.append(int(xs))
    print(input1)
    #Matrix chain multiplication
    matrixlen=len(input1)
    print(matrixlen)
    print("E. Minimum number of multiplications is: ", Order(input1,1,matrixlen-1))

def F():
    user = "F"
    f = open("algoproj.txt")
    for line in f:
        if line.startswith('F'):
            yss = next(f)
            z = next(f)
            w = next(f)
            w = w.split(',')
            w = list(w)
            w = w[0]
            yss = yss.split(',')
            z = z.split(',')
            fields= list(yss)
            zeus = list(z)
    input1 = []
    input2 = []
    for xs in yss:
        input1.append(int(xs))
    for xs in zeus:
        input2.append(int(xs))
    # 0-1 knapsack calling
    knap0n = len(input1)
    print("F. 0-1 Knapsack : ",knapSack(242,input2,input1,knap0n))
    f.close()

def G():
    #partition calling
    user = "G"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('G'):
            d2 = next(E)
            d2 = d2.split(',')
            field2 = list(d2)
    E.close()
    input1 = []
    for xs in field2:
        input1.append(int(xs))
    print(input1)
    print("G. Partition Problem answer: ")
    partitionN = len(input1)
    if findPartition(input1, partitionN) == True:
        print("Can be divided into two",
            "subsets of equal sum")
    else:
        print("Cannot be divided into ",
            "two subsets of equal sum")

def H():
    #rod calling
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('H'):
            d2 = next(E)
            d2 = d2.split(',')
            field2 = list(d2)
    E.close()
    input1 = []
    for xs in field2:
        input1.append(int(xs))
    print(input1)
    rodsize = len(input1)
    print("H. In Rod Cutting the Maximum Obtainable Value is : " + str(cutRod(input1, rodsize)))

def I():
    #coin problem calling
    isso = open("algoproj.txt",'r')
    for line in isso:
        if line.startswith('I'):
            d2 = next(isso)
            d2 = d2.split(',')
            field2 = list(d2)
    isso.close()
    input1 = []
    for xs in field2:
        input1.append(int(xs))
    print(input1)
    coinm = len(input1)
    coinn = 4
    coinx = coins(input1, coinm, coinn)
    print("I. In coin problem the minimum number of coins are : ",coinx)

def J():
    #word break problem calling
    user = "J"
    E = open("algoproj.txt")
    for line in E:
        if line.startswith('J'):
            a2 = next(E)
            a2 = a2.split(',')
            field2 = list(a2)
            a3 = next(E)
            print(a2,a3)
    E.close()
    print("J. Word break solution: \n")
    wordBreak(a2, a3)

from tkinter.font import Font

root = Tk()
bigFont = Font(family="Helvetica", size=12, weight="bold")
button_1 = Button(root, text="   Longest Common Subsequence   ",command=A, padx=20, pady=10,bg="lightblue1", font=bigFont)
button_2 = Button(root, text="  Shortest Common Supersequence ",command=B, padx=20, pady=10,bg="lightskyblue1", font=bigFont)
button_3 = Button(root, text="Levenshtein Distance (edit-distance)",command=C, padx=20, pady=10,bg="skyblue1",font=bigFont)
button_4 = Button(root, text="   Longest Increasing Subsequence  ",command=D, padx=20, pady=10,bg="skyblue3",font=bigFont)
button_5 = Button(root, text="    Matrix Chain Multiplication    ",command=E, padx=42, pady=10,bg="steelblue2",font=bigFont)
button_6 = Button(root, text="0-1-knapsack-problem",command=F, padx=72, pady=10,bg="steelblue3",font=bigFont)
button_7 = Button(root, text="Partition-problem",command=G, padx=92, pady=10,bg="steelblue4",font=bigFont)
button_8 = Button(root, text="Rod Cutting Problem",command=H,padx=78, pady=10,bg="deepskyblue4",font=bigFont)
button_9 = Button(root, text=" Coin-change-making-problem",command=I, padx=43, pady=10,bg="dodgerblue4",font=bigFont)
button_10 = Button(root, text="Word Break Problem",command=J, padx=80, pady=10,bg="royalblue4",font=bigFont)

button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()
button_5.pack()
button_6.pack()
button_7.pack()
button_8.pack()
button_9.pack()
button_10.pack()
button_11 = Button(text="QUIT", bg="red",fg="black",command=root.destroy, font=bigFont)
root.title("K180242-K181185 Algorithms Project")
root.iconbitmap("favicon.ico")
button_11.pack(side="bottom")
root.mainloop()


#Made by
#K181185 & K180242