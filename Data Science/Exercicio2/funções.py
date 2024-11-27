import statistics as st

def moda(dados):

    moda = st.mode(dados)

    print(f"Sua moda é {moda}")

def media(dados):
    
    media = st.mean(dados)

    print(f"Sua média é {media}")

def mediana(dados):
    
    mediana = st.median(dados)

    print(f"Sua mediana é {mediana}")
    
def desvio(dados):
    
    desvio = st.stdev(dados)
    
    print(f"Seu desvio é {desvio}")
    
def amplitude(dados):
    
    amplitude = max(dados) - min(dados)
    
    print(f"Sua amplitude é {amplitude}")
    
def variancia(dados):
    
    variancia = st.variance(dados)
    
    print(f"Sua variancia é {variancia}")