'''for x in range(11,21):
    print("{:4d}".format(x),end=" ")
print('hello')
#print(s)'''
#print(chr(ord('a')))
n=int(input("Enter a Number: "))
print("Prime numbers from 1 to",n,'are:')
for i in range(2,n+1):            
#f=0
    for j in range(2,(i//2)+1):     
        #r = i % j
        if i%j == 0:
#f=1
            break
    #if (r == 0):
        #print(i,end=" ")
    print(i,r)