from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
