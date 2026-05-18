import os

palavra_secreta = input('Digite sua palavra secreta (não deixe o outro jogador ver): ').lower()
letras_certas = ''
tentativas = 0
erro = 0


while True:
    letra = input('Digite uma letra: ').lower()
    os.system("cls" if os.name == "nt" else "clear")
    tentativas += 1
    if len(letra) > 1:
        tentativas -= 1
        print('Digite apenas uma letra.')
        continue

    if letra in letras_certas:
        tentativas -= 1
        print ('Essa letra ja foi digitada.')
        print (f'A palavra formada é: {palavra_formada}')
        continue

    if letra not in palavra_secreta:
        erro += 1
        if erro >= 6:
            print ('Você perdeu :(. Tente novamente! ')
            letras_certas = ''
            tentativas = 0
            erro = 0

    if letra in palavra_secreta:
        letras_certas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
           palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    print (f'A palavra formada é: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system ("cls" if os.name == "nt" else "clear")
        print ('VOCÊ GANHOU!!')
        print (f'Você teve {tentativas} tentativas!')
        print (f'Você errou {erro} vezes!')
        print ('Jogue novamente!')
        print ('\n' * 3)
        palavra_secreta = input('Digite sua palavra secreta (não deixe o outro jogador ver) ').lower()
        letras_certas = ''
        tentativas = 0
        erro = 0
        