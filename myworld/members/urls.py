from django.urls import path
from . import views
from django.urls import path, include # new

app_name = "main"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add, name = 'add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    # user ragistration path
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register")

]
