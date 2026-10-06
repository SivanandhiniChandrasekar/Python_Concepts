# Nested if

mark = int(input("Enter your 12th mark: "))
certificates = input("Enter YES if you have all certificates, Otherwise NO ")
cut_off = float(input("Enter your engineering cut-off: "))
allot_number = int(input("Enter your Admission number: "))
dept = input("Enter the Department alloted: ")

if mark > 500 and cut_off > 160.0:
    if certificates == "YES":
        if dept == 'IT' and allot_number == 42146:
            print("The seat is filled")
        elif dept == 'IT' and allot_number != 42146:
            print("Switched to another dept")
        else:
            print("Not enrolled in this college")
    else:
        print("Get your certificates within 10 days")
else:
    print("Sorry! You are not eligible to alloted in this college!")