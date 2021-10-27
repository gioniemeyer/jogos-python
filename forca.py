def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    palavra_jogo = []

    for x in palavra_secreta:
        palavra_jogo.append('_')

    print(palavra_jogo)

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        chute = input('Qual a letra? ').strip()

        i: int = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                palavra_jogo[i] = chute
            i = i + 1
        print(palavra_jogo)

    print('Fim do jogo')


if(__name__ == "__main__"):
    jogar()
