from socket import *
from constCS import *

def perform_operation(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    
    decoded_data = bytes.decode(data)
    operation, num1, num2 = decoded_data.split(',')
    num1 = float(num1)
    num2 = float(num2)
    
    result = perform_operation(operation, num1, num2)
    conn.send(str.encode(str(result)))

conn.close()