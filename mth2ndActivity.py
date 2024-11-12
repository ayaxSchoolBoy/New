phone_number = input("Enter an 11-digit phone number: ")

if len(phone_number) != 11 or not phone_number.isdigit():
    print ("Invalid input. Please enter an 11-digit")
        
if phone_number[:2] != "09":
    print ("Invalid number. Must start with 09.")

key_digits = phone_number[2:4]
print("")
print("your number:",phone_number)    

if key_digits in ["13", "14", "20", "21", "28", "29", "30"]:
    print("The number belongs to Smart network.")
elif key_digits in ["08", "09", "10", "11", "12", "18", "19"]:
    print("The number belongs to TNT network.")
elif key_digits in ["22", "23", "32", "33"]:
    print("The number belongs to Sun network.")
elif key_digits in ["15", "16", "17", "25", "26", "27"]:
    print("The number belongs to Globe network.")
elif key_digits in ["03", "04", "05", "06", "07"]:
    print("The number belongs to Tm network.")
elif key_digits in ["01", "02", "24"]:
    print("The number belongs to Red network.")
else:  
    print ("Network not found.")