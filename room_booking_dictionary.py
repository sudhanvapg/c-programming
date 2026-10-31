# Main dictionary
booking_info = {}

# To get individual room details
def get_room_details():
    for i in range(5):
        print("\nEnter Room Booking Details", i+1)

        room_no = input("Enter Room Number: ")
        customer_name = input("Enter Customer Name: ")
        contact_number = input("Enter Contact Number: ")
        booking_amount = float(input("Enter Booking Amount: "))
        date = input("Enter Booking Date: ")

        gst = booking_amount * 0.18

        booking_info[room_no] = {
            "Customer Name": customer_name,
            "Contact Number": contact_number,
            "Booking Amount": booking_amount,
            "Date": date,
            "GST": gst
        }


# To display main dictionary
def display_booking():
    print("\n===== ROOM BOOKING DETAILS =====")

    for room_no, details in booking_info.items():
        print("\nRoom Number:", room_no)

        for key, value in details.items():
            print(key, ":", value)


# To get total room price and GST
def get_total_room_price():
    total_amount = 0
    total_gst = 0

    for details in booking_info.values():
        total_amount += details["Booking Amount"]
        total_gst += details["GST"]

    print("\n===== TOTAL BILL =====")
    print("Total Booking Amount:", total_amount)
    print("Total GST:", total_gst)
    print("Grand Total:", total_amount + total_gst)


# Main program
get_room_details()
display_booking()
get_total_room_price()