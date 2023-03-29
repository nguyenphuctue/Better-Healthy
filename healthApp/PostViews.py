from django.contrib import messages
from django.shortcuts import render, redirect

from healthApp.forms import CreatePostForm
from healthApp.models import Post, CustomUser


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {"post": post, }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    form = CreatePostForm()
    context = {"form": form}
    return render(request, 'post/post_create.html', context)


def post_create_save(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.data['category']
            post_image = request.FILES['post_image']
            content = form.cleaned_data['content']

            user_id = request.user.id
            user = CustomUser.objects.get(id=user_id)

            post = Post.objects.create(user_id=user, title=title, category=category, post_image=post_image,
                                       content=content)

            return redirect('healthApp:home')
    else:
        messages.error(request, "Invalid Method")
        return redirect('healthApp:post_create')
    return render(request, 'post/post_create.html', {'form': form})


def post_edit_save(request, id):
    post = Post.objects.get(id=id)
    initial_data = {
        'title': post.title,
        'category': post.category,
        'content': post.content,
        'post_image': post.post_image,

    }
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.category = form.data['category']
            post.content = form.cleaned_data['content']

            if request.FILES.get('post_image') is not None:
                post.post_image = request.FILES.get('post_image')

            post.save()
            return redirect('healthApp:list_post_by_user_id', id=request.user.id)
    else:
        form = CreatePostForm(initial=initial_data)
    return render(request, 'post/post_edit.html', {'form': form, 'post_id': post.id})


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('healthApp:list_post_by_user_id', id=request.user.id)
