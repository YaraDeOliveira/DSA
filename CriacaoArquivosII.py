#Automatizando o processo de gravacao
fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"
arq3 = open(fileName, "w")
arq3.write("Incluindo texto no arquivo criado")
arq3.close()
arq3 = open(fileName, "r")
print(arq3.read())
arq3.close()
