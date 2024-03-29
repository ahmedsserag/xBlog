"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blogApp import views
from django.contrib.sitemaps.views import sitemap
from blogApp.sitemaps import BlogSitemap

sitemaps = {
    "posts": BlogSitemap,
}

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('tag/<slug:tag_slug>', views.home, name='tag'),
    path('blog/<int:year>/<int:month>/<slug:slug>/', views.single, name='single-post'),
    path('new/', views.new, name='new-post'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]
