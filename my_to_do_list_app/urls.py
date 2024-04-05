from django.urls import path
from my_to_do_list_app import views

urlpatterns = [
    path('add-view-page/', views.to_do_list_view, name='add_view'),
]
