from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('contact', views.contact_us, name='contact'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('faq', views.faq, name='faq'),
    path('portfolio/<slug:p_slug>', views.portfolio_details),
    path('blog', views.blog, name='blog'),
    path('blog/<slug:b_slug>', views.blog_details)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
