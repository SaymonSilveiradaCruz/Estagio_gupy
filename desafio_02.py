# Definindo a string
minha_string = "Abracadabra"

# Contando as ocorrências de 'a' e 'A'
contagem_a = minha_string.count('a') + minha_string.count('A')

# Verificando a existência e imprimindo o resultado
if contagem_a > 0:
    print(f"A letra 'a' aparece {contagem_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
