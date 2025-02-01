number_list = []
num1 = input("Enter the first number to be sorted: ")
number_list.append(int(num1))
adding = True
while adding:
    next_num = input("Add another number to the list, or type 'sort' to sort the list in ascending order: ")
    if next_num == 'sort':
        adding = False
    else:
        number_list.append(int(next_num))

sorted_list = [number_list[0]]

for i in number_list[1:]:
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
