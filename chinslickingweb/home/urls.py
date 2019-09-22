# !-*- coding: utf-8 -*-
# @Author  : ching(opencoding@hotmail.com)
# @Date    : 2019/05/02
# @Link    : www.cnblogs.com/ching126/ or blog.csdn.net/chenhongwu666
# @Version : 
# @Desc    :

from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('king/', views.king, name='king'),
    path('contact/', views.contact, name='contact'),
    path('partner/', views.partner, name='partner'),
    path('job_list/', views.job_list, name='job_list'),
    path('layer_coupon_form/', views.layer_coupon_form, name='layer_coupon_form'),

    url('add_coupon/', views.add_coupon, name='add_coupon'),
    url('add_watering_qty/', views.add_watering_qty, name='add_watering_qty'),

    url(r'^product_list/', views.product_list, name='product_list'),
    url(r'^product_detail/(?P<id>\d+)/$', views.product_detail, name='product_detail'),

    # url(r'^news_list/(?P<mtype>\S+)/$', views.news_list, name='news_list'),
    url(r'^news_list/$', views.news_list, name='news_list'),
    url(r'^news_detail/(?P<id>\d+)/$', views.news_detail, name='news_detail'),

    url(r'^resp_list/$', views.resp_list, name='resp_list'),
    url(r'^resp_detail/(?P<id>\d+)/$', views.resp_detail, name='resp_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
