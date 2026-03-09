#Definimos o dicionario ( Base de dados)
preço_frutas = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.00,
}

#definimos qual fruta queremos procurar
fruta_desejada = 'banana' 

#Fazemos a busca direta  usando o método get()
# O .get() tenta encontrar a fruta; se não achar, mostra 'frita não encontrada'
resultado = preço_frutas.get(fruta_desejada, 'fruta não encontrada')    

#Exibimos o resultado
print(f"O preço da {fruta_desejada} é: R${resultado}")
