my_list = [35, 'week', False, 3.1415, 'week', 'holidays']
str_count = 0
for i in my_list:
    if type(i) is str:
        str_count = int((str_count+1))
print(int(str_count))