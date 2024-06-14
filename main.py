if __name__ == "__main__":
    try:
        # Input number for the Fibonacci series
        number = int(input("Enter number for Fibonacci Series: "))
        
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            num1 = 0
            num2 = 1
            print(num1, num2, end=" ")
            for i in range(2, number):
                num3 = num1 + num2
                print(num3, end=" ")
                num1 = num2
                num2 = num3
    except ValueError:
        print("Please enter a valid integer.")




 
