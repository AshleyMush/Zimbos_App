from django.urls import path
from zimbos_portal_app.views import (
    GroupListView,
    GroupDeleteView,
    GroupCreateView,
    GroupUpdateView
)

urlpatterns = [  
    # path('', home, name='home'),
    path('', GroupListView.as_view(), name='group_list'),
    path('group/create/', GroupCreateView.as_view(), name='create_group'),
    path('group/<int:pk>/update/', GroupUpdateView.as_view(), name='update_group'),
    path('group/<int:pk>/delete', GroupDeleteView.as_view(), name='delete_group'),
]