#marks obtained by a student in 5 sub      
#( create a new list        to store marks of five subject)



marks=['sachin',50,55,67,76,89]  
#//declares an list 'mark' to store marks of 'sachin's

my_mark=[]
#dynamic initialization
for number in range(5):
    newmark=int(input("Enter the marks:"))
    my_mark.append(newmark)
print("list elements are:")
for i in range(len(my_mark)):
    print("your marks: ",my_mark[i])