from django.contrib import admin
from django.urls import path,include # import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist.urls'))  # add this line
]
 