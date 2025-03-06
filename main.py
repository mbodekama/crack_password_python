import hashlib
import os
import time


password = input("Enter your password: ")
password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
print(f"Password hash: {password_hash}")

def hash_crack(password_hashed):
    debut = time.time()
    try :
        file = open('liste_francais.txt', 'r')
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    else:
        trouve  = False
        for line in file:
            mots_dict = line.strip()
            if hashlib.md5(mots_dict.encode('utf-8')).hexdigest() == password_hashed:
                trouve = True
                print(f"Le mot de passe est: {mots_dict}")

        if not trouve :
            print("Mot de passe introuvable")

    finally:
        fin = time.time()
        print(f"Excécution en {fin - debut} s")
        print("Le programme a finit de s'exécuter")





hash_crack(password_hash)