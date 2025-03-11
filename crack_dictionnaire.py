import hashlib
import os
import time
import sys

def hash_crack(password_hashed,filename='liste_francais.txt',detail=False):
    """
    :param password_hashed: le mot de passe a trouver
    :param filename: Nom du fichier des mots clés
    :param detail: POur afficher la progression
    :return:
    """
    debut = time.time()
    try :
        file = open(filename, 'r')
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    else:
        trouve  = False
        for line in file:
            mots_dict = line.strip()
            if detail :
                sys.stdout.write(f'\r{" " * 100}')
                sys.stdout.write(f"\r{mots_dict} ")
                sys.stdout.flush()
                time.sleep(0.001)

            if hashlib.md5(mots_dict.encode('utf-8')).hexdigest() == password_hashed:
                trouve = True
                print(f"\nLe mot de passe est: {mots_dict}")
                break

        if not trouve :
            print("Mot de passe introuvable / le mot hashé n'est pas dans la liste")

    finally:
        fin = time.time()
        print(f"Excécution en {(fin - debut):.2f} s")
        print("Le programme a finit de s'exécuter")


if __name__ == "__main__":
    print('Dans crack dico')
    password_hash = input("Enter le mot hashé : ")
    hash_crack(password_hash,detail=True)

