from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('task/create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
]
