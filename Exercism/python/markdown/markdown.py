import re

# All constants placed at the top of this file.
LINES = {
    'h1': r'# (.*)',
    'h2': r'#{2} (.*)',
    'h3': r'#{3} (.*)',
    'h4': r'#{4} (.*)',
    'h5': r'#{5} (.*)',
    'h6': r'#{6} (.*)',
    'li': r'\* (.*)',
    'p': r'(?!<h)(?!<li)(.*)',
}
# Matched across multiple lines
FULL = {
    'strong': r'__([^_]+)__',
    'em': r'_([^_]+)_',
    'ul': r'(<li>.*</li>)',
}


def line_start(markdown):
    if markdown == '':
        return ''
    for tag, regex in LINES.items():
        m = re.match(regex, markdown)
        if m is not None:
            return (f'<{tag}>{m.group(1)}</{tag}>' +
                    line_start(markdown[m.end()+1:]))


def parse(markdown):
    markdown = line_start(markdown)
    for tag, regex in FULL.items():
        for m in re.finditer(regex, markdown):
            markdown = (markdown[:m.start()] +
                        f'<{tag}>{m.group(1)}</{tag}>' +
                        markdown[m.end():])
    return markdown
