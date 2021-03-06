import unittest
from github_repos import GitHubRepos

class HTTPAndWebTest(unittest.TestCase):
    def test_status_code(self):
        gr = GitHubRepos()
        self.assertEqual(gr.status_code, 200, msg='The HTTP status code should be 200')

    def test_not_found(self):
        gr = GitHubRepos('kenlebu')
        self.assertEqual(gr.status_code, 404, msg='Should return 404 error')
    
if __name__ == '__main__':
    unittest.main()
