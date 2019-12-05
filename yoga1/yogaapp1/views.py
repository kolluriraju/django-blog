from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from yogaapp1.models import Post
from django.urls import reverse

# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list})

def post_detail_view(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
                           # status='published',
                           # publish_year=year,
                           # publish_month=month,
                           # publish_day=day)

    context = {
        'post': post
    }
    return render(request,"blog/post_detail.html",context)
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list})
