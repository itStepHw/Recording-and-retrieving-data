from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Post
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    print('hello')

    # cat = Category.objects.get(pk=1)
    # cat = Category.objects.get(pk__gte=2)
    # cat = get_object_or_404(Category, name='asasdsad')

    # print(cat)

    # post = Post(
    #     title='title 1',
    #     category=cat
    # )

    # post.save()

    # post = Post.objects.create(title='title 2', category=cat)
    # print(post)

    # post = Post.objects.get(pk=1)
    # post.description = 'TEST'
    # post.content = 'TEEEEEEEEEEEEEST'
    # post.save()

    # post, _ = Post.objects.get_or_create(title="title new", category=cat)
    # post, _ = Post.objects.get_or_create(title="title new2", defaults={
    #     "category": cat,
    #     'description': 'eeeeeeeeeeeeeeeeeeeeeeee'
    # })

    # post, _ = Post.objects.update_or_create(title='title new', defaults={
    #     "content": 'sssssssssssssss',
    #     'is_published': True
    # })
    #
    # print(post)
    # post.description = 'asdasdasdasdsa'
    # post.save()

    # data1 = [
    #     {
    #         'title': 'title25',
    #         'category': cat,
    #     }
    # ]

    # data = [
    #     Post(title='title6', category=cat),
    #     Post(title='title7', category=cat),
    #     Post(title='title8', category=cat),
    #     Post(title='title9', category=cat),
    # ]

    # data = list(map(lambda i: Post(**i), data1))
    #
    # Post.objects.bulk_create(data)

    return HttpResponse("success")


def posts(request):
    # data = Post.objects.all()
    data = Post.objects.order_by('-id').all()


    return render(request, 'post/index.html', context={"data": data})


def post_info(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'post/post_info.html', context={'post': post})


def add_post(request):
    categ = Category.objects.first()
    if categ:
        Post.objects.create(
            title="Один пост",
            content="Контент",
            description="Описание",
            category=categ,
            is_published=True,
        )
    return redirect('post')


def add_multi_post(request):
    categ = Category.objects.first()
    if categ:
        for i in range(10):
            Post.objects.create(
                title=f"Пост {i+1}",
                content=f"Контент поста {i+1}",
                description=f"Описание поста {i+1}",
                category=categ,
                is_published=True
            )
    return redirect('post')



def update_titles(request):
    posts = Post.objects.all()
    for post in posts:
        post.title = f"{post.title} ({post.id})"
        post.save()
    return redirect('post')



def delete_ne_chetniy_post(request):
    posts = Post.objects.all()
    for post in posts:
        title_parts = post.title.split()
        if title_parts and title_parts[-1].strip('()').isdigit():
            post_id = int(title_parts[-1].strip('()'))
            if post_id % 2 != 0:
                post.delete()
    return redirect('post')