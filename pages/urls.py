"""
URL configuration for my_project project.

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
from django.contrib import admin
from django.urls import path
from . import views
#from mysite import views

urlpatterns = [
    path('', views.mainpage),

    # about
    path('about/info/', views.company_info),
    path('about/map/', views.company_map),
    path('about/vision-mission/', views.company_mission),

    # support
    path('support/inquiry/', views.support_inquiry),
    path('support/feedback/', views.support_feedback),

    # faqs
    path('faqs/company/', views.faqs_company),
    path('faqs/product/', views.faqs_product),
]
