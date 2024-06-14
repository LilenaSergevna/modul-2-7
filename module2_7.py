def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

#1
print_params()
print_params(4,6,False)
print_params(11,c=False)

print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list=[123,'текст',False]
values_dict={'a':875, 'b':'тут будет текст', 'c':777}

print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)