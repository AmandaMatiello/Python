#calcular a média das notas de um aluno e exibir uma mensagem na tela dizendo se ele foi aprovado (média >= 6) ou ficou de recuperação (média < 6)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 6:
    print('Sua média foi {:.1f}, você está de recuperação.'.format(media))
elif media >= 6:
    print('Sua média foi {:.1f}, você está aprovado.'.format(media))