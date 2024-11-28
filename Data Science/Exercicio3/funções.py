import statistics as st
from tela import *

def moda(lista):
    
    moda = st.mode(lista)

    print(f"Sua moda é {moda}")

def media(lista):
    
    media = st.mean(lista)

    print(f"Sua média é {media}")

def mediana(lista):


    mediana = st.median(lista)

    print(f"Sua mediana é {mediana}")
    
def desvio(lista):


    desvio = st.stdev(lista)
    
    print(f"Seu desvio é {desvio}")
    
def amplitude(lista):
    
    amplitude = max(lista) - min(lista)
    
    print(f"Sua amplitude é {amplitude}")
    
def variancia(lista):

    variancia = st.variance(lista)
    
    print(f"Sua variancia é {variancia}")