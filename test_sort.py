python_list = []
python_list.append(100)
python_list.append(200)
python_list.append(10)
python_list.append(800)
python_list.append(60)

print('--------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

python_list.sort()

print('--------------------------')
print('【ソート表示】')
for value in python_list:
    print(value)
