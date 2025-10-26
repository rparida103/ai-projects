import pytest
from release_notes import ReleaseNotes
from models.release import Release

@pytest.fixture
def release_notes():
    return ReleaseNotes()


def test_add_release(release_notes):
    release_notes.add_release('1.0.0', 'Initial release', '2023-10-01')
    releases = release_notes.get_releases()
    assert len(releases) == 1
    assert releases[0].version == '1.0.0'
    assert releases[0].description == 'Initial release'
    assert releases[0].date == '2023-10-01'


def test_get_releases_empty(release_notes):
    assert release_notes.get_releases() == []