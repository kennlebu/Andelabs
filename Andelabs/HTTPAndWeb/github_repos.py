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
            
            print('Language\t\t| Repository name')
            for repo in response.json():
                print('[{}]\t\t| {}'.format(repo['language'], repo['name']))

        else:
            print('Error {0}: {1}'.format(response.status_code, response.text))


if __name__ == '__main__':
    print(GitHubRepos('andela').status_code)

