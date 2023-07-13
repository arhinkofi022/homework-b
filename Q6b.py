def check_triangle():
    a = int(input("Enter the length of the first stick: "))
    b = int(input("Enter the length of the second stick: "))
    c = int(input("Enter the length of the third stick: "))

    if is_triangle(a, b, c):
        print("Yes, you can form a triangle.")
    else:
        print("No, you can't form a triangle.")
