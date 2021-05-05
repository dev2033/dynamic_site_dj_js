from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Post


class BaseView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        posts = Post.objects.all()[:2]
        context = {'posts': posts}
        return render(request, 'mainapp/index.html', context=context)


class DynamicPostsLoad(View):

    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET.get('lastPostId')
        more_posts = Post.objects.filter(pk__gt=int(last_post_id)).values('id', 'title')[:2]
        print(more_posts)

        if not more_posts:
            return JsonResponse({'data': False})

        data = []
        for post in more_posts:
            obj = {
                'id': post['id'],
                'title': post['title'],
            }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data': data})

