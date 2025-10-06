from django.urls import path
from services.views import CreateListServices, UpdateDeleteDetailServices

urlpatterns = [
    path('services/', CreateListServices.as_view(), name='create_list_services'),
    path('services/<int:pk>', UpdateDeleteDetailServices.as_view(), name='update_delete_detail_services'),
]