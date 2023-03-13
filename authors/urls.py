from django.urls import path
from .views import authors_list, authors_details

urlpatterns = [
    path('', authors_list, name='authors-list'),
    path('<int:pk>/', authors_details, name='authors-details')
]
