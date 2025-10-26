import pytest
from markdown_formatter import format_release_notes
from models.release import Release


def test_format_release_notes():
    releases = [
        Release('1.0.0', 'Initial release', '2023-10-01'),
        Release('1.1.0', 'Minor improvements', '2023-10-15')
    ]
    expected_markdown = '## Version 1.0.0\nDate: 2023-10-01\nDescription: Initial release\n\n## Version 1.1.0\nDate: 2023-10-15\nDescription: Minor improvements\n\n'
    assert format_release_notes(releases) == expected_markdown