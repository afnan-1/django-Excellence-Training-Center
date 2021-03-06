"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import include

from django.urls import path, include
from django.contrib import admin

from django.views.generic import TemplateView

#importing from models apps

# from products.views import (
#     ProductListView,
#     product_list_view,
#     ProductDetailView,
#     ProductDetailSlugView,
#     product_detail_view,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView
#     )

from .views import *

urlpatterns = [
	path('', home_page, name='home'),
	path('about/', about_page, name='about'),
	path('contact/', contact_page, name='contact'),
	path('service/', service_page, name='service'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include("products.urls")),
    path('search/', include("search.urls")),
 #    path('featured/', ProductFeaturedListView.as_view()),
 #    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
 #    path('products/', ProductListView.as_view()),
 #    path('products-fbv/', product_list_view),
 #    # path('products/<int:pk>/', ProductDetailView.as_view()),
 #    path('products/<slug>/', ProductDetailSlugView.as_view()),
 #    path('products-fbv/<int:pk>/', product_detail_view),
	# path('call/', call_page),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)