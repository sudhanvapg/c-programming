base_price =250
day = input("Enter day of week : ")
age = int(input("Enter your age: "))
time = input("Enter time of day (morning, afternoon, evening): ")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    actual_price = base_price - (base_price * 0.25)
elif day == "Saturday" or day == "Sunday":
    actual_price = base_price + (base_price * 0.25)

if age < 5:
    base_price =50 
elif age >= 5 and age <= 15:
    base_price = 190
elif age >= 16 and age <= 50:
    base_price = 250
else:
    base_price = 120  
 
actual_price = base_price 
if time == "morning":
    final_price = actual_price 
elif time == "afternoon":
    final_price = actual_price + (actual_price * 0.10)
elif time == "evening":
    final_price = actual_price + (actual_price * 0.30)
else:
    final_price = actual_price  
print("Final ticket price: RS", final_price)






