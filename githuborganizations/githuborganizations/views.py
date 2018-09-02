import requests


class Main():
    auth = ('carlossalas', 'bb68c007d0a1227396b4f2a23ef46879f6bf75ab')

    def getOrganization(self):
        re = requests.get('https://api.github.com/orgs/githubtraining', auth=self.auth)
        return re.json()
