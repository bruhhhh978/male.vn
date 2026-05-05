from django.contrib import messages
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    # Lấy tất cả bài viết, sắp xếp theo mới nhất
    posts = Post.objects.all().order_by('-create_at').select_related('user')
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('posts:index')
    else:
        form = PostCreateForm()
    return render(request, 'posts/create.html', {'form': form})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', id=post.id)
    else:
        form = PostCreateForm(instance=post)

    return render(request, 'posts/edit.html', {'form': form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:index')

    return render(request, 'posts/delete.html', {'post': post})

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.info(request, 'Đã bỏ thích bài viết.')
    else:
        post.likes.add(request.user)
        messages.success(request, 'Đã thích bài viết!')
    
    return redirect('posts:index')

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        text = request.POST.get('comment_text')
        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=text
            )
            messages.success(request, 'Đã thêm bình luận 💬')

    return redirect('posts:detail', pk=pk)