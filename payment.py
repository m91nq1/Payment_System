def main():
    for x in range(1, 16):
        print("You are using the Microsoft payment system")
        
        name = input("Enter employee name: ")
        
        while True:
            try:
                salary = float(input("Enter the salary: "))
                break
            except ValueError:
                print("Error: Please enter a valid numerical value for salary.")
        
        while True:
            try:
                kilometres = float(input("Distance Travelled in Kilometres: "))
                break
            except ValueError:
                print("Error: Please enter a valid numerical value for kilometres.")
        
        while True:
            try:
                hours = float(input("Overtime hours: "))
                break
            except ValueError:
                print("Error: Please enter a valid numerical value for hours.")
        
        while True:
            try:
                contributions = float(input("Sundry Contributions: "))
                break
            except ValueError:
                print("Error: Please enter a valid numerical value for contributions.")
        
        print(f"Employee name: {name}")
        
        num1 = kilometres * 3
        num2 = hours * ((salary / 168) * 1.5)
        num3 = salary
        num4 = contributions
        num5 = num1 + num2 + num3 + num4
        
        print(f"Total Salary: R{num5}")

if __name__ == "__main__":
    main()

