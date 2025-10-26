from models.release import Release
from models.changelog import Changelog

class ReleaseNotes:
    def __init__(self):
        self.changelog = Changelog()

    def add_release(self, version, description, date):
        release = Release(version, description, date)
        self.changelog.add_release(release)

    def get_releases(self):
        return self.changelog.get_releases()