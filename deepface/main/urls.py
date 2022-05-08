from django.urls import path

from .views import index, recognize, upload

urlpatterns = [
    path('', upload),
    path('second/', index),
    path('second/url/to/save/image', recognize)
]
