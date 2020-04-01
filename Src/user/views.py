from django.shortcuts import render

def about(request):
    return render(request, 'blog/about.html', {'title':'من أنا'})

