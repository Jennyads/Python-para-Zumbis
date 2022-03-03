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

contem = []
for x in texto:
    if x[0] in  'python' or x[-1] in 'python':
        contem.append(x)

print('Contém em Python:', contem)
    
