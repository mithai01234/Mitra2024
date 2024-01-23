from django.urls import path
from . import views
from .views import  registerlist, view_item,waletlist
from .views import UserViewSet
from .views import *
urlpatterns = [
    path('api/user-delete/', UserViewSet.as_view({'delete': 'destroy'}), name='user-delete'),
    path('get-customusers/', views.CustomUserList.as_view(), name='get-customusers'),
    path('backend/userlist/', registerlist, name="userlist"),
    path('backend/waletlist/', waletlist, name="waletlist"),
    path('backend/userlist/view_item/<int:myid>/', view_item, name="userlist/view_item"),
    path('backend/userlist/activate_catagory/<int:catagory_id>/', activate_catagory,name='userlist/activate_catagory'),
    path('backend/userlist/deactivate_catagory/<int:catagory_id>/', deactivate_catagory,name='userlist/deactivate_catagory'),
    path('backend/userlist/suspend_user/<int:catagory_id>/', suspend_user, name='userlist/suspend_user'),
]
