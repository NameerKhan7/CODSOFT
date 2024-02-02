size = input("Enter size of array : ")
i = 0
list = []
for i in range(int(size)):
    list[i] = print("the value of i is : ",i)
    # value = input("Enter values of array : ")
    # list.append(int(value))
    i+=1

print(list)

choice = input("Choose 1. To stay 0. to leave: ")

if choice == "0":
    exit()
elif choice == "1":
    print("Thanku for staying")
else:
    print("Invalid choice")
    exit()    