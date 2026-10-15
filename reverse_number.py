n = int(input("Enter a whole number please. "))
print("Numbers from {0} to {1} are ".format(n, 1))

for i in range(n, 0, -1):
    print(i)

for i in range(1, 6):
    print("⭐" * i)