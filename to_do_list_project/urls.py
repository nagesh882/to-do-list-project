from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('to-do-list/', include('my_to_do_list_app.urls')),
]
