from django.shortcuts import render,redirect
from .models import Blogger,BlogPost
from .forms import BloggerForm,BlogPostForm

# Create your views here.
def index(request):
    """博客的主页"""
    return render(request,'blogs/index.html')

def bloggers(request):
    """显示所有博客"""
    bloggers = Blogger.objects.order_by('date_added')
    context = {'bloggers':bloggers}
    return render(request,'blogs/bloggers.html',context)

def blogger(request,blogger_id):
    """显示单篇博客及其所有的内容"""
    blogger = Blogger.objects.get(id=blogger_id)
    blogposts = blogger.blogpost_set.order_by('-date_added')
    context = {'blogger': blogger, 'blogposts': blogposts}
    return render(request, 'blogs/blogger.html', context)

def new_blogger(request):
    """添加新博客"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = BloggerForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BloggerForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:bloggers')
        
    # 显示空表单或者指出表单数据无效
    context = {'form': form}
    return render(request, 'blogs/new_blogger.html', context)

def new_blogpost(request, blogger_id):
    """在特定的主题中添加新条目"""
    blogger = Blogger.objects.get(id=blogger_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = BlogPostForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.blogger = blogger
            new_blogpost.save()
            return redirect('blogs:blogger', blogger_id=blogger_id)
    #显示空表单或指出表单数据无效 
    context = {'blogger': blogger, 'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

def edit_blogpost(request, blogpost_id):
    """编辑既有条目"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogger = blogpost.blogger

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = BlogPostForm(instance=blogpost)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogger', blogger_id=blogger.id)
        
    context = {'blogpost': blogpost, 'blogger': blogger, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
