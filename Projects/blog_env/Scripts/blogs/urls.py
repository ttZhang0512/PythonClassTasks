"""定义blogs的URL模式"""

from django.urls import path
from . import views

app_name='blogs'
urlpatterns = [
    # 主页
    path('',views.index,name='index'),
    # 显示所有主题的页面
    path('bloggers/',views.bloggers,name='bloggers'),
    # 具体博客界面
    path('bloggers/<int:blogger_id>',views.blogger,name='blogger'),
    # 用于添加新博客的网页
    path('new_blogger/',views.new_blogger,name='new_blogger'),
    # 用于添加新博文的页面
    path('new_blogpost/<int:blogger_id>/',views.new_blogpost,name='new_blogpost'),
    # 用于编辑条目的页面
    path('edit_blogpost/<int:blogpost_id>/',views.edit_blogpost,name='edit_blogpost'),
]
