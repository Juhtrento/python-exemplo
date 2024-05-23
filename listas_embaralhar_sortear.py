import random
alunos=['João', 'Maria', 'Ana', 'Pedro', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Escolhe um aluno aleatoreamente 
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")
