from django.urls import path

from .views import CreateShortURLApi, ShortUrlRedirectView

app_name = "shortener"

urlpatterns = [
    path("api/v1/urls/", CreateShortURLApi.as_view(), name="shorten_url"),
    path("<str:short_url>", ShortUrlRedirectView.as_view(), name="redirect"),
]
