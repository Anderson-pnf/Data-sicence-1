
def moda(freq):
    
    x = len(freq)+1
    y = 2
    z = x/y
    print(z)
        
def mediana(freq):
    
    if len(freq) != 3:
        x = len(freq) // 2
        print(x)
    else:
        x = len(freq) // 2 + 1
        y = len(freq) // 2
        z = ((x + y) / 2)
        print(z)

    
def media(freq):
    
    x = sum(freq)/len(freq)
    print(x)