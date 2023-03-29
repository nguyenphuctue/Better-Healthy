from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from healthApp.forms import EditUserForm
from healthApp.models import CustomUser, Post


# def index(request):
#     return render(request, 'index.html')


def home(request):
    category = request.GET.get('category')
    if category is not None:
        category = request.GET.get('category')
        posts = Post.objects.all().filter(category=category)
    else:
        posts = Post.objects.all().order_by('created_at')

    for p in posts:
        if len(p.content) < 80:
            p.content = p.content[0:180] + '...'

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    first_post = Post.objects.filter(category="1").first()
    second_post = Post.objects.filter(category="2").first()
    third_post = Post.objects.filter(category="3").first()
    context = {
        "user": request.user,
        "page_posts": page_posts,
        "first_post": first_post,
        "second_post": second_post,
        "third_post": third_post,

    }
    return render(request, 'home.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('healthApp:home')
        else:
            messages.error(request, "Username hoặc mật khẩu của bạn chưa đúng. Vui lòng kiểm tra lại !")
            return render(request, 'authentication/login.html',)

    return render(request, 'authentication/login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]

        my_user = CustomUser.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.phone = phone
        my_user.address = "None"

        my_user.save()
        messages.success(request, "Register successful")

        return redirect("healthApp:login")
    return render(request, 'authentication/register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "Logout successful")
    return redirect('healthApp:home')


def user_profile(request):
    current_user = request.user
    initial_data = {
        # 'user_image': current_user.user_image,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'username': current_user.username,
        'phone': current_user.phone,
        'email': current_user.email,
        'address': current_user.address,
    }
    form = EditUserForm(initial=initial_data)
    context = {
        "user": request.user,
        "form": form
    }
    return render(request, 'user/profile.html', context)


def user_edit_save(request, id):
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES)
        if form.is_valid():
            user_image = request.FILES.get('user_image')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']

            user = CustomUser.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.phone = phone
            user.email = email
            user.address = address
            if user_image is not None:
                user.user_image = user_image
            user.save()

            return redirect('healthApp:user_profile')
    else:
        messages.error(request, "Invalid Method")
        return redirect('healthApp:user_profile')
    return render(request, 'user/profile.html', {'form': form})


def list_post_by_user_id(request, id):
    posts = Post.objects.filter(user_id=id).order_by('created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    context = {
        "page_posts": page_posts
    }
    return render(request, 'user/list_post.html', context)
