import statistics as st

def moda(freq):

    moda = st.mode(freq)

    print(moda)

def media(freq):
    
    media = st.mean(freq)

    print(media)

def mediana(freq):
    
    mediana = st.median(freq)

    print(mediana)
