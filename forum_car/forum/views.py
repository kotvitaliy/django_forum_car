from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Category, Product, Author, News
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from django.conf import settings
from .models import Comments
from .forms import CommentForm



@login_required(redirect_field_name=settings.LOGIN_URL)
def cabinet(request):
    ctx = {}
    ctx['cabinet_tab'] = 'main'
    if request.method == 'GET':
        try:
            author = Author.objects.get(user=request.user.id)
            ctx['form'] = AuthorForm(instance=author)
        except Exception as e:
            ctx['form'] = AuthorForm
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user.id)
            author.date_birth = form.cleaned_data['date_birth']
            author.bio = form.cleaned_data['information']
            author.type_view = form.cleaned_data['type_view']
            author.pseudoname = form.cleaned_data['cleaned_data']
            author.save()
            ctx['save'] = True
            ctx['form'] = AuthorForm(instance=author)
        else:
            ctx['form'] = AuthorForm(request.POST)
    return render(request, 'forum/forum/cabinet.html', ctx)


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'forum/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'forum/product/detail.html',
                  {'product': product,
                   })


def index(request):
    all_books = Product.objects.all()  # 'SELECT * FROM wa_1_book;'
    return render(request, 'index.html', {})

def news_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "forum/forum/list.html", {"news": news})


def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "forum/forum/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})



