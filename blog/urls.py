from django.urls import path
#from .views import home, detail, category
from .views import ArticleList, ArticleDetail, ArticlePreview, CategoryList, AuthorList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page_number>', ArticleList.as_view(),name='home'),
    path('articles/<slug:slug>', ArticleDetail.as_view() ,name='detail'),
    path('preview/<int:pk>', ArticlePreview.as_view() ,name='preview'),
    path('category/<slug:slug>', CategoryList.as_view() ,name='category'),
    path('category/<slug:slug>/page/<int:page_number>', CategoryList.as_view() ,name='category'),
    path('author/<slug:username>', AuthorList.as_view() ,name='author'),
    path('author/<slug:username>/page/<int:page_number>', AuthorList.as_view() ,name='author')


]

