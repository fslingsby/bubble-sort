number_list = []
num1 = input("Enter the first number to be sorted: ")
number_list.append(int(num1))
adding = True
num2 = input("Add more numbers to the list, pressing enter each time, "
                 "and when you are ready to begin the sort, type 'sort': ")
number_list.append(int(num2))
while adding:
    next_num = input()
    if next_num == 'sort':
        adding = False
    else:
        number_list.append(int(next_num))
order = input("What order would you like the list? Choose 'a' for ascending, or 'd' for descending: ")

sorted_list = [number_list[0]]

for i in number_list[1:]:
    if order == 'd':
        print(sorted_list[::-1])
    else:
        print(sorted_list)
    pos = 0
    bigger = True
    while bigger:
        if i > sorted_list[pos]:
            pos += 1
        else:
            bigger = False
            sorted_list.insert(pos,i)
        if pos == len(sorted_list):
            bigger = False
            sorted_list.insert(pos,i)
