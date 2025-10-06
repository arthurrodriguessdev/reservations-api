from django.urls import path
from staff.views import CreateListStaff, UpdateDeleteDetailStaff

urlpatterns = [
    path('staff/', CreateListStaff.as_view(), name='create_list_staff'),
    path('staff/<int:pk>', UpdateDeleteDetailStaff.as_view(), name='update_delete_detail_staff'),
]