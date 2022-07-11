from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('home/', home, name='home'),
    path('<int:id>/', detail, name='detail'),
    path('new/', new, name='new'),
    path('about/', about, name="about"),
    path('genre/indie', indie, name="indie"),
    path('genre/rock', rock, name="rock"),
    path('genre/kpop', kpop, name="kpop"),
    path('genre/pop', pop, name="pop"),
    path('genre/other', other, name="other"),
    path('mycode/', mycode, name="mycode"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('comments_create/<int:id>', comments_create, name="comments_create"),
    path('comments_delete/<int:blog_id>/<int:comment_id>', comments_delete, name="comments_delete"),
]