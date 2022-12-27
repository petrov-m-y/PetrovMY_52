# Sum from 1 to n
var_1 = int(input("Enter desired number: "))
agregator = []
for i in range(1, var_1+1):
    print(i, sep=" ", end=" ")
    if i < var_1:
        print("+", sep=" ", end=" ")
    agregator.append(i)
print("=", sum(agregator))
