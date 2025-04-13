# x0 = 2
# y0 = 2

# r = 1

# x1 = 1
# y1 = 1
# x2 = 3
# y2 = 3

# if (x1 <= x0 <= x2) and (y1 <= y0 <= y2):
#     print("круг пересекается с квадратом")
# else:
#     print("чё то не так")

X = float(input("Введите x: "))
Y = float(input("Введите y: "))

X2 = float(input("Введите x2: "))
Y2 = float(input("Введите y2: "))

if (abs(X) <= 2 and abs(Y) <= 2) and (X2 + Y2 >= 1):
    print("Услвоия выполняются")
else:
    print("Услвоия не выполняются")
