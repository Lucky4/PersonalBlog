from django.shortcuts import render
from PersonalBlog_app.models import User, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect, HttpRequest, HttpResponse
from PersonalBlog_app.forms import SearchForm
from django.core.urlresolvers import reverse


def index(request, page=1):
    context_dict = {}

    try:
        # Retrieve all of the admin posts objects.
        user = User.objects.get(pk=1)
        posts = Post.objects.all().filter(user=user)

        # Retrieve Recent 3 post title.
        recents = Post.objects.order_by('create_time')[:3]

        # Retrieve all post's date, which used to archieve.
        date = Post.objects.all().values('create_time')
        for date_item in date:
            date_item['year'] = date_item['create_time'].year
            date_item['month'] = date_item['create_time'].month

        # Clear the whitespace and make the tag into a list.
        for post in posts:
            post.tags = post.tags.split(',')

        # Paginate by the page.
        paginator = Paginator(posts, 2)
        page = request.GET.get('page')
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except User.DoesNotExist:
        raise Http404("User does not exists.")

    # This is the searchform handle.
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            title = request.POST['title']
            return HttpResponseRedirect(reverse('search_title', args=[''.join(title)]))
    else:
        form = SearchForm()

    # Add our results to the template under name posts.  
    context_dict['posts'] = posts
    context_dict['form'] = form
    context_dict['recents'] = recents
    context_dict['date'] = date
    return render(request, 'PersonalBlog/index.html', context_dict)

def detail(request, post_title_slug):
    try:
        # Retrieve the post base on the slug.
        post = Post.objects.get(slug=post_title_slug)
        post.tags = post.tags.split(',')
    except Post.DoesNotExist:
        raise Http404("Post does not exists.") 
    return render(request, 'PersonalBlog/post.html', {'post': post})

def search_title(request, keys):
    title = keys
    results = []
    try:
        # Retrieve all the posts if request title in posts's title and take the post into the result. 
        posts = Post.objects.all()
        for post in posts:
            if title in post.title:
                results.append(post)
                post.tags = post.tags.split(',')
    except Post.DoesNotExist:
        raise Http404("Post does not exists.")
    return render(request, 'PersonalBlog/search_title.html', {'results': results})

def search_tag(request, tag):
    try:
        posts = Post.objects.filter(tags__contains=tag)
    except Post.DoesNotExist:
        raise Http404("Post.does not exists.")
    return render(request, 'PersonalBlog/search_tag.html', {'posts': posts})

def about(request):
    return render(request, 'PersonalBlog/about.html')
