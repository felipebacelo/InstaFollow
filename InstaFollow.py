import csv
from instaloader import Instaloader, Profile

def login(username, password):
    # Cria uma instância do Instaloader e faz login no Instagram
    L = Instaloader()
    L.login(username, password)
    return L

def get_followers_list(L, username):
    # Obtém a lista de usuários que me seguem
    profile = Profile.from_username(L.context, username)
    followers = profile.get_followers()
    return sorted([follower.username for follower in followers])

def get_following_list(L, username):
    # Obtém a lista de usuários que eu sigo
    profile = Profile.from_username(L.context, username)
    following = profile.get_followees()
    return sorted([followee.username for followee in following])

def generate_csv_file(filename, headers, data):
    # Gera um arquivo CSV com os dados fornecidos
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    # Informe as credenciais de login
    username = "username"
    password = "password"

    # Faz login no Instagram
    L = login(username, password)

    # Obtém a lista de usuários que eu sigo e que me seguem
    followers = get_followers_list(L, username)
    following = get_following_list(L, username)

    # Gera os dados para os arquivos CSV
    followers_data = [[follower, follower in following] for follower in followers]
    following_data = [[followee, followee in followers] for followee in following]

    # Cabeçalhos dos arquivos CSV
    followers_headers = ['Me segue', 'Eu sigo de volta']
    following_headers = ['Eu sigo', 'Me segue de volta']

    # Gera os arquivos CSV
    generate_csv_file('followers.csv', followers_headers, followers_data)
    generate_csv_file('following.csv', following_headers, following_data)

    print("Arquivos CSV gerados com sucesso!!!")

if __name__ == "__main__":
    main()