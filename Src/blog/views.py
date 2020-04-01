from django.shortcuts import render
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
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title':'من أنا'})













