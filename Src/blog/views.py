from django.shortcuts import render, get_object_or_404
from .models import Post ,Comment
from .forms import NewComment
posts = [
    {
        'title':'التدوينة الاولة',
        'content':'نص التدوينة الاولة كنص تجريبي',
        'post_date':'16-3-2020',
        'author':'محمود أحمد الفوراوي',
    },
    {
        'title':'التدوينة الثانية',
        'content':'نص التدوينة الثانية كنص تجريبي',
        'post_date':'16-9-2020',
        'author':'محمود أحمد الفوراوي',
    },
    {
        'title':'التدوينة الثالتة',
        'content':'نص التدوينة الثالتة كنص تجريبي',
        'post_date':'16-10-2020',
        'author':'محمود أحمد الفوراوي',
    },
]

def home(request):

    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'من أنا'})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context ={
        'title': post,
        'post': post,
        'comments': comments,
        'comment_from': comment_form,
    }
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    return render(request,'blog/detail.html',context )












