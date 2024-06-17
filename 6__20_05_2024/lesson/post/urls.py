from django.urls import  path
from .views import *

urlpatterns = [
    path('', posts, name='post'),
    path('post/<int:post_id>', post_info, name='post_info'),

    path('add_post', add_post, name='add_post'),
    path('add_multi_post', add_multi_post, name='add_multi_post'),
    path('update_titles', update_titles, name='update_titles'),
    path('delete_ne_chetniy_post', delete_ne_chetniy_post, name='delete_ne_chetniy_post'),
]