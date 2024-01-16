from django.shortcuts import render
from . import util
import markdown2
import random

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
        "content": content,
        "title": title
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

def new_page(request):
    title = request.GET.get('title')
    content = request.GET.get('text-area')
    err = None
    entry_list = util.list_entries()
    if not title or not content:
        err  ="Please enter both title and description!"

    elif title in entry_list:
        err = "An entry with this title already exists!"

    if err:
        return render(request, "encyclopedia/new.html", {
            "err": err,
            "title": title,
            "text": content
        })
    else:
        util.save_entry(title, content)
        return render(request, "encyclopedia/new.html", {
            "err": "submitted",
            "title": "",
            "text": ""
        })

def edit_page(request):
    title = request.GET.get('title')
    content = util.get_entry(title)
    return render (request, "encyclopedia/edit.html", {
        "content": content,
        "title": title
    })

def save_page(request):
    title = request.GET.get('title')
    content = request.GET.get('text-area')
    util.save_entry(title, content)
    return entry(request, title)

def random_page(request):
    entry_list = util.list_entries()
    random_index = random.randint(0, len(entry_list) - 1)
    title = entry_list[random_index]
    return entry(request, title)






