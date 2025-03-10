import sys
import requests
from pathlib import Path

def get_followers(data_dict):
    response_get_followers = requests.get(data_dict['followers_url'])
    for follower in response_get_followers.json():
        dossier = Path(follower['login'])

        avatar_name = follower['login'] + '.jpg'
        avatar = dossier / avatar_name
        dossier.mkdir(parents=True, exist_ok=True)

        repo_info = 'repo-'+follower['login'] + '.txt'
        repo_info_file = dossier / repo_info
        dossier.mkdir(parents=True, exist_ok=True)

        re_follower_repo = requests.get(follower['repos_url'])
        for repo in re_follower_repo.json():
            line = (f"Nom du repository : {repo['name']} \n Description : {repo['description']} \n "
                    f"URL : {repo['url']} \n {('-')*50} \n")
            with repo_info_file.open('a') as file:
                file.write(line)

        avatars_req = requests.get(follower['avatar_url'])
        with avatar.open('wb') as file:
            file.write(avatars_req.content)

try:
    username = input('username: ')
    r = requests.get('https://api.github.com/users/'+username)
    """print(r.status_code)
    print(r.headers['content-type'])
    print(r.status_code)"""
    data_dict = r.json()
    get_followers(data_dict)

except requests.exceptions.RequestException as e:
    print(e)
else:
    if r.status_code == 200:
        try:
            req2 = requests.get(data_dict['repos_url'])
            avatar_req = requests.get(data_dict['avatar_url'])
        except requests.exceptions.RequestException as e:
            print("Erreur : Problème de connexion.")
        else:
            if avatar_req.status_code == 200:
                img_name = data_dict['login'] + '.jpg'
                with open(img_name, 'wb') as f:
                    f.write(avatar_req.content)

                list_repo = req2.json()
                for repo in list_repo:
                    print(f"Nom repo : {repo['name']} => {repo['description']}")
            else:
                print("Erreur lors du téléchargement de l'avatar")
    else:
        print("Aucune ressource trouvé")


print("Fin du programme")

