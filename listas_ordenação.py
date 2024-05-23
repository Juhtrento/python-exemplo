import random
alunos=['João', 'Maria', 'Ana', 'Pedro', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Ordena a lista Crescente 
alunos.sort()
print(f"Lista crescente: {alunos}")
# Ordena a lista decrescente
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")
