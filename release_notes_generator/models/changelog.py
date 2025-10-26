class Changelog:
    def __init__(self):
        self.releases = []

    def add_release(self, release):
        self.releases.append(release)

    def get_releases(self):
        return self.releases