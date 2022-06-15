from django.urls import URLPattern


from django.urls import path

from pet.models import Pet

from .views import PetList

urlpatterns = [path("", PetList.as_view())]
