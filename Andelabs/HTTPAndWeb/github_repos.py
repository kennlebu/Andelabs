import requests

class GitHubRepos:
    def __init__(self, username='kennlebu'):
        self.status_code = None
        self.username = username
        self.print_repos()
        
    def print_repos(self):
        response = requests.get('https://api.github.com/users/{}/repos'.format(self.username))

        #assert response.status_code == 200
        self.status_code = response.status_code
        if self.status_code == 200:
            
            print('Language  :   Repository name')
            for repo in response.json():
                print('[{}]  : {}'.format(repo['language'], repo['name']))

        else:
            ans = response.json()
            err = ans['message']
            print('Error {0}: {1}'.format(response.status_code, err))


if __name__ == '__main__':
    username = input("Enter a GitHub username: ")
    GitHubRepos(username)

