from django.shortcuts import render
from . import util
import markdown2

markdowner = markdown2.Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        content = markdowner.convert(content)
    
    return render(request, "encyclopedia/entry.html", {
        "content": content
    })

