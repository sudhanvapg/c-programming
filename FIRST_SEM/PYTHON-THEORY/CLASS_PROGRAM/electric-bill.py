u=int (input('Enter the no of units:'))
t=int(input("press 0 = household / 1 = commercial:"))
date=int(input("Enter the date of payment e.g 1,4,17:"))
b=100
if t==0:
    if u>100 and u<=300:
        mu=u-b
        billamt=(mu*6)+(b*5)
    elif u>300:
        hu= u-300
        mu=u-hu-b
        billamt=(hu*8)+(mu*6)+(b*5)
    else:
        billamt= u*5
    peak=input("Is peak threshold found [yes/no]")
    if peak== "yes":
        billamt= billamt+50
elif t==1:
    if u>100 and u<=300:
            mu=u-b
            billamt=(mu*12)+(b*10)
    elif u>300:
            hu= u-300
            mu=u-hu-b
            billamt=(hu*15)+(mu*12)+(b*10)
    else:
            billamt= u*10
    peak=input("Is peak threshold found [yes/no]")
    if peak== "yes":
        billamt= billamt+100
else:
    print("Invalid input")

print(f"bill amount is: {billamt}")