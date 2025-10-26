def format_release_notes(release_notes):
    markdown = ''
    for release in release_notes:
        markdown += f'## Version {release.version}\n'
        markdown += f'Date: {release.date}\n'
        markdown += f'Description: {release.description}\n\n'
    return markdown