from django.urls import path
from .apps import CoreConfig
from .views import FilesListView, AddFileView, UpdateFileView, DeleteFileView, \
    DetailFileView

app_name = CoreConfig.name

urlpatterns = [
    path('', FilesListView.as_view(), name='files_list_view'),
    path('add_file/', AddFileView.as_view(), name='add_file_view'),
    path('detail_file/<int:pk>/', DetailFileView.as_view(), name='detail_file_view'),
    path('update_file/<int:pk>/', UpdateFileView.as_view(), name='update_file_view'),
    path('delete_file/<int:pk>/', DeleteFileView.as_view(), name='delete_file_view')
]