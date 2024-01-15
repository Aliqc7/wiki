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

def search(request):
    query = request.GET.get('q', '')
    entry_list = util.list_entries()

    if query in entry_list:
        content = util.get_entry(query)
        content = markdowner.convert(content)
        return render(request, "encyclopedia/entry.html", {
        "content": content
    })
    else:


        
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "entry_list": entry_list
        })






