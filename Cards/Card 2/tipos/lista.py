nums = [1, 2, 3]
print(type(nums))

nums.append(3)
nums.append(4)
nums.append(500)

#para adicionar na lista
print(len(nums))

print(2 in nums)

nums[3] = 100
#adicionando numero na posicao do indice
nums.insert(0, -200)
'''adicionando numero na posicao do indice
deslocando os outros numeros para direita'''

print(nums[6])
#acessar o elemento apartir do indice
print(nums[-1])
#indices negativos a ordem e de tras para frente
print(nums)