from django.urls import path
from .views import HomePageView, AboutPageView, CareerPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("careers/", CareerPageView.as_view(), name="careers"),
]