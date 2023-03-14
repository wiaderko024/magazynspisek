from django.urls import path
from .views import articles_list, articles_details

urlpatterns = [
    path('', articles_list, name='articles-list'),
    path('<int:pk>/', articles_details, name='articles-details')
]
