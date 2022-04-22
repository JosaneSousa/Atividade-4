nome = input("Digite o nome: ")
data = input("Digite sua data de nascimento: ")
dia = data[0:2]
mês = data[2:4]
ano = data[4:8]
dataFormatada= dia+"/"+mês+"/"+ano
print("Meu nome é "+nome.title()+", nasci em "+dataFormatada)