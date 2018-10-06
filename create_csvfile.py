import csv

csv_file_path = 'C:/Users/amemiya/Documents/GitHub/Python/test.csv'
csv_file = open(csv_file_path, 'w', newline='')
#writer = csv.writer(
#    csv_file,
#    quoting=csv.QUOTE_ALL,
#    delimiter=':',
#    quotechar='`'
#)

writer = csv.writer(csv_file)

row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()
