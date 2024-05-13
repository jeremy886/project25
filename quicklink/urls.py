# quicklink/urls.py
# QuickLink Method 1 - RedirectView
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('google/', RedirectView.as_view(url="https://www.google.com.au/"), name="gogoogle"),
    path('django/', RedirectView.as_view(url="https://www.djangoproject.com/"), name="godjango"),
    # your turn 1
]

# QuickLink Method 2 - HttpResponse
from django.http import HttpResponse


def secret_view(request):
    return HttpResponse("<p>Why do programmers prefer dark mode?<br/>Because light attracts bugs!</p>")


urlpatterns += [
    path('secret/', secret_view, name="mysecret"),
]


# QuickLink Method 3 - redirect function
from django.shortcuts import redirect, render
from .views import go_pokemon
def go_admin(request):
    # Example of redirecting to an internal Django admin page by URL name
    return redirect('admin:index')


urlpatterns += [
    path('admin/', go_admin, name="goadmin"),
    path('pokemon/<str:pokemon_name>/', go_pokemon, name="gopokemon")
]