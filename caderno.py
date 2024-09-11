from folium.plugins import MarkerCluster
import folium.map
import folium
import math
import random
import string
import timeit
import matplotlib.pyplot as plt

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
# historico = ""
# string.ascii_lowercase
# print(f"Jogo da forca\nVocê possui {vida} vidas")
# while vida > 0:
#     print("Palavra: ", descoberto)
#     print("Letras já escolhidas: ",historico)
#     letra = str(input("Digite uma letra para o chute: "))
#     #Verifica a entrada de valor não alfabeticos e entradas maiores que uma letra
#     while letra not in string.ascii_letters or len(letra) > 1 or len(letra) == 0:
#         print("Digite somente uma letra!")
#         letra = str(input("Digite uma letra para o chute: "))
#     #Verifica se o usuário já digitou a letra
#     while letra in historico:
#         letra = str(input("Você já digitou essa letra! Escolha novamente: "))
#     letra = letra.lower()
#     historico += letra
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

# Utilização de listas
# lista = []
# contaPar = 0
# for i in range(30):
#     lista.append(random.randint(1,500))
# maior = lista[0]
# for i in lista:
#     if i > maior: maior = i
#     if i%2==0: contaPar += 1
# print(lista)
# print(len(lista))
# print("Maior: ", maior)
# print("Pares: ", contaPar)

# Utilização de listas 2
# lista = []
# for i in range(30):
#     lista.append(random.randint(1,50))
# print(lista)
# print(lista.count(1))
# print(sum(lista))
# print(min(lista))
# print(max(lista))
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

# Listas notas dos alunos
# notas = []
# acimaDaMedia = 0
# abaixoDaMedia = 0
# for i in range(15):
#     notas.append(random.randint(0,10))
# media = sum(notas)//len(notas)
# for i in notas:
#     if i > media:
#         acimaDaMedia += 1
#     elif i < media:
#         abaixoDaMedia += 1
# print(notas)
# print("Media: ", media)
# print("Acima: ",acimaDaMedia)
# print("Na media: ", notas.count(media))
# print("Abaixo: ", abaixoDaMedia)
# print("Menor nota: ",min(notas))
# print("Maior nota: ",max(notas))

# Votação gestor
# avaliacao = []
# for i in range(25):
#     avaliacao.append(random.randint(1, 5))
# lValores = []
# lConceito = ["Excelente", "Bom", "Regular", "Ruim", "Péssimo"]
# lValores = [avaliacao.count(5)] + [avaliacao.count(4)] + \
#     [avaliacao.count(3)] + [avaliacao.count(2)] + [avaliacao.count(1)]
# maiorVal = lValores[0]
# MaiorConc = lConceito[0]
# for i in range(5):
#     print(lConceito[i], "-", lValores[i])
#     if lValores[i] > maiorVal:
#         maiorVal = lValores[i]
#         MaiorConc = lConceito[i]
# print("Maior: ", maiorVal, MaiorConc)

# Calculo idades
# idades = []
# for i in range(20):
#     idades.append(random.randint(1,100))
# print("Maior idade",max(idades))
# print("Menor idade",min(idades))
# print("Media", sum(idades)/len(idades))

# 10 maiores valores
# valores = []
# lOrdenada = []
# for i in range(30):
#     valores.append(random.randint(0,100))
# lOrdenada = valores
# lOrdenada.sort()
# lOrdenada.reverse()
# print(lOrdenada[:10])

# Calculo Jogadores
# jogadores = []
# estatistica = []
# for i in range(5):
#     nome = input(f"Digite o nome do jogador {i}:" )
#     pontos = random.randint(0,100)
#     asssitencias = random.randint(0,100)
#     rebotes = random.randint(0,100)
#     jogadores.append((nome, pontos, asssitencias, rebotes))
# for j in jogadores:
#     soma = 0
#     for d in range(1,4):
#         soma += j[d]
#     estatistica.append((j[0],soma/3))
# melhor = estatistica[0]
# for item in estatistica:
#     if item[1] > melhor[1]:
#         melhor = item
# print(melhor)

# Peças vendidas - utilizando tuplas
# vendas = []
# tamanhos = []
# cores = []
# catTamanhos = ("P", "M", "G")
# catCores = ("Branco", "Preto", "Azul")
# for peca in range(50):
#     tamanho = random.sample(catTamanhos, k=1)[0]
#     cor = random.sample(catCores, k=1)[0]
#     tamanhos.append(tamanho)
#     cores.append(cor)
#     vendas.append((tamanho, cor))
# somaTamanhos = \
#     tamanhos.count("P"), tamanhos.count("M"), tamanhos.count("G")
# print(catTamanhos, "\n", somaTamanhos)
# somaCores = \
#     cores.count("Branco"), cores.count("Preto"), cores.count("Azul")
# print(catCores, "\n", somaCores)
# print()
# print("O tamanho mais vendido foi: ", catTamanhos[somaTamanhos.index(
#     max(somaTamanhos))], somaTamanhos[somaTamanhos.index(max(somaTamanhos))])
# print(f"Foram vendidas {somaTamanhos[1]} para o tamanho M")
# print("Cor mais vendida: ",catCores[somaCores.index(max(somaCores))])

# Introdução a arquivos
# Motivos para abrir o arquivo: r = leitura; w = gravação; a = alteração append
# arq = open("direção arquivo", "r")
# Abrir para gravar: variavelArquivo.write(item)k
# arq = open("direção arquivo", "w") - Zera o arquivo para inserir os conteúdos
# for para percorrer o documento
# split para separar em listas
# Fechar o arquivo com arq.close()

# def gravacao():
#     arq = open("Faculdade\\Exercicios-Programas-Python\\altura.txt", "w")
#     arq.write("Nome - Altura\n")
#     for i in range(5):
#         nome = input("Digite um nome: ")
#         altura = random.randint(150,200)/100
#         arq.write(nome + ' - ' + str(altura) + "\n")
#     arq.close()
# def leitura():
#     alunos = []
#     arq = open("Faculdade\\Exercicios-Programas-Python\\altura.txt", "r")
#     arq.readline()
#     for i in arq:
#         linha = i[:-1].split(" - ")
#         alunos.append((linha[0],float(linha[1])))
#     arq.close()
#     return alunos
# gravacao()
# listaAlunos = leitura()
# maisAlto = ""
# altMaisAlto = 0
# somaAltura = 0
# for i in listaAlunos:
#     if i[1] > altMaisAlto:
#         maisAlto = i[0]
#         altMaisAlto = i[1]
#     somaAltura += i[1]
# print(f"Nome do mais alto: {maisAlto}, com {altMaisAlto}m")
# print(f"Media das alturas: {(somaAltura/len(listaAlunos)):0.2f}")

# Listas aninhadas e abrangencia de listas
# lista = [item+1 for item in range(10)]
# quadrados = [item**2 for item in lista]
# print(quadrados)
# quadrados2 = [item**2 for item in lista if item%2==0]
# print(quadrados2)
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriz)
# matriz[0][0] = 15
# print(matriz)

# Segmentando frases
# frases = ["Eu estudo na puc", "O sol nasceu", "Deitei na cama"]
# tokens = []
# for i in frases:
#     tokens.append(i.split())
# print(tokens)
# for i in tokens:
#     print("Frase: ", i)
#     for e in i:
#         print(e)

# Gráficos
# plt.plot([2,4,9,16],[1,2,3,4])
# plt.show()
# listax = [item for item in range(11)]
# listay = [item**2 for item in range(11)]
# listay2 = [item**3 for item in range(11)]
# plt.plot(listax, listay, 'b-', label="$x^2$")
# plt.plot(listax, listay2, 'r-', label="$x^3$")
# plt.title("$x^2$ e $x^3$")
# plt.legend()
# plt.show()
# anos = [a for a in range(1990, 2011)]
# valores = [random.randint(100, 1500) for v in range(len(anos))]
# plt.bar(anos, valores)
# # Realiza as divisões dos valores apresentaveis
# plt.xticks(range(1990, 2011, 2))
# plt.show()
# random.seed(42)
# valores = [random.randint(0, 11) for item in range(0, 100)]
# x = [item+0.5 for item in range(0, 11)]
# plt.hist(valores, x)
# print(x)
# print(valores)
# plt.show()

# Biblioteca folium gera mapas interativos, interessante para mostrar
# Latitudes e longitudes
# import folium

# Dicionarios
# dic = {}
# dic["Fulano"] = "99817-9123"
# dic["Beltrano"] = "99671-7562"
# dic["Ciclano"] = "99881-1642"
# del dic["Fulano"]
# nome = ""
# while nome != "fim":
#     print(dic.keys(), "\n",
#           dic.values(), "\n",
#           dic.items(), "\n",
#           dic.get("Fulano"))
#     nome = input("Nome para procurar (Digite fim para sair)")
#     if nome != "fim":
#         if nome in dic:
#             print(f"Telefone: {dic[nome]}")
#         else:
#             print("Nome não encontrado!")

# Operações de acesso aos dicionários
# dic = {}
# dic["Fulano"] = "99817-9123"
# dic["Beltrano"] = "99671-7562"
# dic["Ciclano"] = "99881-1642"
# print(dic.keys(), "\n",
#           dic.values(), "\n",
#           dic.items(), "\n",
#           dic.get("Fulano"))
# for k in dic.keys():
#     print(f"Chave: {k}")
# for v in dic.values():
#     print(f"Valor: {v}")
# print("Chaves e valores em ordem de inclusão: ")
# for k, v in dic.items():
#     print(f"{k:8} -> {v}") #{k:8} aumenta a quantidade de caracteres para deixar no mesmo tamanho.
# print("Ordenado pelas chaves: ")
# for k,v in sorted(dic.items()):
#     print(f"{k:8} -> {v}")
# print("Ordenado pelos valores: ")
# for k,v in sorted(dic.items(), key=lambda x: x[1]):
#     print(f"{k:8} -> {v}")
#     print (lambda x:x[0])
#     print (lambda x:x[1])

# Conjuntos
# conj1 = set()
# conj2 = {2,4,6,8}
# # Operações:
# # conj1.add(elem)
# # conj1.remove(elem)
# # conj1.pop()
# # conj1.clear()
# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(a)
# print(b)
# # a | b:
# print("uniao:", a.union(b))
# # a & b:
# print("Intersecção:", a.intersection(b))
# # a - b:
# print("Diferença:", a.difference(b))
# # a ^ b : Sem os elementos comuns
# print("Sem os elementos em comum:", a.symmetric_difference(b))

# print(a.isdisjoint(b)) # True se A e B não tem elementos em comum
# print(a.issubset(b)) # True se B contém todos os elementos de A
# print(a.issuperset(b)) # True se B está contido em A

# Busca de letras em um texto
# frase = input("Texto: ").lower()
# frase = "texte de texto"
# hist = {}
# alphabet = set(string.ascii_lowercase)
# for l in frase:
#     if l not in hist and l != " ":
#         hist[l] = frase.count(l)
# usadas = set(hist.keys())
# for chave in sorted(hist.keys()):
#     print(f"{chave} -> {hist[chave]}")
# print("Letras utilizadas: ")
# print(sorted(usadas))
# print("Letras não utilizadas: ")
# print(sorted(alphabet.difference(usadas)))

# import nltk
# nltk.download("stopwords")
# stopwords = nltk.corpus.stopwords.words('portuguese')
# freq = {}
# print(pontuacao)
# file = open(
#     "Faculdade\\Exercicios-Programas-Python\\domcasmurro.txt", encoding="utf8")
# content = file.readlines()
# content = content[61:]
# for linha in content:
#     linha = linha.lower()[:-1]
#     for pont in string.punctuation:
#         linha = linha.replace(pont, "")
#     for palavra in linha.split(" "):
#         if len(palavra) < 3 or palavra in stopwords:
#             continue
#         if palavra not in freq:
#             freq[palavra] = 0
#         freq[palavra] += 1
# for x, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:30]:
#     print(f"{x:3} -> {v}")

# Função lambda
# lista = ["A", "b", "Roxo", "azul", "Preto", "l", "124"]
# print(lista)
# print(sorted(lista))
# print(sorted(lista, key=lambda x: x.lower()))

# Trabalhando com dados
# unidades = {}
# with open("Faculdade\\Exercicios-Programas-Python\\Unidades_Basicas_Saude-UBS.csv") as csv:
#     csv.readline()
#     for linha in csv:
#         aux = linha[:-1].split(";")
#         lat = aux[6]
#         lon = aux[7]
#         uf = aux[1]
#         if lat != '' and lon != '' and uf == "43":
#             nome = aux[3][1:-1]
#             logr = aux[4][1:-1]
#             bairro = aux[5][1:-1]
#             lat = float(lat.replace(",", "."))
#             lon = float(lon.replace(",", "."))

#             unidades[nome] = (logr, bairro, lat, lon)
# ubs = input("Digite o nome da unidade: ").upper()
# if ubs in unidades:
#     print(unidades[ubs])
# else:
#     for nome in unidades.keys():
#         if ubs in nome:
#             print("Unidade encontrada: ", nome, unidades[nome])
# map = folium.Map(location=[-40.161034, -52.098611], zoom_start=6, min_zoom=5)
# marker_cluster = MarkerCluster().add_to(map)
# for aux in unidades.values():
#     folium.CircleMarker(radius=1, location=[
#                         aux[2], aux[3]]).add_to(marker_cluster)
# map.show_in_browser()

# Simulação de lançamento
# g = 9.80665
# x = 0
# ang = float(input("Digite o angulo: "))
# y0 = float(input("Digite a altura inicial: "))
# v = float(input("Digite a velocidade inicial (m/s): "))
# y = y0
# listaX = []
# listaY = []
# ang = math.radians(ang)
# while y >= 0:
#     if x != 0:
#         listaX.append(x)
#         listaY.append(y)
#     y = x*math.tan(ang) - ((1/(2*v**2)) * ((g*x**2)/(math.cos(ang)**2))) + y0
#     x += 0.1
# plt.ylabel("Altura")
# plt.xlabel("Distancia")
# plt.plot(listaX, listaY, "bo")
# plt.show()

# Fibonacci
def fibo(n):
    num1 = 1
    num2 = 1
    aurea = (1 + math.sqrt(5))/2
    print(num1)
    for i in range(n):
        print(f"{num1}")
        num2, num1 = num1, num1 + num2


fibo(100)
