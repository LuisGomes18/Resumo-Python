# Resunmo feito por Luís Gomes
# Este resumo server para relembrar de alguma coisa.
#? Import dos modulos usados
import random

 #? Para definir as def's
def acertou():
  print("Acertas-te \n")
def errou():
  print("Erras-te \n")


#? Apresentação com a pessoa
nome = input("Qual seu nome? ") 
print(f'Seja bem-vindo {nome} muito gosto em te conheçer')
print('Bora começar por maténatica \n')

score = 0
#? Perguntas de soma (básico)
n1 = int(random.uniform(0, 9))
n2 = int(random.uniform(0, 9))
total = n1 + n2
perg0 = float(input('{:.0f}+{:.0f}= '.format(n1, n2)))
if perg0 == total:
    acertou()
    score +=1
else:
    errou()

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(10, 99))
n2 = int(random.uniform(10, 99))
total = n1 + n2
perg1 = float(input('{:.0f}+{:.0f}= '.format(n1, n2)))
if perg1 == total:
    acertou()
    score +=1
else:
    errou()

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(100, 999))
n2 = int(random.uniform(100, 999))
total = n1 + n2
perg2 = float(input('{:.0f}+{:.0f}= '.format(n1, n2)))
if perg2 == total:
    acertou()
    score +=1
else:
    errou()

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(1000, 9999))
n2 = int(random.uniform(1000, 9999))
total = n1 + n2
perg3 = float(input('{:.0f}+{:.0f}= '.format(n1, n2)))
if perg3 == total:
    acertou()
    score +=1
else:
    errou()


#? Perguntas da subtrações
print('\n Perguntas de subtração')
total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(0, 9))
n2 = int(random.uniform(0, 9))
total = n1 - n2
perg00 = float(input('{:.0f}-{:.0f}= '.format(n1, n2)))
if perg00 == total:
    acertou()
    score +=1
else:
    errou()

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(10, 99))
n2 = int(random.uniform(10, 99))
total = n1 - n2
perg00 = float(input('{:.0f}-{:.0f}= '.format(n1, n2)))
if perg00 == total:
    acertou()
    score +=1
else:
    errou()   

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(100, 999))
n2 = int(random.uniform(100, 999))
total = n1 - n2
perg00 = float(input('{:.0f}-{:.0f}= '.format(n1, n2)))
if perg00 == total:
    acertou()
    score +=1
else:
    errou()    

total = 0
n1 = 0
n2= 0
n1 = int(random.uniform(1000, 9999))
n2 = int(random.uniform(1000, 9999))
total = n1 - n2
perg00 = float(input('{:.0f}-{:.0f}= '.format(n1, n2)))
if perg00 == total:
    acertou()
    score +=1
else:
    errou()     

print('\n****************************  SCORE  ******************************************')
print('                                                                                ')
print(f'                    O total da sua pontuação é {score}                         ')
print('                                                                                ')
print('*******************************************************************************')      