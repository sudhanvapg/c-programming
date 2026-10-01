type=input("enter the category[commercial/non-commercial]:")
units=float(input("Enter the units of electricity consumed:"))
peak=input("is peak threshold found [yes/no]:")
bill = 0.0
if types=="commercial":
      if units<=100:
            amount=units*10
      elif unit>100 and unit<=300:
             amount=amount*12     
      else


if 'type' == "commercial":
    if units <= 100:
        price= unit * 10 
    elif unts <= 300:
        price = (100 * 10) + ((units - 100) * 12) 
    else:
        price = (100 * 10) + (200 * 12) + ((units - 300) * 15)



elif category == "non-commercial"        
    if rate < 0-100
        price=5/unit
    elif rate>=101 and rate <300:
            print=6/unit      
    elif rate >=300:
            print=50/unit        


elif category == "non-commercial":
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + ((units - 100) * 6)
    else:
        bill = (100 * 5) + (200 * 6) + ((units - 300) * 8)
else:
    print("Invalid category entered.")
    exit()

# 2. Apply surcharge using logical operators
# Condition: Commercial category AND peak threshold is yes
if category == "commercial" and peak_threshold == "yes":
    bill += 100
    print("Commercial peak threshold surcharge of Rs. 100 applied.")
elif category == "non-commercial" and peak_threshold == "yes":
    bill += 50
    print("Non-commercial peak threshold surcharge of Rs. 50 applied.")

# 3. Apply early payment discount (e.g., 5% discount)
if paid_early == "yes":
    discount = bill * 0.05
    bill -= discount
    print(f"Early payment discount of 5% (-Rs. {discount:.2f}) applied.")

# Final output
print(f"Total Electricity Bill: Rs. {bill:.2f}")
