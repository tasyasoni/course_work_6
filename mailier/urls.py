from django.urls import path
from django.views.decorators.cache import cache_page

from mailier import views
from mailier.apps import MailierConfig
from mailier.views import ClientListView, ClientCreateView, ClientUpdateView, \
    MailingListView, MailingDeleteView, MailingCreateView, MailingUpdateView, LogfileListView, \
    MsgListView, MsgDeleteView, MsgCreateView, MsgUpdateView

#from mailier.views import

app_name = MailierConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('client/form/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('mailing/form/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('logfile/list/', LogfileListView.as_view(), name='logfile_list'),
    path('msg/form/', MsgCreateView.as_view(), name='msg_create'),
    path('msg/update/<int:pk>/', MsgUpdateView.as_view(), name='msg_update'),
    path('msg/list/', MsgListView.as_view(), name='msg_list'),
    path('msg/delete/<int:pk>/', MsgDeleteView.as_view(), name='msg_delete'),


    # path('detail/<int:pk>/', cache_page(30)(ProductDetailView.as_view()), name='detail'),

    # path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    # path('toggle/<int:pk>/', toggle_publish, name='toggle'),
]