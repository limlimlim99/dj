# view는 함수방식, class방식 2개가 있다.
# listviwe를 상속을 받아서 씀 

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# listview 상속받기
class PostList(ListView):
    model = Post
    # ordering은 순서이다. 최근에 온 것이 가장 먼저 뜨게 함
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post