from django.urls import path
from .views import upload_image, view_image

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('image/<int:image_id>/', view_image, name='view_image'),
]
