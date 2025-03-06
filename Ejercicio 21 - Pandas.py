import pandas as pd
lista = ["300", "200", "conejo", "90", "perro", "500"]

pf = pd.Series(lista)
print (pf)
#Muestra los datos no numericos como NaN

pf = pd.to_numeric(pf, errors = "coerce")

print (pf)

print (pf.hasnans)

#Solo muestra datos numericos y descarta los valores NaN
lista = pf.dropna()
print (lista)
