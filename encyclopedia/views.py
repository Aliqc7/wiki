from django.shortcuts import render
from . import util
import markdown2

markdowner = markdown2.Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title.upper(),
        "content": markdowner.convert(util.get_entry(title.upper()))
    })

