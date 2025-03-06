import hashlib
import time
import argparse
import sys

parser = argparse.ArgumentParser(description='Carcker CLI')
parser.add_argument('file',metavar='filename', type=str, help='Chemin du fichier')
parser.add_argument('password',metavar='password', type=str,  help='Mot de passe hashé')
parser.add_argument('-d', '--detail', dest='detail', action='store_true', help='Show detail of execution' ,required=False)



args = parser.parse_args()

args.password = hashlib.md5(args.password.encode('utf-8')).hexdigest()


def hash_crack(password_hashed, file_path):
    debut = time.time()
    try :
        file = open(file_path, 'r')
    except FileNotFoundError:
        print("Le fichier n'existe pas")
        return
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    else:
        trouve  = False
        for line in file:
            mots_dict = line.strip()
            if args.detail :
                sys.stdout.write(f'\r{" " * 100}')  # Remplir la ligne avec des espaces pour effacer l'ancien texte
                sys.stdout.write(f'\rEssai : {mots_dict}')  # Afficher le nouveau mot
                sys.stdout.flush()
                time.sleep(0.001)
            if hashlib.md5(mots_dict.encode('utf-8')).hexdigest() == password_hashed:
                trouve = True
                print(f"Le mot de passe est: {mots_dict}")
                break
        if not trouve :
            print("Mot de passe introuvable")

    finally:
        fin = time.time()
        print(f"Excécution en {(fin - debut):.2f} secondes")
        print("Le programme a finit de s'exécuter")


hash_crack(args.password, args.file)