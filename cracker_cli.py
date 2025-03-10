import argparse
import hashlib
import time
import sys
import crack_dictionnaire as crack


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI pour CRACKER un PASSWORD')
    parser.add_argument('file', metavar='filename', help='Chemin du fichier qui contient les mots francais')
    parser.add_argument('password',metavar='password',type=str,help='Mot de passe a decouvrir')
    parser.add_argument('-d','--detail',dest='detail',action='store_true',help="Affiche les détails d'exécution du programme")
    args = parser.parse_args()

    try:
        crack.hash_crack(args.password,args.file,args.detail)
    except KeyboardInterrupt as e:
        exit(1)

