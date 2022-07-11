from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.core.paginator import Paginator


# Create your views here.
def intro(request):
  return render(request, 'intro.html')

def home(request):
  blogs = Blog.objects.order_by('-pub_date')
  query = request.GET.get('query')
  if query:
    blogs = Blog.objects.filter(title__contains=query)
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {'blogs':paginated_blogs})

def about(request):
  return render(request, 'about.html')

def detail(request, id):
  blog = get_object_or_404(Blog, pk=id)
  comment_form = CommentForm()
  comments = Comment.objects.filter(post_id = id).order_by('-created_time')
  return render(request, 'detail.html', {"blog" : blog, "comment_form":comment_form, "comments":comments})

def new(request):
  form = BlogForm()
  if request.method == "POST":
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
      new_blog = form.save(commit=False)
      new_blog.pub_date = timezone.now()
      if request.user.is_authenticated:
        new_blog.user = request.user
      new_blog.save()
      return redirect('blog:detail', new_blog.id)
    return redirect('blog:home')
  return render(request, 'new.html', {"form" : form})

def update(request, id):
  update_blog = Blog.objects.get(id=id)
  if request.method == "POST":
    update_blog.title = request.POST["title"]
    update_blog.singer = request.POST["singer"]
    update_blog.code = request.POST["code"]
    update_blog.pub_date = timezone.now()
    update_blog.lyrics = request.POST["lyrics"]
    update_blog.memo = request.POST["memo"]
    update_blog.save()
    return redirect('blog:detail', update_blog.id)
  return render(request, 'update.html', {"blog":update_blog})

def delete(request, id):
  blog = Blog.objects.get(id=id)
  blog.delete()
  return redirect('blog:home')

def comments_create(request, id):
  form = CommentForm(request.POST)
  if form.is_valid():
    finalform = form.save(commit=False)
    finalform.post = get_object_or_404(Blog, pk=id)
    if request.user.is_authenticated:
      finalform.user = request.user
    finalform.save()
  return redirect('blog:detail', id)

def comments_delete(request, blog_id, comment_id):
  comment = Comment.objects.get(pk = comment_id)
  if request.user.is_authenticated:
    comment.delete()
  return redirect('blog:detail', blog_id)

def indie(request):
  blogs = Blog.objects.filter(genre="Indie").order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {"blogs":paginated_blogs})

def rock(request):
  blogs = Blog.objects.filter(genre="Rock").order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {"blogs":paginated_blogs})

def kpop(request):
  blogs = Blog.objects.filter(genre="K-pop").order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {"blogs":paginated_blogs})

def pop(request):
  blogs = Blog.objects.filter(genre="Pop").order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {"blogs":paginated_blogs})

def other(request):
  blogs = Blog.objects.filter(genre="Else").order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  paginated_blogs = paginator.get_page(page)
  return render(request, 'home.html', {"blogs":paginated_blogs})

def mycode(request):
  if request.user.is_authenticated:
    blogs = Blog.objects.filter(user = request.user).order_by('-pub_date')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {"blogs":paginated_blogs})
  else:
    return redirect('account:login')