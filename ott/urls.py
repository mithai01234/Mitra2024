# yourapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UploadedContentViewSet, Ottlist, add_account, activate_product, deactivate_product, delete_item, \
    edit_account,add_category,add_subcategory,category_list,subcategory_list
from .views import get_subcategories,CategoryViewSet,SubcategoryViewSet,OttByCategoryAndSubcategoryViewSet

urlpatterns = [
    path('api/ott', UploadedContentViewSet.as_view({'get': 'get_all_uploads'}), name='all-uploads'),
    path('api/lang/', CategoryViewSet.as_view({'get': 'list'}), name='lang'),
    path('api/lang/detail/', SubcategoryViewSet.as_view({'get': 'list'}), name='lang-detail'),
    path('api/ottbylang/', OttByCategoryAndSubcategoryViewSet.as_view({'get': 'list'}), name='otts'),
    path('api/ott/', UploadedContentViewSet.as_view({'get': 'get_video_by_id'}), name='get-video-by-id'),
    path('edit/<int:ott_id>/', edit_account, name='ott/edit'),  # <int:ott_id> captures the Ott instance I
    path('backend/add_ott/', add_account, name="add_accounts"),
    path('get-subcategories/', get_subcategories, name='get_subcategories'),
    path('backend/add_category/', add_category, name="add_category"),
    path('backend/add_subcategory/', add_subcategory, name="add_subcategory"),
    path('backend/category_list/', category_list, name='category_list'),
    path('backend/subcategory_list/', subcategory_list, name='subcategory_list'),
    path('backend/ottlist/', Ottlist, name="ottlist"),
    path('backend/ottlist/activate_product/<int:id>/', activate_product, name='addcustomer/activate_product'),
    path('backend/ottlist/deactivate_product/<int:id>/', deactivate_product,name='addcustomer/deactivate_product'),
    path('backend/ottlist/delete_item/<int:myid>/', delete_item, name="addroles/delete_item"),
]
