nome = input('Digite seu nome, caro aluno!')
nota1 = float(input('Digite sua primeira nota!'))
nota2 = float(input('Digite sua segunda nota!'))

media = (nota1 + nota2) / 2

if media >=7:
    print (f'{nome}, Você foi aprovado com media {media: .1f}!')

else:
    print (f'{nome}, Você foi reprovado com media {media: .1f}!')