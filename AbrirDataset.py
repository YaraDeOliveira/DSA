r = open("/Users/fabioveiga/Downloads/salarios.csv", "r")
data = r.read()

#Para dividir o dataset em uma linha
#rows = data.split("\n")
#print(rows)

#Para dividir o dataset em colunas
'''rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
print(full_data)'''

'''#Contando as linhas de um arquivo
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1
print(count)'''

#Contando o numero de colunas de um arquivo
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0
for row in first_row:
    count += 1
print(count)