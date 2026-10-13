marks=['sachin',6,7,8,9,6]

my_mark=[]
sum=0
#dynamin inalisation
for number in range(5):
    newmark=int(input("Enter the marks:"))
    my_mark.append(newmark)

print("list elements are:")
for i in range(len(my_mark)):
    print("your marks: ",my_mark[i])

for i in range(len(my_mark)):
    sum+my_mark[i]
