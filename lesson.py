add = str(input('do you want add name?(y) or (n)\n'))
all_list = []
while add == "y":
    all_list.append(str(input('enter your name: ')))
    all_list.append(str(input('enter your last name: ')))
    all_list.append(str(input('enter your age: ')))
    ex = str(input('do you want continue?(y) or (n): '))
    if ex == 'n':
        break
print(all_list)