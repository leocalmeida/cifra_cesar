def is_number(value):
    """ Valida se o valor fornecido é um numero inteiro """
    return value.isdigit()


def is_c_or_d(value):
    """ valida se a opção passada é a letra C ou a letra D """
    local_value = value.lower()
    if local_value == "c" or local_value == "d":
        return True
    else:
        return False


def encrypt_decrypt_pass(letter, pace, opt):

    local_pace = int(pace)

    is_lowecase = letter.islower()

    local_letter = letter.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz" if opt == 'c' else "abcdefghijklmnopqrstuvwxyz"[::-1] 

    if local_letter.isalpha():
        if int(pace) > 26:
            i = local_pace // 26
            local_pace = local_pace - (i * 26)

        letter_position = alphabet.find(local_letter)

        if (letter_position + local_pace) > 25:
            new_position = (letter_position + local_pace) - 26
        else:
            new_position = letter_position + local_pace

        return alphabet[new_position] if is_lowecase else alphabet[new_position].upper()

    else:
        return local_letter


def main():
    new_message = ""

    message = input("Digite uma mensagem a ser tratada: ")

    pace = input("Quantas posicoes devo usar: ")
    while is_number(pace) == False:
        pace = input("Valor invalido! Digite um numero inteiro. Quantas posicoes devo usar?: ")

    opt = input("Escolha c - Criptograr ou d - Descriptografar: ")
    while is_c_or_d(opt) == False:
        opt = input("Opcao invalida! Escolha c - Criptograr ou d - Descriptografar: ")

    for letter in message:
        new_message = new_message + encrypt_decrypt_pass(letter, pace, opt)

    return new_message


print(f"Sua mensagem tratada: {main()}")
