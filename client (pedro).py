from socket import *
from constCS import *

def send_operation(operation, num1, num2):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    
    data = f"{operation},{num1},{num2}"
    s.send(str.encode(data))
    
    result = s.recv(1024)
    print("Result:", bytes.decode(result))
    
    s.close()

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            send_operation("add", num1, num2)
        elif choice == 2:
            send_operation("subtract", num1, num2)
        elif choice == 3:
            send_operation("multiply", num1, num2)
        elif choice == 4:
            send_operation("divide", num1, num2)
        else:
            print("Invalid choice")