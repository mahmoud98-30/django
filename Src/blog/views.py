from django.shortcuts import render, get_object_or_404
from .models import Post ,Comment
from .forms import NewComment , PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
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
    posts = Post.objects.all()
    # how meny posts viwe in home
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    # code can you browse between pages
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        'page': page,
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

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False






