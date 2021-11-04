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
    errors = 0

    while(not acertou and not enforcou):
        chute = input('Qual a letra? ').strip()

        if chute in palavra_secreta:
            i: int = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    palavra_jogo[i] = chute
                i = i + 1
        else:
            errors = errors + 1

        print(palavra_jogo)
        enforcou = errors == 6
        acertou = "_" not in palavra_jogo

    if acertou:
        print("Você ganhou!")
    else:
        print("Quem sabe na próxima?")
    print('Fim do jogo')


if(__name__ == "__main__"):
    jogar()
