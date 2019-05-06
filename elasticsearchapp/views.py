from django.shortcuts import render

from .search import PostDocument

def search(request):

    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match", title=q)
        for i in posts:
        	print(i.username)
    else:
        posts = ''

    return render(request, 'search.html', {'posts': posts})
