ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Encontra o índice do elemento a ser substituído e faz a substituição
# O método index() retorna o índice do primeiro elemento com o valor especificado
index = ft_list.index('tata!')
ft_list[index] = 'World!'
# Outra forma de substituir 'tata!' por 'World!' usando compreensão de lista
# ft_list = ['World!' if item == 'tata!' else item for item in ft_list]

# A tupla é imutável, então é necessário converter a tupla em uma lista para fazer a substituição
# Converte a tupla em uma lista
ft_list_from_tuple = list(ft_tuple)
# Encontra o índice do elemento a ser substituído e faz a substituição
index = ft_list_from_tuple.index('toto!')
ft_list_from_tuple[index] = 'Brasil!'
# Converte a lista de volta em uma tupla
ft_tuple = tuple(ft_list_from_tuple)

# Remove o elemento no conjunto e adiciona outro
# O conjunto não garante a ordem dos elementos
# O conjunto não permite elementos duplicados
ft_set.add("Rio de Janeiro!")
ft_set.remove("tutu!")

# Modifica o dicionário
ft_dict['Hello'] = '42Rio!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)