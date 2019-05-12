from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib import messages
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def home(request): #request란? 사용자가 요청한 메서드 + string + ... 값 / 해쉬 형태로 넘어간다
    post_list = Post.objects.all().order_by('-updated_at')
    paginator = Paginator(post_list, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts' : posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/new.html', {'form': form})

def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk) #post를 가져와서 댓글을 쓸 post를 인식함
    if request.method == "POST":
        form = CommentForm(request.POST)
        # post = get_object_or_404(Post)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('detail', post.pk) #pk = post(변수).pk라고 써줘야 함
    else:
        form = CommentForm()
    return render(request, 'blog/comment_new.html', {'form': form})

def edit(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id) 
        form = PostForm(request.POST, request.FILES, instance = post) #post 모델 중 한 행 - 폼 필드에 채워
        if form.is_valid():
            post = form.save()
            return redirect('detail', post.pk)
    else:
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(instance = post)
    return render(request, 'blog/edit.html', {'form': form, 'post': post})

def remove(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')

def comment_remove(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', post_id=comment.post.pk)