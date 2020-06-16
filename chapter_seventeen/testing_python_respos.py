import unittest
from python_respos import github_python_reponse


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        data = github_python_reponse()
        self.assertEqual(data, 'python_repos.html')


if __name__ == '__main__':
    unittest.main()
