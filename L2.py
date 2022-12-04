# Запись данных
# colors = [ 'red', 'green', 'blue3']
# data = open('file.txt', 'w')
# data.writelines(colors)
# data.close()

# Чтение данных
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# def concatenatio (*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

#Словарь
dictionary = {}
dictionary = \
    {
        'up': '*',
        'left': '/',
        'down': '-',
        'right': '+'
    }
# print(dictionary)
# print(dictionary['left'])

for k in dictionary.keys():
    print(k)