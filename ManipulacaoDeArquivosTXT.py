texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."
print(texto)

'''import os
arquivo = open(os.path.join("/Users/fabioveiga/Downloads/cientista.txt"), "w")
#gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra+" ")
arquivo.close()'''

'''arquivo = open(os.path.join("/Users/fabioveiga/Downloads/cientista.txt"), "r")
print(arquivo.read())
arquivo.close()'''

#Usando a expressao with / sendo que o metodo close () eh executado automaticamente
#with open("/Users/fabioveiga/Downloads/cientista.txt", "r") as arquivo:
 #   conteudo = arquivo.read()
#print(len(conteudo))
#print(conteudo)

with open("/Users/fabioveiga/Downloads/cientista.txt", "w") as arquivo:
    arquivo.write(texto[:21])
    arquivo.write("\n")
    arquivo.write(texto[:33])

with open("/Users/fabioveiga/Downloads/cientista.txt", "r") as arquivo:
    conteudo = arquivo.read()



