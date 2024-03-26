print("**Welcome to Gross Pay Calculator**")

try:
    hours = int(input("Enter number of hours: "))
    rate = int(input("Enter rate: "))
except ValueError:
    print("Error, Please enter a numeric value.")
    quit()

if hours < 40:
    pay = round(hours * rate, 2)

else:
    overtime = hours - 40
    pay = round((40 * rate) + (overtime * rate * 1.5), 2)

print(f'Your pay is: {pay}')

