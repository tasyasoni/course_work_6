from django.urls import path
from django.views.decorators.cache import cache_page

from mailier import views
from mailier.apps import MailierConfig
from mailier.views import ClientListView, ClientCreateView, ClientUpdateView

#from mailier.views import

app_name = MailierConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('client/list/', ClientListView.as_view(), name='client_list'),
    # path('detail/<int:pk>/', cache_page(30)(ProductDetailView.as_view()), name='detail'),
    path('client/form/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    # path('toggle/<int:pk>/', toggle_publish, name='toggle'),
]