
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.asset_form, name='asset_insert'), #get and post request for insert
    path('<int:id>/', views.asset_form, name='asset_update'), #get and post request for update
    path('delete/<int:id>/', views.asset_delete, name='asset_delete'), #get request for delete
    path('list/',views.asset_list, name='asset_list'), #get and post for display
]