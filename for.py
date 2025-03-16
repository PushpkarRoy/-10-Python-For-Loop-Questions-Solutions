# Q1 print no. from 1 to 5 for the using for loop ----------------
for ol in range(1,6,1):
    print(ol, end=" ")

# Q2 write the squre of the no. 1 to 5 --------------------------

for i in range(1,6,1):
    print(i*i, end=" ")

#  or =================================
for a in range(1,6,1):
    b = a * a
    print(b,end=" ")

#  Q3 print even no. from 1 to 10----------------------------
for i in range(2,11,2):
    print(i, end=" ")

#  or ===============================

for a in range(1,11,1):
    if (a %2 == 0):
        print(a, end=" ")

# Q4  calculate sum of no. from 1 to 10 ---------------------------

total = 0
for i in range(1,11,1):
    total += i
print(total)

# Q5 write a program to print python in reverse ----------------------

a = "python" 
for i in range(len(a) -1, -1,-1):
    print(a[i], end="") 
    
# Q6 write a program to count the number of vowels in the world "education "

a = "education"
v = "aeiou"

count = 0
for el in range(0,len(a), 1):
        if(a[el] in v ):
            count+=1       
print(count)
# or =======================

a = "education"
v = "aeiou"
count = 0

for i in a:
    if i in v:
        count += 1
print(count)

# Q7 print  fibonaci sequence upto 10---------------
a = 0
b = 1
print(a,b, end=" ")
for _ in range(8):
    next_step = a + b
    print(next_step,end= " ")
    a,b = b,next_step

#  Q8 Calculate the factoral of the no. 5

a = int(input("enter the value :="))
for i in range(1,a,1):
    a*= i
print("The factorial of ",i +1, "is", a)

# or =============================

fact = 5
input = 1
for i in range(1,fact +1):
    input*= i
print(input)

# Q9 write a program to check if a given number such as 7 is a prime number

a = int(input("Enter the value :="))
for i in range(2,a-1):
    if(a %i == 0 ):
        print(i)
    
# OR =======================

a = 100
is_prime = True


for i in range(2,a-1):
    if(a %i == 0 ):
        is_prime = False
        
        

if is_prime and a > 1:
    print( a, "is a prime no")
else:
    print(a,"is not a prime no")
  
# Q10 count occurrencess of each charactor in a string
    #    Write a program to count occurrencess of each charater inthe word "Programming"

word = "programming"
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char,count in char_count.items():
    print(char, ':', count)
