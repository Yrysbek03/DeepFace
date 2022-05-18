from django.urls import path

from .views import index, recognize, upload

urlpatterns = [
    path('', index),
    path('second/', upload),
    path('url/to/save/image', recognize)
]
