from django.conf.urls import url
from howdy import views

urlpatterns =[
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), #add this /about/ route
]
