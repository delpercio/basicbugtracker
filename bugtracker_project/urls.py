from django.contrib import admin
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('', views.index),
    path('edit/', views.edit_ticket_view),
    path('submit/', views.submit_ticket_view),
    path('ticket/<int:ticket_id>', views.ticket_view),
    path('user/<int:user_id>', views.user_detail_view),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('claim/<int:ticket_id>',views.claim_ticket),
    path('complete/<int:ticket_id>',views.login),
]
