from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Category

from .forms import ArticleForm
from .models import *
from .util import get_random_page


# Create your views here.

def index_html(request):
    title = Category.objects.all()
    context = {
        'title': title,
        'name': "Wiki_test"
    }
    return render(request, 'new_app/index.html', context)


def article(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category
    }
    return render(request, 'news/article.html', context)


class AddArticle(CreateView):
    model = Category
    form_class = ArticleForm
    template_name = 'new_app/add_article.html'
    success_url = reverse_lazy('index')


class ArticleDeleteView(DeleteView):
    model = Category
    template_name = 'new_app/delete_article.html'
    context_object_name = 'article'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')



class EditArticle(UpdateView):
    model = Category
    form_class = ArticleForm
    template_name = 'new_app/add_article.html'


def search(request):
    word = request.GET.get('q')
    print(word)
    articles = Category.objects.filter(Q(titles__icontains=word))

    context = {
        'titles': word,
        'components': articles
    }

    return render(request, 'new_app/index.html', context)



class RandomPage(DetailView):
    model = Category
    template_name = "news/article.html"

    def get_object(self, queryset=None):
        random_page = get_random_page(Category.objects.all())
        if random_page is not None:
            return random_page