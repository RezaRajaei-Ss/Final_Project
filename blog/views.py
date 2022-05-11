from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.contrib.auth.models import User
from account.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from account.mixins import AuthorAccessMixin
#from django.http import HttpResponse

# # Create your views here.
# def home(request, page_number=1):

#     articles_list = Article.objects.filter(status='p')
#     paginator = Paginator(articles_list, 3)
#     page_number = request.GET.get('page')
#     articles = paginator.get_page(page_number)
#     context = {
#        "articles": articles, 
#           #"articles": Article.objects.filter(status='p')
#           # or  "articles": Article.objects.published()NL
#     }
#     return render(request, "blog/index.html" , context)


class ArticleList(ListView):
    #context_object_name = "articles"
    queryset = Article.objects.published()
    #template_name =  "blog/index.html" # in home its not nessosary
    paginate_by=3
    

class ArticleDetail(DetailView):
    #template_name =  "blog/detail.html" 
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


class ArticlePreview(AuthorAccessMixin, DetailView):
    #template_name =  "blog/detail.html" 
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


# def detail(request, slug):
#     context = {
#        "article": get_object_or_404(Article, slug=slug, status="p"),

#     }
#     return render(request,"blog/detail.html" , context)   

# def category(request, slug, page_number=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     page_number = request.GET.get('page')
#     paginator = Paginator(articles_list, 3)
#     articles = paginator.get_page(page_number)
#     context = {
#          "category": category,
#          "articles": articles
#    }
#     return render(request, "blog/category.html" , context)


class CategoryList(ListView):
    template_name =  "blog/category_list.html"
    paginate_by=3

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name =  "blog/author_list.html"
    paginate_by=3

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context