from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, HashTag
from .forms import BlogForm, CommentForm

# Create your views here.

def home(request):
    blog = Blog.objects #query set!
    return render(request, 'home.html', {'blogs': blog})

def detail(request, blog_id): 
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blog_hashtag = blog_detail.hashtag.all()
    return render(request, 'detail.html', {'blog': blog_detail, 'hashtags': blog_hashtag})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    new_form = BlogForm(request.POST, request.FILES)
    if new_form.is_valid():
        new_blog = new_form.save(commit=False) 
        new_blog.pub_date = timezone.now()
        new_blog.save() #데이터베이스에 반영하는 과정
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            # ht = HashTag()
            # ht.hashtag_name = tag
            # ht.save()
            # new_blog.hashtag.add(ht) #주석처리한 곳처럼 하면 태그가 중복으로 등록됨
            ht=HashTag.objects.filter(hashtag_name=tag)
            new_blog.hashtag.add(ht[0])
        return redirect('detail', new_blog.id)
    return redirect('home')

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    blog_update.title = request.POST['title']
    blog_update.body = request.POST['body']
    blog_update.save()
    return redirect('home')

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': blog_detail})

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def add_comment_to_post(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form' : form})