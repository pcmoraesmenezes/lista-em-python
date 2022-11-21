#Para criar listas em python é bem simples, a estrutura é essa: x = ["x0", "x1" , "x2" ... "xn"], sendo que o primeiro elemento e dado pelo valor x[0], por exemplo:
almoco = ["arroz", "feijão", "ovo", "frango", "suco de acerola"]
#para acessar toda a lista
print(almoco)
#para acessar um elemento especifico usa-se:
print(almoco[0])
#Uma lista em python e semelhante a uma lista sequencial em c/c++, porem utilizando indices, na memoria o funcionamento é praticamente o mesmo
#Para mudar um elemento é bem simples, a estrutura funciona da seguinte forma, o nome do vetor na posição de alteração desejada recebera o elemento desejado, por exemplo:
almoco[1] = "salada"
print(almoco[1])
#Há algumas maneiras de printar o elemento especifico, por exemplo se deseja printar o elemento de 1 a 2, usa-se print(variavel[1:2]), porem se deseja printar o ultimo elemento pode-se usar print(variavel[-1])
print(almoco[-1])
print(almoco[0:3])
#para adicionar um elemento na ultima posição da lista pode-se usar o comando append(), a estrutura é: variavel.apend  (""), e pronto o elemento sera adicionado na ultima posição da lista
almoco.append ("sobremesa")
print(almoco)
#para adicionar elementos em posição especifica usa-se o insert, por exemplo se deseja adicionar elemento na posição 2, a estrutura seria almoco.insert(2,"")
almoco.insert(2,"cenoura ralada")
print(almoco[2])
#para fazer uma concatenação de uma lista, ou seja, para adicionar uma lista na outra utiliza-se var = var1 + var2
ingredientes = ["polpa de acerola", "açucar", "agua"]
resultado = ["suco de acerola"]
suco = ingredientes + resultado
print(suco)
#para saber o tamanho da lista usa-se o comando len
print(len(suco))
print(len(almoco))
#voce pode buscar um elemento especifico em uma lista e o valor sera retornado em booleando, ou seja verdadeiro ou falso(usa-se o comando in)
print("sobremesa" in almoco)
print("feijao" in almoco)
#EXERCICIO:
mes =["0", "jan", "feb", "marc", "april", "may"]
exp = ["0", 2200, 2350, 2600, 2130, 2190]
print (mes)
print ( exp)
#Em comparação com fevereiro, quantos dolares voce gastou em janeiro
print("Foi gasto: " )
print(exp[2] - exp[1])
#Descubra quanto foi gasto nos tres primeiros meses
print("Nos tres primeiros meses foram gastos: ")
print(exp[1] + exp[2] + exp[3])
#Descubra se voce gastou 2000 dolares em algum mes:
if(2000 in exp):
  print("voce gastou 2000 dolares em um mes")
else:
  print("voce nao gastou 2000 dolares em um mes")
#Adicione o mes de junho com um gasto de 1980 dolares
mes.append("june")
exp.append(1980)

#voce devolveu um item de 200 dolares no mes de abril, desconte isso na sua lista
exp[4] = exp[4] + 200
print(exp[4])

