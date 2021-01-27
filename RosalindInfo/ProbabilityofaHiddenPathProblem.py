hiddenPath = input('Hidden Path input: ')
states = input('States input: ')
transitions = []

startProb = [0.5, 0.5, 0.5, 0.5]

aux = []
for i in range(0,2):
    x = input('Linha 1 - Coluna ' + str(i) + ': ')
    y = input('Linha 2 - Coluna ' + str(i) + ': ')
    aux.append(x)
    aux.append(y)
    transitions.append(aux)
    aux=[]

for letter in hiddenPath:
           