import math
import random
import string
import timeit

# Calculos dois numeros
# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# print("Soma: ", a+b,
#       "\nDiferença: ", a-b,
#       "\nMédia: ", (a+b)/2,
#       "\nDistancia: ", math.fabs(a-b),
#       "\nO maior: ", (a+b+math.fabs(a-b))/2,
#       "\nO Menor: ", (a+b-math.fabs(a-b))/2)

# Mostrar horas, minutos e segundos dos segundos
# segundos = float(input("Informe os segundos em inteiros: "))
# minutos = segundos//60
# segundos = segundos%60
# horas = minutos//60
# minutos = minutos%60
# print("Horas: ", horas,
#       "\nMinutos: ", minutos,
#       "\nSegundos: ", segundos)
# Inverter número
# valor = int(input("Digite um valor de 4 digitos: "))
# digito1 = valor//1000
# resto = valor%1000
# digito2 = resto//100
# resto = resto%100
# digito3 = resto//10
# digito4 = resto%10
# print(digito4*1000+digito3*100+digito2*10+digito1)

# Calculo peso
# altura = float(input("Digite a altura: "))
# sexo = str(input("Digite o sexo (Masculino = M; Feminino = F): "))
# if(sexo == "F" or sexo == "f"):
#     print("Peso ideal feminino: ", 62.1*altura - 44.7)
# elif(sexo == "M" or sexo == "m"):
#     print("Peso ideal masculino: ", 72.7*altura - 58)
# else: print("Sexo inválido")

# Horário do jogo
# hora = int(input("Digite o valor da HORA que INICIOU o jogo: "))
# minuto = int(input("Digite o valor da MINUTO que INICIOU o jogo: "))
# inicio = hora*60+minuto
# hora = int(input("Digite o valor da HORA que FINALIZOU o jogo: "))
# minuto = int(input("Digite o valor da MINUTO que FINALIZOU o jogo: "))
# fim = hora*60+minuto
# if(inicio >= fim):
#     duração = fim+60*24 - inicio
# else: duração = fim - inicio
# print("A duração do jogo foi de",duração//60,"horas e",duração%60,"minutos")

# Número Capicua
# numero = int(input("Digite 4 digitos inteiros: "))

# if(numero < 1111 and numero > 9999): print("Numero inválido!")
# else:
#     numeroInv = numero//1000 + ((numero%1000)//100)*10 + ((numero%100)//10)*100 + (numero%10)*1000
#     if(numero == numeroInv): print("Números capicua!:",numero,numeroInv)
#     else: print("Não são números capcua!",numero,numeroInv)

# Ordem Crescente 3 valores
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# if(valor2 < valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# valor3 = int(input("Digite o terceiro valor: "))
# if(valor3 < valor1):
#     cache = valor1
#     valor1 = valor3
#     valor3 = valor2
#     valor2 = cache
# if(valor3 < valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# print(valor1, valor2, valor3)

# Ordem Crescente e decrescente 3 valores
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# maior = valor1
# if(valor2 > maior): maior = valor2
# if(valor3 > maior): maior = valor3
# menor = valor1
# if(valor2 < menor): maior = valor2
# if(valor3 < menor): maior = valor3
# meio = valor1+valor2+valor3 - maior - menor
# print("Crescente:",menor,meio,maior)
# print("Decrescente:",maior,meio,menor)

# Ordem Crescente 4 valores - 1
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# if(valor2<valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# valor3 = int(input("Digite o terceiro valor: "))
# if(valor3<valor1):
#     cache = valor2
#     valor2 = valor1
#     valor1 = valor3
#     valor3 = cache
# elif(valor3<valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# valor4 = int(input("Digite o quarto valor: "))
# if(valor4<valor1):
#     cache = valor2
#     valor2 = valor1
#     valor1 = valor4
#     valor4 = valor3
#     valor3 = cache
# elif(valor4<valor2):
#     cache = valor2
#     valor2 = valor4
#     valor4 = valor3
#     valor3 = cache
# elif(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# print(valor1, valor2, valor3, valor4)

# Ordem Crescente 4 valores - 2
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# valor3 = int(input("Digite o terceiro valor: "))
# valor4 = int(input("Digite o quarto valor: "))
# if(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# if(valor3<valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# if(valor2<valor1):
#     cache = valor1
#     valor1 = valor2
#     valor2 = cache
# if(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# if(valor3<valor2):
#     cache = valor2
#     valor2 = valor3
#     valor3 = cache
# if(valor4<valor3):
#     cache = valor3
#     valor3 = valor4
#     valor4 = cache
# print(valor1, valor2, valor3, valor4)

# Preço de venda
# custo = float(input("Digite o custo do produto: "))
# if(custo<10): venda = custo*70/100+custo
# if(custo>=10 and custo<30): venda = custo*50/100+custo
# if(custo>=30 and custo<50): venda = custo*40/100+custo
# if(custo>=50): venda = custo*30/100+custo
# print("\nPreço de venda: ",venda)

# Media ponderada
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# if(nota2>nota1):
#     cache = nota1
#     nota1 = nota2
#     nota2 = cache
# if(nota3>nota1):
#     cache = nota1
#     nota1 = nota3
#     nota3 = cache
# print("Media: ", (nota1*5+nota2*2.5+nota3*2.5)/(5+2.5+2.5))

# Bhaskara
# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = float(input("Digite o valor de c: "))
# delta = b**2 - 4*a*c
# if(delta<0 or a == 0): print("Erro, delta negativo ou divisão por 0")
# else:
#     x1 = (-b + math.sqrt(delta))/(2*a)
#     x2 = (-b - math.sqrt(delta))/(2*a)
#     print(x1, x2)

# Saldo e limite
# saldo = float(input("Informe seu saldo médio: "))
# if(saldo<500): print("Não há limite.")
# elif(saldo>=500 and saldo<1000): print("Limite: ", saldo*8/100)
# else: print("Limite: ", saldo*15/100)

# Seleção aninhada - Quantas raizes?
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
# delta = b*b - 4*a*c
# if((delta) < 0):
#     print("\nNão há raizes")
# else:
#     if((delta) == 0):
#         x = -b/(2*a)
#         print(f"Possui uma raiz, que é {x}")
#     else:
#         x = (-b + math.sqrt(delta))/(2*a)
#         y = (-b - math.sqrt(delta))/(2*a)
#         print(f"Tem duas raizes, que são: {x}, {y}")

# Seleção aninhada - Condições climáticas
# temp = float(input("Digite a temperatura: "))
# if(temp>30):
#     humid = float(input("Qual a humidade? "))
#     if(humid > (60/100)):
#         print("Tempo quente e humido.")
#     else:
#         print("Tempo quente.")
# else:
#     if(temp<=30 and temp>=20):
#         print("Ameno.")
#     else:
#         if(temp<20 and temp>=10):
#             print("Frio.")
#         else:
#             print("Muito frio.")

# Seleção aninhada
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# n3 = float(input("Digite a terceira nota: "))
# freq = float(input("Qual a frequencia do aluno? "))
# if(freq<0.75):
#     print(f"Reprovado por faltas! frequencia: {freq}")
# else:
#     if(n1 > 10 or n2 > 10 or n3 > 10):
#         print("Valor inválido.")
#     else:
#         if(n1 < 0 or n2 < 0 or n3 < 0):
#             print("valor inválido")
#         else:
#             g1 = (n1+n2+n3)/3
#             if(g1 >= 7):
#                 print(f"Aluno aprovado! Media: {g1}")
#             else:
#                 if(g1<4):
#                     print("Aluno reprovado!")
#                 else:
#                     print("Reprovado G1!")
#                     n1 = float(input("Digite a primeira nota: "))
#                     n2 = float(input("Digite a segunda nota: "))
#                     n3 = float(input("Digite a terceira nota: "))
#                     if(n1 > 10 or n2 > 10 or n3 > 10):
#                         print("Valor inválido.")
#                     else:
#                         if(n1 < 0 or n2 < 0 or n3 < 0):
#                             print("valor inválido")
#                         else:
#                             g2 = (n1+n2+n3)/3
#                             media = (g1 + g2) / 2
#                             if(media >= 5):
#                                 print(f"Aluno aprovado em grau 2! Media grau 2: {media}")
#                             else:
#                                 print("Aluno reprovado em grau 2!")

# Seleção aninhada - Notas
# nota = float(input("Digite a nota do aluno de 0 - 100: "))
# if(nota>100 or nota < 0):
#     print("Nota inválida")
# else:
#     if(nota >= 90):
#         print("A")
#     else:
#         if(nota >= 80):
#             print("B")
#         else:
#             if(nota >= 70):
#                 print("C")
#             else:
#                 if(nota >= 60):
#                     print("D")
#                 else:
#                     print("F")

# Seleção aninhada - dia da pascoa em um ano específico
# ano = int(input("Digite um ano entre 1900 e 2099: "))
# if(ano>2099 or ano<1900):
#     print("Valor inválido")
# else:
#     a = ano % 19
#     b = ano % 4
#     c = ano % 7
#     d = (19 * a + 24) % 30
#     e = (2 * b + 4 * c + 6 * d + 5) % 7
#     dia = 22 + d + e
#     if(ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076):
#         dia = dia - 7
#     else:
#         if(dia>31):
#             print("Data da páscoa:", dia % 31,"de Abril")
#         else:
#             print("Data da páscoa: ", dia, "de Março")

# Dias do calendário - Elif
# mes = int(input("Digite o mês 1 - 12: "))
# if(mes>12 or mes<1):
#     print("Mês inválido")
# elif(mes == 2):
#     dias = 28
# elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#     dias = 30
# else:
#     dias = 31
# print(f"Quantidade de dias no mês eh: {dias}")

# Calculo IMC
# peso = float(input("Digite o peso (em kg): "))
# altura = float(input("Digite a altura (em m): "))
# imc = peso/altura**2
# if(imc < 18.6):
#     print("Baixo peso.")
# elif(imc < 25):
#     print("Peso ideal.")
# elif(imc < 30):
#     print("Sobrepeso")
# elif(imc < 35):
#     print("Obesidade grau 1")
# elif(imc < 40):
#     print("Obesidade grau 2")
# else:
#     print("Obesidade grau 3")
# print(f"Seu IMC eh {imc}")

# Pedra, papél e tesoura
# jogador = int(input("Escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))
# if(jogador > 3 or jogador < 0):
#     print("Valor inválido!")
# else:
#     computador = random.randint(1,3)
#     print("Computador escolheu: ", computador)
#     if(jogador == computador):
#         print("Deu empate!")
#     elif(jogador == 1):
#         if(computador == 2):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")
#     elif(jogador == 2):
#         if(computador == 3):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")
#     else:
#         if(computador == 1):
#             print("Computador ganhou! ")
#         else:
#             print("Jogador ganhou!")

# Pressão
# sist = int(input("Sistólica: "))
# diast = int(input("Diastólica: "))
# if(sist >= 180 or diast >= 120):
#     print("Crise Hipertensiva.")
# elif(sist >= 140 or diast >= 90):
#     print("Hipertensão Estágio 2.")
# elif(sist >= 130 or diast >= 80):
#     print("Hipertensão Estágio 1.")
# elif(sist >= 120):
#     print("Elevada.")
# else:
#     print("Normal.")

# Ano bissesto
# ano = int(input("Digite o ano: "))
# if(ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
#     print("Ano bissexto.")
# else:
#     print("Ano não é bissexto.")

# Ano bissexto nos dias do calendário
# mes = int(input("Digite o mês 1 - 12: "))
# ano = int(input("Digite o ano: "))
# if(mes>12 or mes<1):
#     print("Mês inválido")
# elif(mes == 2):
#     if(ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
#         dias = 29
#     else:
#         dias = 28
# elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
#     dias = 30
# else:
#     dias = 31
# print(f"Quantidade de dias no mês eh: {dias}")

# Calculo do salário liquido

# salBruto = float(input("Informe o salário bruto: "))
# qntDependentes = int(input("Quantidade de dependentes: "))
# INSS
# if(salBruto <= 1212):
#     if(salBruto*0.075 > 90.90):
#         inss = 90.90
#     else:
#         inss = salBruto*0.075
# elif(salBruto <= 2427.35):
#     if(salBruto*0.09 - 18.18 > 200.28):
#         inss = 200.28
#     else:
#         inss = salBruto*0.09 - 18.18
# elif(salBruto <= 3641.03):
#     if(salBruto*0.12 - 91.00 > 345.92):
#         inss = 345.92
#     else:
#         inss = salBruto*0.12 - 91.00
# else:
#     if(salBruto*0.14 - 163.82 > 828.39):
#         inss = 828.39
#     else:
#         inss = salBruto*0.14 - 163.82
# print("INSS: ", inss)
# IRRF
# irrf = salBruto - inss - 189.59*qntDependentes
# if(irrf < 1903.99):
#     irrf = 0
# elif(irrf <2826,66):
#     irrf = irrf * 1.075 - 142.80
# elif(irrf < 3751.05):
#     irrf = irrf * 1.150 - 354.80
# elif(irrf < 4664.68):
#     irrf = irrf * 1.225 - 636.16
# else:
#     irrf = irrf * 1.275 - 869.36
# print("IRRF: ", irrf)
# liquido = salBruto - inss - irrf
# print("Salário líquido: ", liquido)

# for
# de 0 a 9
# for cont in range(0,10):
#     print(cont)
# de 1 a 10
# for cont in range(1,11):
#     print(cont)
# de 10 a 1
# for cont in range(10,0,-1):
#     print(cont)
# de 1 10 pulando duas casas
# for cont in range(1,11,2):
#     print(cont)

# Raiz quadrada de 1 até 50
# for cont in range(1, 51):
#     print(f"{cont:2}: {math.sqrt(cont):.3f}")

# Somatório de uma range
# soma = 0
# num = int(input("Num: "))
# for cont in range(1,num+1):
#     soma = soma + cont
# print(f"Soma: {soma}")

# Metodo de Heron
# num = float(input("Numero: "))
# raizAprox = 1
# for cont in range(1,100):
#     if (abs(raizAprox - (raizAprox+(num/raizAprox))/2) < 0.00001):
#         print(f"{cont:6}: {raizAprox:.3f}")
#         break
#     raizAprox = (raizAprox+(num/raizAprox))/2
#     print(f"{cont}:{raizAprox}")

# Média altura pessoas
# soma = 0
# for cont in range(1,4):
#     altura = float(input(f"Digite a altura da pessoa {cont}: "))
#     soma = soma + altura
# print(f"Média das alturas: {soma/3:.2f}")

# Identificar a maior altura
# maior = 0
# for cont in range(1,11):
#     altura = random.uniform(1.5,2)
#     if altura > maior:
#         maior = altura
#         print(f"Maior: {maior}")
# print(f"Maior altura: {maior:.3f}")

# Estatistica alunos
# sumIdade = 0
# qntAlunos = 0
# maior = 0
# for cont in range(50):
#     idade = random.randint(18, 60)
#     semestre = random.randint(1, 10)
#     curso = random.choice(["ADS", "Engenharia", "Física"])
#     sumIdade = sumIdade + idade
#     if (semestre == 5):
#         qntAlunos += 1
#     if (idade > maior):
#         maior = idade
#         cursoVeio = curso
# print(f"Média idades: {sumIdade/50}")
# print(f"Curso do aluno mais velho: {cursoVeio}, com {maior} anos.")
# print(f"Quantidade de alunos no quinto semestre: {qntAlunos}")

# Manipulando string
# frase = "Esta é uma string"
# final = frase[:5] + "E" +frase[6:]
# print(final)
# for cont in range(0,17):
#     print(f"{cont}, {frase[cont]}")

# Ordem em strings
# frase1 = "Teste"
# frase2 = "teste"
# if(frase1 < frase2):
#     print(frase1, frase2)
# elif(frase2 < frase1):
#     print(frase2, frase1)
# else:
#     print("São iguais:", frase1, frase2)

# Contém
# frase1 = "teste"
# frase2 = "Isso é apenas um teste"
# if frase1 in frase2:
#     print("Verdade!")

# Palíndromo - 1
# palavra = str(input("Digite a palavra: "))
# for cont in range(len(palavra)):
#     if(palavra[cont] != palavra[-cont-1]):
#         print("Não é palindromo.")
#         break
#     elif(len(palavra) == cont+1):
#         print("É palíndromo")
# print(palavra)
# print(palavra[::-1])

# Palíndromo - 2
# palavra = str(input("Digite a palavra: "))
# if palavra != palavra[::-1]:
#     print("Não é palíndromo.")
# else:
#     print("É palíndromo")

# Detectar vogais
# vogais = "aeiouAEIOU"
# conta = 0
# palavra = str(input("Digite a palavra: "))
# for letra in palavra:
#     if letra not in vogais:
#         conta += 1
# print(conta)

# Senha forte - 1
# maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# minusculas = "abcdefghijklmnopqrstuvwxyz"
# numeros = "0123456789"
# maiuscula = False
# especial = False
# numero = False
# senha = str(input("Digite sua senha: "))
# for digito in senha:
#     if(digito in maiusculas):
#         maiuscula = True
#     if(digito in numeros):
#         numero = True
#     if(digito not in maiusculas and digito not in minusculas and digito not in numeros):
#         especial = True
# if(maiuscula == True and numero == True and especial == True):
#     print("Senha forte!")
# else:
#     print("Senha fraca!")

# Senha forte 2
# maiuscula = False
# numero = False
# pontuacao = False
# senha = str(input("Digite sua senha: "))
# for digito in senha:
#     if digito in string.ascii_uppercase:
#         maiuscula = True
#     if digito in string.digits:
#         numero = True
#     if digito not in string.digits and digito not in string.ascii_letters:
#         pontuacao = True
# if maiuscula == False or numero == False or pontuacao == False:
#     if maiuscula == False:
#         print("Erro: Senha inválida. Não possui letras maiusculas.")
#     if numero == False:
#         print("Erro: Senha inválida. Não possui numeros.")
#     if pontuacao == False:
#         print("Erro: Senha inválida. Não possui caractere especial.")
# else:
#     print("Senha forte!")

# Iniciais dos nomes
# nome = str(input("Digite seu nome: "))
# iniciais = ""
# for indice in len(nome):
#     if indice == 0:
#         iniciais += nome[indice] + ". "
#     elif nome[indice] == " ":
#         iniciais += " " + nome[indice+1] + "."
# print(iniciais)

# Adivinhar número
# numero = random.randint(1,100)
# for cont in range(10):
#     chute = int(input(f"Chute nº {cont+1}: "))
#     if chute == numero:
#         print("Acertou!!")
#         break
#     elif chute < numero:
#         print("O nomero é maior que o chute.")
#     elif chute > numero:
#         print("O nomero é menor que o chute.")
# print("Fim de jogo. Numero sorteado: ",numero)

# Estatistica
# mediaRenda = 0
# mediaIdadeQnt3filhos = 0
# Qnt3Filhos = 0
# mediaFilho = 0
# mediaHomensIdade = 0
# homemMaisVelho = 0
# rendaHomemMaisVelho = 0
# mulherMaiorRenda = 0
# idadeMulherMaiorRenda = 0
# for cont in range(2000):
#     idade  = random.randint(18,90)
#     renda  = random.randrange(1000,10000)
#     sexo  = random.choice(["Homem","Mulher"])
#     numFilhos = random.randint(0,5)
#     mediaRenda += renda
#     mediaFilho += numFilhos
#     if(numFilhos > 3):
#         mediaIdadeQnt3filhos += idade
#         Qnt3Filhos += 1
#     if(idade<30 and sexo == "Homem"):
#         mediaHomensIdade += 1
#     if idade > homemMaisVelho and sexo == "Homem":
#         homemMaisVelho = idade
#         rendaHomemMaisVelho = renda
#     if renda > mulherMaiorRenda and sexo == "Mulher":
#         mulherMaiorRenda = renda
#         idadeMulherMaiorRenda = idade
# print(  "Media renda: ", mediaRenda/(cont+1),
#       "\nMedia idade quem tem mais de 3 filhos: ", mediaIdadeQnt3filhos//Qnt3Filhos,
#       "\nQuantidade de homens com menos de 30 anos:", mediaHomensIdade,
#       "\nMedia numero de filhos:", mediaFilho//(cont+1),
#       "\nRenda do homem mais velho: ", rendaHomemMaisVelho,
#       "\nIdade da mulher com maior renda: ", idadeMulherMaiorRenda,"\n")

# Fatorial
# num = int(input("Digite um valor: "))
# fatorial = num
# if num == 0:
#     print(num+1)
# elif num < 0:
#     print("Número negativo.")
# else:
#     while num > 2:
#         fatorial = fatorial * (num-1)
#         num -= 1
#     print("Fatorial: ",fatorial)

# Divisores
# num = int(input("Digite um valor: "))
# aux = num
# if num <= 0:
#     print("O valor precisa ser maior que 0.")
# else:
#     while aux > 0:
#         if num%aux == 0:
#             print(aux)
#         aux -= 1

# Numeros primos
# num = int(input("Digite um valor: "))
# aux = 1
# cont = 0
# if num < 0:
#     print("Valor deve ser positivo.")
# else:
#     while aux <= num:
#         if num%aux == 0:
#             cont += 1
#         if cont >= 3:
#             print("O número não é primo.")
#             break
#         aux += 1
#     if cont == 2:
#         print("O número é primo.")

# Calculo termos
# num = int(input("Quantos termos? "))
# if num <= 0:
#     print("Numero inválido.")
# else:
#     aux = 1
#     termo = 0
#     while aux <= num:
#         termo = termo + 1/aux
#         aux += 1
#     print("Soma dos termos: ", termo)

# Calculo termos 2
# num = int(input("Quantos termos? "))
# aux = 1
# termo = 0
# if num <= 0: print("Número inválido!")
# else:
#     while aux <= num:
#         termo += aux*2/(aux*2-1)
#         print(termo)
#         aux += 1
#     print(termo)

# Numero perfeito
# num = int(input("Digite o número: "))
# aux = 1
# soma = 0
# while num <= 0:
#     num = int(input("Numero inválido, digite novamente: "))
# while aux <= num/2:
#     if num%aux == 0:
#         print(aux)
#         soma += aux
#     aux += 1
# print("Soma: ", soma)
# if soma == num:
#     print("Numero perfeito!")
# else:
#     print("O número não é perfeito...")

# Zé e chico
# ze = 110
# chico = 150
# anos = 0
# while ze <= chico:
#     ze += 3
#     chico += 2
#     print("- ",ze, chico)
#     anos += 1
# print(f"Levou {anos} anos para o Zé ficar maior que o Chico.")

# Par e números primos
# vezes = int(input("Quantos numeros? "))
# contVezes = 1
# num = 4
# while contVezes <= vezes:
#     met1 = num//2
#     met2 = met1
#     while met1 <= met2:
#         aux = 1
#         contMet1 = 0
#         while aux <= met1:
#             if met1%aux == 0: contMet1 += 1
#             aux +=1
#         if contMet1 == 2:
#             aux = 1
#             contMet2 = 0
#             while aux <= met2:
#                 if met2%aux == 0: contMet2 += 1
#                 aux += 1
#             if contMet2 == 2:
#                 print("\nNumero: ",num,
#                     "\ndivisores primos: ", met1, met2)
#                 break
#         met1 -= 1
#         met2 += 1
#     num += 2
#     contVezes += 1

# Fatorial
# for num in range(0, 10):
#     total = 1
#     aux = 2
#     while aux <= num:
#         total = total * aux
#         aux += 1
#     print("Fatorial do número", num, ": ", total)

# Intervalo de numeros
# print("Digite um valor negativo para sair do programa.")
# intervalo1 = 0
# intervalo2 = 0
# intervalo3 = 0
# intervalo4 = 0
# total = 0
# while True:
#     num = int(input("Digite o valor: "))
#     if num < 0:
#         break
#     else:
#         total += 1
#         if num>=0 and num<=25:
#             intervalo1 += 1
#         elif num <= 50:
#             intervalo2 += 1
#         elif num <= 75:
#             intervalo3 += 1
#         elif num <=100:
#             intervalo4 += 1
# print("[0;25]:", intervalo1,
#       "\n[26;50]:", intervalo2,
#       "\n[51;75]:", intervalo3,
#       "\n[76;100]:", intervalo4,
#       "\nQuantidade total de valores: ", total)

# Funções
# def imc(peso, altura):
#     return peso / altura ** 2
# p = float(input("Digite o peso: "))
# a = float(input("Digite a altura: "))
# print(f"IMC: {imc(p, a)}")

# Funções 2
# def ehprimo(valor):
#     for i in range(2,valor//2+1):
#         if valor%i == 0:
#             return False
#     return True
# v = int(input("Digite um valor par maior que 2: "))
# while v <= 2:
#     v = int(input("Erro! Digite um valor par maior que 2: "))
# div1 = v//2
# div2 = div1
# while ehprimo(div1) == False or ehprimo(div2) == False:
#     div1 -= 1
#     div2 += 1
# print("Para o número: ", v)
# print("Os primos são: ", div1,div2)

# Funções 3
# def ehprimo(valor):
#     for i in range(2,valor//2+1):
#         if valor%i == 0:
#             return False
#     return True
# def goldbach(numero):
#     for v1 in range(2, numero):
#         v2 = numero - v1
#         if ehprimo(v1) and ehprimo(v2):
#             return v1, v2
# for i in range(4,102,2):
#     primo1, primo2 = goldbach(i)
#     print(f"Para o valor {i}, os primos são: {primo1} + {primo2}")

# Distância entre dois pontos
# def distancia(x1,y1,x2,y2):
#     deltax = x1-x2
#     deltay = y1-y2
#     dist = math.sqrt(deltax**2 + deltay**2)
#     return dist
# x1 = float(input("x1: "))
# y1 = float(input("y1: "))
# x2 = float(input("x2: "))
# y2 = float(input("y2: "))
# print(f"A distância eh: {distancia(x1,y1,x2,y2):0.5f}")

# Coeficiente Binomial
# def fatorial(n):
#     """Realiza o fatorial de um número"""
#     if n < 0:
#         return 0
#     total = 1
#     for i in range(2, n+1):
#         total = i * total
#     return total

# Coeficiente Binomial2
# def binomial(n, k):
#     return fatorial(n)//(fatorial(k)*fatorial(n-k))

# Coeficiente Binomial3
# def binomial2(n, k):
#     prod = 1
#     total = k
#     if n-k < k:
#         total = n-k
#     for i in range(1, total+1):
#         prod = prod * ((n+1-i)/i)
#     return int(prod)

# Triangulo de pascal
# def triangulo(n):
#     for i in range(n):
#         for e in range(i+1):
#             print(binomial2(i, e), end="")
#         print()
# print(timeit.timeit("triangulo(10)", globals=globals(), number=1))
# print(timeit.timeit("triangulo2(10)", globals=globals(), number=1,))


# Jogo da forca
# def verifica(let, palav):
#     """Verifica se a palavra contém a letra e retorna as coordenadas de onde estão"""
#     posEncontrado = ""
#     for l in range(len(palav)):
#         if let == palav[l]:
#             posEncontrado = posEncontrado + str(l)
#     return posEncontrado
# def atualiza(let, pos, desc):
#     """Atualiza e retorna a string descoberto utilizando as coordenadas passadas pela função verifica"""
#     for p in pos:
#         desc = desc[:int(p)] + let + desc[int(p)+1:]
#     return desc
# vida = 5
# palavra = "amora"
# descoberto = len(palavra) * "-"
# coord = ""
# historico = []
# string.ascii_lowercase
# print(f"Jogo da forca\nVocê possui {vida} vidas")
# while vida > 0:
#     print("Palavra: ", descoberto)
#     print("Letras já escolhidas: ", historico)
#     letra = str(input("Digite uma letra para o chute: "))

#     #Verifica a entrada de valor não alfabeticos e entradas maiores que uma letra
#     while letra not in string.ascii_letters or len(letra) > 1 or len(letra) == 0:
#         print("Digite somente uma letra!")
#         letra = str(input("Digite uma letra para o chute: "))
#     #Verifica se o usuário já digitou a letra
#     while letra in historico: 
#         letra = str(input("Você já digitou essa letra! Escolha novamente: "))
#     letra = letra.lower()
#     historico.append(letra)
#     coord = verifica(letra, palavra)
#     if coord == "":
#         vida -= 1
#         print("Errou!\nVidas: ",vida)
#     else:
#         descoberto = atualiza(letra, coord, descoberto)
#         print("Acertou!")
#         if "-" not in descoberto:
#             print("Você ganhou!\nPalavra: ",palavra)
#             exit()
# print("Você perdeu! Tente novamente.")
# print("Palavra:",palavra)

