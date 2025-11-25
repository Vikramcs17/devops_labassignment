# calculator.py
def calculate(a, b, op):
    """Perform a simple operation on two numbers."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    else:
        raise ValueError("Unsupported operation")

if __name__ == "__main__":
    print("Simple Calculator v1.0")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operation (+ - * /): ")
    print("Result:", calculate(x, y, op))
