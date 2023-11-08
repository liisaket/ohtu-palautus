from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        name = data['tool']['poetry']['name']
        description = data['tool']['poetry']['description']
        license = data['tool']['poetry']['license']

        authors = data['tool']['poetry']['authors']

        dependencies = data['tool']['poetry']['dependencies']
        devdep = data['tool']['poetry']['group']['dev']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, devdep)
