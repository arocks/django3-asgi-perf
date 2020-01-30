from django.contrib import admin
from django.urls import include, path
from django.views import generic

urlpatterns = [
    path("", generic.TemplateView.as_view(template_name="index.html")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
