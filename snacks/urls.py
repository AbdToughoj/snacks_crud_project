from django.urls import path
from .views import SnacksListView, SnackDetailsView, SnackCreateView, SnackUpdateView ,SnackDeleteView

urlpatterns = [
    path('', SnacksListView.as_view(), name= 'snacks' ),
    path('<int:pk>/',SnackDetailsView.as_view(), name='snack_detail'),
    path('create/',SnackCreateView.as_view(), name = 'snack_create'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = 'snack_update'),
    path('delete/<int:pk>/',SnackDeleteView.as_view(), name = 'snack_delete'),



]