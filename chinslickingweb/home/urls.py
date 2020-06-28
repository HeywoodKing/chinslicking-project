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
    url(r'^about', views.about, name='about'),
    url(r'^king', views.king, name='king'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^partner', views.partner, name='partner'),
    url(r'^job_list', views.job_list, name='job_list'),
    url(r'^layer_coupon_form', views.layer_coupon_form, name='layer_coupon_form'),

    url(r'^add_coupon', views.add_coupon, name='add_coupon'),
    url(r'^add_watering_qty', views.add_watering_qty, name='add_watering_qty'),

    url(r'^product_list', views.product_list, name='product_list'),
    url(r'^product_detail/(?P<id>\d+)', views.product_detail, name='product_detail'),

    # url(r'^news_list/(?P<mtype>\S+)/$', views.news_list, name='news_list'),
    url(r'^news_list', views.news_list, name='news_list'),
    url(r'^news_detail/(?P<id>\d+)', views.news_detail, name='news_detail'),

    url(r'^compet_list/(?P<id>\d+)', views.compet_list, name='compet_list'),
    url(r'^compet_enroll', views.compet_enroll, name='compet_enroll'),

    url('', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^home', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
