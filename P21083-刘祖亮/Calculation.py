while True:
    n = int(input("Enter first number:"))
    s = input("Enter + - * /:")
    m = int(input("Enter second number:"))
    t = 0
    if s == "+" :
        t = n + m
    elif s == "-":
        t = n - m
    elif s == "*":
        t = n * m
    else:
        t = n / m
    print(t)
