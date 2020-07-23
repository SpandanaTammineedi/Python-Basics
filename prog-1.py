# To write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        inum=int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest=inum
    elif inum<smallest:
        smallest=inum
    if largest is None:
        largest=inum
    elif inum>largest:
        largest=inum
print("Maximum is", largest)
print("Minimum is", smallest)

#Build function:
def computepay(h,r):
    if h<=40:
        pay= h*r
    else:
        x=h-40
        pay= (40*r)+(1.5*r*x)
    return pay

hrs = input("Enter Hours:")
rt= input("Enter Rate:")
hours=float(hrs)
rate=float(rt)

p = computepay(hours,rate)
print("Pay",p)









#Conditional and try:
s=input("Enter score:")
score=float(s)
if 0.0<=score<=1.0:
    if score>=0.9 :
        print("A")
    elif score>=0.8:
        print("B")
    elif score>=0.7:
        print("C")
    elif score>=0.6:
        print("D")
    elif score <0.6:
        print("F")
else:
    print("Error")
    quit()



#Conditional
hrs= input("Enter hours:")
rate= input("Enter rate:")
h= float(hrs)
r= float(rate)
if h<=40:
    pay= h*r
else:
    x=h-40
    pay= (40*r)+(1.5*r*x)
print(pay)












nam=input('Who are you?')
print('Welcome',nam)

#Convert User input type
hrs = input("Enter hours:")
rate = input("Enter rate:")
pay = float(hrs)*float(rate)
print("Pay:",pay)
