# Problem Programs
# (1) Pgm to find prime numbers between 1 to a given number N
n=int(input("Enter a Number: "))
print("Prime numbers from 1 to",n,'are:')
for i in range(1,n+1):             # Outer loop for tracking number 1 to N
#f=0
 for j in range(2,(i//2)+1):     # Inner loop for checking a number for complete division by any number other than 1 and itself
  r=i%j
  if r==0:
#f=1
  break
 if r!=0:
 print(i,end=" ")       # simple statement just to print a prime number'''
	
'''(2)     1
           2  3
           4  5  6
           7  8  9  10       '''
'''n=4
v=1
for i in range (1,n+1):             # Outer loop for row, loop variable is i, default step value is 1
	for j in range (1,i+1):     # Inner loop for print no. of required character in a row, loop variable is j, default step value is 1
		print(v,end=" ")    # simple statement just to print required character once, end is keyword used to make sure that how print is ending
		v+=1                # Increment of printing value as per requirement
	print("\n")                 # To change the row after completion of a paricular row'''


'''(3)     4  3  2  1
           3  2  1
           2  1
           1       '''
'''n=8
for i in range (n,0,-1):            # Outer loop for row, loop variable is i, Step value is -1
	for j in range (i,0,-1):    # Inner loop for print no. of required character in a row, loop variable is j, Step value is -1
		print("j,end=" ")   # simple statement just to print required character once, end is keyword used to make sure that how print is ending
	print("\n")                 # To change the row after completion of a paricular row'''

'''(4)     10  9  8  7
            6  5  4
            3  2
            1       '''
'''n=4
x=int(n*(n+1)/2)                                    # Initialization of printing value
for i in range (n,0,-1):                            # Outer loop for row, loop variable is i, Step value is -1
	for j in range (1,i+1):                     # Inner loop for print no. of required character in a row, loop variable is j, Step value is 1
		print("{:4d}".format(x),end=" ")    # simple statement just to print required character once, end is keyword used to make sure that how print is ending
		x-=1                                # Decrement of printing value as per requirement
	print("\n")                                 # To change the row after completion of a paricular row'''

'''(5)             a 
                b  c
             d  e  f
          g  h  i  j        '''
                  
'''n=4
v=ord('a')                                # Initialization of printing value
for i in range (1,n+1):                   # Outer loop for row, loop variable is i, default step value is 1
	for j in range(1,n-i+1):          # First Inner loop for print no. of required spaces in a row before starting to print actual value/character, loop variable is j, default step value is 1
		print(" ",end=" ")        # Simply print space once
	for j in range (1,i+1):           # Inner loop for print no. of required character in a row, loop variable is j, default step value is 1
		print(chr(v),end=" ")     # simple statement just to print required character once, end is keyword used to make sure that how print is ending
		v+=1                      # Increment of printing value as per requirement
	print("\n")                       # To change the row after completion of a paricular row'''

'''              *
                ***
               *****
              *******         '''
'''n=4
for i in range (1,n+1):                   # Outer loop for row, loop variable is i, default step value is 1
	for j in range(1,n-i+1):          # First Inner loop for print no. of required spaces in a row before starting to print actual value/character, loop variable is j, default step value is 1
		print(" ",end="")        # Simply print space once
	for j in range (1,2*i):           # Inner loop for print no. of required character in a row, loop variable is j, default step value is 1
		print('*',end="")     # simple statement just to print required character once, end is keyword used to make sure that how print is ending
	print("\n")                       # To change the row after completion of a paricular row'''
