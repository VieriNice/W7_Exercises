# num = int(input('Enter a number: '))

# if num == 0:
#     raise Exception("Cannot be 0")

# print(f'Your number is {num}')








def divide_by(num):
    try:
        div_num = int(num)
        if div_num == 0:
            raise ZeroDivisionError("Cannot be 0")
    except ValueError:
        print("Not a number")
        div_num = None
    except ZeroDivisionError:
        print("Number cannot be zero")
    return f'Your number is {div_num}'

print(divide_by(input("Enter a number: ")))