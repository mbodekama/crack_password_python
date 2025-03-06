import requests

def get_followers(url):
    response_get_followers = requests.get(data_dict['followers_url'])
    for follower in response_get_followers.json():
        avatars_req = requests.get(follower['avatar_url'])
        avatar_name = follower['login'] + '.jpg'
        with open(avatar_name, 'wb') as file:
            file.write(avatars_req.content)

try:
    r = requests.get('https://api.github.com/users/mbodekama')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.status_code)
    data_dict = r.json()

    #get_followers(data_dict['followers_url'])

except requests.exceptions.RequestException as e:
    print(e)
else:
    if r.status_code == 200:
        try:
            req2 = requests.get(data_dict['repos_url'])
            avatar_req = requests.get(data_dict['avatar_url'])
        except requests.exceptions.RequestException as e:
            print(e)
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




