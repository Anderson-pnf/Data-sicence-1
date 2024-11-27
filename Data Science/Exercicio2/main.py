from funções import *

freq = {
"empresa1": [900,6000,1200,8000,1400],
"empresa2": [5000,4000,3000,2000,7000],
"empresa3": [1200,1300,8000,3000,15000],
"empresa4": [1400,1200,1600,4500,5900],
"empresa5": [1400,1750,2000,4500,1000]}

empresa = int(input(f'''Diga qual empresa você deseja fazer uma verificação:
    Empresa 1 - {freq["empresa1"]}
    Empresa 2 - {freq["empresa2"]}
    Empresa 3 - {freq["empresa3"]}
    Empresa 4 - {freq["empresa4"]}
    Empresa 5 - {freq["empresa5"]}
    >>> '''))

dados = []
 
if empresa == 1:
    dados = freq["empresa1"]
    
elif empresa == 2:
    dados = freq["empresa2"]
    
elif empresa == 3:
    dados = freq["empresa3"]

elif empresa == 4:
    dados = freq["empresa4"]

elif empresa == 5:
    dados = freq["empresa5"]
else:
    print("Opção inválida!")
    

variancia(dados)
amplitude(dados)
desvio(dados)
moda(dados)
media(dados)
mediana(dados)

