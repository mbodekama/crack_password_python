import hashlib
import time
import string


mot_de_passe = input("Entrez le mot de passe : ")
password_hash = hashlib.md5(mot_de_passe.encode('utf-8')).hexdigest()
print(f"Password claire =>  {mot_de_passe} et password hashé  : {password_hash}")

def hash_crack(password_hash):
    debut = time.time()
    file = open("liste_francais.txt", "r")
    for line in file:
        mot_fr = line.strip()
        mot_fr_hash = hashlib.md5(mot_fr.encode('utf-8')).hexdigest()
        if password_hash == mot_fr_hash:
            print(f"Mot de passe trouvé : {mot_fr} HASH  => {mot_fr_hash}")
            fin = time.time()
            print(f"Temps d'execution : {(fin - debut):.2f} secondes")
            return



hash_crack(password_hash)