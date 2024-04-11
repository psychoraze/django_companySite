from django.urls import path
from .views import home, about, contact
from django.urls import reverse_lazy

urlpatterns = [
    path("", reverse_lazy(home), name="home"),
    path("about/", reverse_lazy(about), name="about"),
    path("contact/", reverse_lazy(contact), name="contact"),
]
