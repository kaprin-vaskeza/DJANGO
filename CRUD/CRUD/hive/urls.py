from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('hives', ProductViewSet.as_view({
        'get': 'get_all',
        'post': 'save'
    })),
    path('hives/<str:pk>', ProductViewSet.as_view({
        'get': 'get',
        'put': 'update',
        'delete': 'delete'
    })),
    # path('user', UserAPIView.as_view())
]