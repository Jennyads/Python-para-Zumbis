texto = ''' 
The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you '''

texto = texto.lower()
texto = texto.replace(',', ' ').replace('.', ' ').replace(':',' ')
texto = texto.split()

palavras = []
for x in texto:
    for letra in x:
         if letra in 'python' and len(x) > 4:
             palavras.append(x)
             break
print(palavras)
print(len(palavras))


ou

texto = ''' 
The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you '''

texto = texto.lower()
texto = texto.replace(',', ' ').replace('.', ' ').replace(':',' ')
texto = texto.split()

def é_python(p):
    if len(p) <=4: return False
    for c in p:
        if c in 'python': return True
    return False
lista = []
for p in texto:
    if é_python(p):
        lista.append(p)
print(lista)
print(len(lista))
