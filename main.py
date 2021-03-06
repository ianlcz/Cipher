#!/usr/bin/python3

import os
import time
import curses.ascii as ca
from pathlib import Path
from cipherlib import *

listMethods = [
    "Chiffre de César",
    "Chiffrement par substitution",
    "Chiffre de Vigenère",
    "Code Morse international"]


def read_file(name):
    """
    Reads the content of a text file specified by the user.
    """
    file = open(name, 'r', encoding="UTF-8")
    return file.read()


def write_file(content, specifyFolder=False):
    """
    Allows to write to a file.
    """
    if not specifyFolder:
        specifyFolder = "cipherFolder"
    while not os.path.exists(str(Path.home()) + '/' + specifyFolder + '/'):
        os.makedirs(str(Path.home()) + '/' + specifyFolder)
    with open(f"{time.strftime(str(Path.home()) + '/' + specifyFolder + '/' + '%d%m%Y%H%M%S')}", 'w', encoding="UTF-8") as file:
        file.write(content)
    return str(Path.home()) + '/' + specifyFolder + \
        '/' + time.strftime('%d%m%Y%H%M%S')


def leave_software():
    """
    Displays an end message when the user exits the program.
    """
    print(
        f"\t\tMerci d'avoir utilisé Cipher\n\n\t\t\t\t\t\t{' ' * 4}Yann LE COZ")
    time.sleep(2)
    os.system("clear")


def show_error(
        keyboard,
        isNotNumeric=False,
        checkSubstitutionAlphabet=False,
        duplicate=False):
    """
    Displays an error message when the user enters incorrect characters.
    """
    print(f"{'-' * 63}\n{' ' * 29}ERREUR\n{'-' * 63}")
    if isNotNumeric:
        print(
            f"Le caractère que vous venez d'entrez ({keyboard}) n'est pas un chiffre.\n")
    elif checkSubstitutionAlphabet:
        if duplicate:
            print(
                f"La lettre que vous venez d'entrer ({keyboard.upper()}) existe déjà.\n\nVeuillez en entrer une nouvelle:")
        else:
            print(
                f"La lettre que vous venez d'entrer ({keyboard}) est incorrecte.\n\nVeuillez entrer de nouveau une lettre de l'alphabet:")
    else:
        print(
            f"L'option que vous venez d'entrer ({keyboard}) est incorrecte.\n")


def do_you_want_to_continue():
    """
    Allows the user to return to the main menu or exit the program.
    """
    answerKeyboard = ''
    print(f"{'-' * 63}\n")
    while answerKeyboard.upper() != 'O' and answerKeyboard.upper() != 'N':
        if answerKeyboard != '':
            os.system("clear")
            show_error(answerKeyboard)
        answerKeyboard = input(
            "Voulez-vous retourner au menu principal [O/N] ? ")
        if answerKeyboard.upper() == 'O':
            os.system("clear")
            print(f"{'-' * 63}\n{' ' * 25}MENU PRINCIPAL\n{'-' * 63}")
            cipher_core()
        elif answerKeyboard.upper() == 'N':
            print("\n")
            leave_software()


def cipher_core():
    """
    This is the general function of Cipher, it is from it that users can encrypt or decrypt their various messages.
    """

    def display_options_message():
        """
        Allows the user to choose to encrypt or decrypt a message he has in his possession.
        """
        choiceOfFormat = ''
        choiceOfAction = ''
        print(f"{'-' * 63}\n{' ' * 27}OPTIONS\n{'-' * 63}")
        print("F - Fichier texte\nM - Message\n")
        while choiceOfFormat.upper() != 'F' and choiceOfFormat.upper() != 'M':
            choiceOfFormat = input("Quel format voulez-vous traiter [F/M] ? ")
        print(f"\n1 - Chiffrer\n2 - Déchiffrer\n{'-' * 63}\n")
        while choiceOfAction != '1' and choiceOfAction != '2':
            choiceOfAction = input("Entrez l'index d'une de ces options: ")
        return choiceOfFormat.upper() + choiceOfAction

    def display_message_entry_information():
        """
        Allows the user to enter the path of the text file or message they want to encrypt or decrypt.
        """
        if choiceOfOption == "F1":
            return str(Path.home()) + '/' + \
                input(f"Entrez le chemin de votre fichier:\n{str(Path.home())}/")
        elif choiceOfOption == "F2":
            return str(Path.home()) + '/cipherFolder/' + input(
                f"Entrez le chemin du fichier chiffré:\n{str(Path.home())}/cipherFolder/")
        elif choiceOfOption == "M1":
            return input("Entrez votre message: ")
        else:
            return input("Entrez le message chiffré: ")

    def create_overview(name, number):
        """
        Allows you to create an overview of text file.
        """
        return name[:number].replace('\n', '')

    message = ''
    choiceOfCipherMethod = ''
    while choiceOfCipherMethod not in ['1', '2', '3', '4'] and choiceOfCipherMethod.upper(
    ) != 'C' and choiceOfCipherMethod.upper() != 'Q':
        if choiceOfCipherMethod != '':
            os.system("clear")
            show_error(choiceOfCipherMethod)
        print("Méthodes d'encodage disponibles:")
        for index, nameMethods in enumerate(listMethods, 1):
            print(f"{index} - {nameMethods}")
        print(f"\nC - Crédits\nQ - Sortir de Cipher\n{'-' * 63}")
        choiceOfCipherMethod = input("\nEntrez l'index d'une de ces options: ")
    if choiceOfCipherMethod.upper() != 'Q':
        os.system("clear")
    if choiceOfCipherMethod == '1':
        choiceOfOption = display_options_message()
        choiceOfFolder = ''
        nameFolder = ''
        os.system("clear")
        print(f"{'-' * 63}\n{' ' * 22}CHIFFRE DE CÉSAR\n{'-' * 63}")
        while not message:
            message = display_message_entry_information()
        offset = input("Entrez la valeur du décalage: ")
        while offset.isnumeric() == False or int(offset) >= 26:
            if offset.isnumeric() == False:
                print("\n")
                show_error(offset, True)
                offset = input("\tVeuillez entrer le nombre de décalage: ")
            else:
                offset = input(
                    "\nVous venez de dépasser la limite de décalage. (Max. 25)\nVeuillez entrer un nombre de décalage plus petit: ")
        if choiceOfOption == "F1":
            nameFolder = write_file(
                caesar_encryption(
                    read_file(message),
                    int(offset)))
        elif choiceOfOption == "F2":
            while choiceOfFolder.upper() != 'O' and choiceOfFolder.upper() != 'N':
                choiceOfFolder = input(
                    "\nSouhaitez-vous enregistrer le fichier déchiffré dans un dossier\nprécis [O/N] ? ")
            if choiceOfFolder.upper() == 'O':
                pathFolder = input(
                    f"\nVeuillez indiquer le chemin vers ce dossier:\n{Path.home()}/").replace('//', '/')
                if pathFolder[-1] == '/':
                    list_pathFolder = list(pathFolder)
                    list_pathFolder.pop(-1)
                    pathFolder = ''.join(list_pathFolder)
                nameFolder = write_file(
                    caesar_encryption(
                        read_file(message),
                        int(offset),
                        True),
                    pathFolder)
            else:
                nameFolder = write_file(
                    caesar_encryption(
                        read_file(message),
                        int(offset),
                        True))
        print(f"\n\nCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}\n\nAperçu:\n{create_overview(caesar_encryption(read_file(message), int(offset)), 63)}" if choiceOfOption == 'F1' else f"\n\nDÉCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}" if choiceOfOption ==
              'F2' else f"\nVotre message chiffré est:\n{''.join(caesar_encryption(message, int(offset)))}" if choiceOfOption == 'M1' else f"\nLe message d'origine est:\n{caesar_encryption(message, int(offset), True)}")
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '2':
        choiceOfOption = display_options_message()
        choiceOfFolder = ''
        nameFolder = ''
        os.system("clear")
        print(f"{'-' * 63}\n{' ' * 17}CHIFFREMENT PAR SUBSTITUTION\n{'-' * 63}")
        key = ''
        while not message:
            message = display_message_entry_information()
        if choiceOfOption[1] == '1':
            print("\nCONFIGURATION DE L'ALPHABET DE SUBSTITUTION\n")
            for letterAlphabet in string.ascii_uppercase:
                letterUser = input(f"\t{letterAlphabet}: ")
                while len(letterUser) != 1 or letterUser.upper() in key or letterUser.isnumeric(
                ) or letterUser.upper() == ' ' or ca.ispunct(letterUser):
                    print("\n")
                    show_error(
                        letterUser,
                        False,
                        True,
                        True) if letterUser.upper() in key else show_error(
                        letterUser,
                        False,
                        True)
                    letterUser = input(f"\t{letterAlphabet}: ")
                else:
                    key += unidecode(letterUser).upper()
        else:
            while len(key.replace(' ', '')) != 26 or key.isnumeric():
                key = input("Entrez votre clé de chiffrement: ")
        if choiceOfOption == "F1":
            nameFolder = write_file(
                substitution_encryption(
                    read_file(message),
                    unidecode(key).upper()))
        elif choiceOfOption == "F2":
            while choiceOfFolder.upper() != 'O' and choiceOfFolder.upper() != 'N':
                choiceOfFolder = input(
                    "\nSouhaitez-vous enregistrer le fichier déchiffré dans un dossier\nprécis [O/N] ? ")
            if choiceOfFolder.upper() == 'O':
                pathFolder = input(
                    f"\nVeuillez indiquer le chemin vers ce dossier:\n{Path.home()}/").replace('//', '/')
                if pathFolder[-1] == '/':
                    list_pathFolder = list(pathFolder)
                    list_pathFolder.pop(-1)
                    pathFolder = ''.join(list_pathFolder)
                nameFolder = write_file(
                    substitution_encryption(
                        read_file(message), unidecode(key).replace(
                            ' ', '').upper(), True), pathFolder)
            else:
                nameFolder = write_file(
                    substitution_encryption(
                        read_file(message), unidecode(key).replace(
                            ' ', '').upper(), True))
        print(f"\nVotre clé de chiffrement est:\n{' '.join(key)}\n\n\nCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}\n\nAperçu:\n{create_overview(substitution_encryption(read_file(message), unidecode(key).upper()), 63)}" if choiceOfOption == 'F1' else f"\n\nDÉCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}" if choiceOfOption ==
              'F2' else f"\nVotre clé de chiffrement est:\n{' '.join(key)}\nVotre message chiffré est:\n{substitution_encryption(message, unidecode(key).upper())}" if choiceOfOption == 'M1' else f"\nLe message d'origine est:\n{substitution_encryption(message, unidecode(key).replace(' ', '').upper(), True)}")
        do_you_want_to_continue()
    elif choiceOfCipherMethod == '3':
        choiceOfOption = display_options_message()
        choiceOfFolder = ''
        nameFolder = ''
        os.system("clear")
        print(f"{'-' * 63}\n{' ' * 21}CHIFFRE DE VIGENÈRE\n{'-' * 63}")
        while not message:
            message = display_message_entry_information()
        key = input("Entrez votre clé de chiffrement: ")
        if choiceOfOption == "F1":
            nameFolder = write_file(
                vigenere_encryption(
                    read_file(message), key))
        elif choiceOfOption == "F2":
            while choiceOfFolder.upper() != 'O' and choiceOfFolder.upper() != 'N':
                choiceOfFolder = input(
                    "\nSouhaitez-vous enregistrer le fichier déchiffré dans un dossier\nprécis [O/N] ? ")
            if choiceOfFolder == 'O':
                pathFolder = input(
                    f"\nVeuillez indiquer le chemin vers ce dossier:\n{Path.home()}/").replace('//', '/')
                if pathFolder[-1] == '/':
                    list_pathFolder = list(pathFolder)
                    list_pathFolder.pop(-1)
                    pathFolder = ''.join(list_pathFolder)
                nameFolder = write_file(
                    vigenere_encryption(
                        read_file(message),
                        key,
                        True),
                    pathFolder)
            else:
                nameFolder = write_file(
                    vigenere_encryption(
                        read_file(message), key, True))
        print(f"\n\nCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}\n\nAperçu:\n{create_overview(vigenere_encryption(read_file(message), key), 63)}" if choiceOfOption == 'F1' else f"\n\nDÉCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}" if choiceOfOption ==
              'F2' else f"\nVotre message chiffré est:\n{''.join(vigenere_encryption(message, key))}" if choiceOfOption == 'M1' else f"\nLe message d'origine est:\n{vigenere_encryption(message, key, True)}")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == '4':
        choiceOfOption = display_options_message()
        choiceOfFolder = ''
        nameFolder = ''
        encodableCharacters = string.ascii_uppercase + \
            string.digits + '!\"$&\'()+,-./:;=?@_ '
        os.system("clear")
        print(f"{'-' * 63}\n{' ' * 20}CODE MORSE INTERNATIONAL\n{'-' * 63}")
        while not message:
            message = display_message_entry_information()
        if choiceOfOption == "F1":
            nameFolder = write_file(
                substitution_encryption(
                    read_file(message),
                    morseCharacters, False, encodableCharacters))
        elif choiceOfOption == "F2":
            while choiceOfFolder.upper() != 'O' and choiceOfFolder.upper() != 'N':
                choiceOfFolder = input(
                    "\nSouhaitez-vous enregistrer le fichier déchiffré dans un dossier\nprécis [O/N] ? ")
            if choiceOfFolder.upper() == 'O':
                pathFolder = input(
                    f"\nVeuillez indiquer le chemin vers ce dossier:\n{Path.home()}/").replace('//', '/')
                if pathFolder[-1] == '/':
                    list_pathFolder = list(pathFolder)
                    list_pathFolder.pop(-1)
                    pathFolder = ''.join(list_pathFolder)
                nameFolder = write_file(
                    substitution_encryption(
                        read_file(message),
                        morseCharacters,
                        True,
                        encodableCharacters),
                    pathFolder)
            else:
                nameFolder = write_file(
                    substitution_encryption(
                        read_file(message),
                        morseCharacters,
                        True,
                        encodableCharacters))
        print(f"\nCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}\n\nAperçu:\n{create_overview(substitution_encryption(read_file(message), morseCharacters, False, encodableCharacters), 63)}" if choiceOfOption == 'F1' else f"\n\nDÉCHIFFREMENT DU CONTENU DU FICHIER TERMINÉ\n{nameFolder}" if choiceOfOption ==
              'F2' else f"\nVotre message chiffré est:\n{substitution_encryption(message, morseCharacters, False, encodableCharacters)}" if choiceOfOption == 'M1' else f"\nLe message d'origine est:\n{substitution_encryption(message, morseCharacters, True, encodableCharacters)}")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'C':
        print(f"{'-' * 63}\n{' ' * 26}CRÉDITS\n{'-' * 63}\nVERSION:{' ' * 51}v1.0\n\nAUTEUR:{' ' * 45}Yann LE COZ\nÉTABLISSEMENT:{' ' * 29}Bordeaux Ynov Campus")
        do_you_want_to_continue()
    elif choiceOfCipherMethod.upper() == 'Q':
        print("\n")
        leave_software()


os.system("clear")
print(f"{'-' * 63}\n{' ' * 20}BIENVENUE DANS CIPHER\n{'-' * 63}\nCette application encode et décode des messages.\n")
cipher_core()
