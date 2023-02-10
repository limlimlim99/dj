from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
# view는 함수방식, class방식 2개가 있다.
# listviwe를 상속을 받아서 씀 

# listview 상속받기
class PostList(ListView):
    model = Post
    # ordering은 순서이다. 최근에 온 것이 가장 먼저 뜨게 함
    ordering = '-pk'


    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories']= Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories']= Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def category_page(request, slug):   # slug는 일반적으로 이미 얻은 데이터를 사용하여 유효한 url을 생성하는 방법
    if slug == 'no category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    
    return render(
        request, 
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category, 
        } 
    )