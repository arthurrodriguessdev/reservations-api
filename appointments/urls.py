from django.urls import path
from appointments.views import CreateListAppointment, UpdateDeleteDetailAppointment

urlpatterns = [
    path('appointments/', CreateListAppointment.as_view(), name='create_list_appointments'),
    path('appointments/<int:pk>', UpdateDeleteDetailAppointment.as_view(), name='update_delete_detail_appointments'),
]