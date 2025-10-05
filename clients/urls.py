from django.urls import path
from clients.views import CreateListClients, UpdateDeleteDetailClients

urlpatterns = [
    path('clients/', CreateListClients.as_view(), name='create_list_clients'),
    path('clients/<int:pk>', UpdateDeleteDetailClients.as_view(), name='update_delete_detail_clients'),
]