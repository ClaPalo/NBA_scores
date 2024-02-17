from rich.markdown import Markdown
from rich.console import Console
MARKDOWN = """
# This is an h1
## This is an h2
### This is an h3


Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""

console = Console()
md = Markdown(MARKDOWN)
console.print(md)
