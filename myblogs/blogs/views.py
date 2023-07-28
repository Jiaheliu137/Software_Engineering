from django.shortcuts import render

from .models import Post
from .models import Author
from django.shortcuts import get_object_or_404


from django.http import JsonResponse
from django.template.loader import render_to_string

from django.contrib import messages

from django.urls import reverse

from datetime import datetime, date

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

from django.db.models import Q
from .models import Post, Author

from django.views.generic import ListView

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from django.http import HttpResponse





def post_list(request):
    posts = Post.objects.all().order_by('-date_created')

    # Check if start_date and end_date parameters are provided
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    # Convert the date strings to datetime objects if they exist
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None

    # Swap start_date and end_date if start_date is after end_date
    if start_date and end_date and start_date > end_date:
        start_date, end_date = end_date, start_date

    # If both start_date and end_date exist, filter posts by the provided date range
    if start_date and end_date:
        posts = posts.filter(date_created__date__range=[start_date, end_date])

    paginator = Paginator(posts, 5)  # Show 5 posts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blogs/post_list.html', {'posts': posts})



def author_list(request):
    authors = Author.objects.all()
    return render(request, 'blogs/author_list.html', {'authors': authors})

from datetime import datetime, date

def author_posts(request, username):
    author = Author.objects.get(user__username=username)
    posts = Post.objects.filter(author=author).order_by('-date_created')

    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None

    if start_date and end_date and start_date > end_date:
        start_date, end_date = end_date, start_date

    if start_date and end_date:
        posts = posts.filter(date_created__date__range=[start_date, end_date])

    paginator = Paginator(posts, 5) 
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)

    current_url = reverse('author_posts', kwargs={'username': username})

    return render(request, 'blogs/author_posts.html', {'posts': posts, 'author': author,'current_url': current_url})


def date_posts(request, year, month, day):
    date = datetime(year, month, day)
    posts = Post.objects.filter(date_created__date=date)
    return render(request, 'blogs/date_posts.html', {'date': date, 'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in.
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blogs/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Log the user in.
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blogs/login.html', {'form': form})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.author
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blogs/new_post.html', {'form': form})





def search(request):
    query = request.GET.get('q', '')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None
    if start_date and end_date and start_date > end_date:
        start_date, end_date = end_date, start_date

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(author__user__username__icontains=query)
        )
        if start_date and end_date:
            results = results.filter(date_created__date__range=[start_date, end_date])
    else:
        results = Post.objects.none()

    paginator = Paginator(results, 5)
    page_number = request.GET.get('page', 1)
    results = paginator.get_page(page_number)

    return render(request, 'blogs/search_results.html', {'results': results, 'query': query})



class PostListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

from django.core.exceptions import PermissionDenied

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author.user or request.user.is_superuser:
        if request.method == 'POST':
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('post_list')
        else:
            return render(request, 'blogs/post_delete.html', {'post': post})
    else:
        raise PermissionDenied



    

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ChangeUsernameForm, CustomPasswordChangeForm

@login_required
def user_center(request):
    if request.method == 'POST':
        username_form = ChangeUsernameForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        
        if username_form.is_valid():
            username_form.save()
            messages.success(request, 'Your username was successfully updated!')
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
    else:
        username_form = ChangeUsernameForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    return render(request, 'blogs/user_center.html', {'username_form': username_form, 'password_form': password_form})
