from django.contrib import admin
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('edit/<int:ticket_id>', views.edit_ticket_view,name='edit'),
    path('submit/', views.submit_ticket_view,name='submit'),
    path('ticket/<int:ticket_id>', views.ticket_view,name='ticket_view'),
    path('user/<int:user_id>', views.user_detail_view,name='user_view'),
    path('admin/', admin.site.urls),
    path('login/', views.login,name='login'),
    path('claim/<int:ticket_id>',views.claim_ticket,name='claim'),
    path('complete/<int:ticket_id>',views.complete_ticket, name='complete'),
    path('invalid/<int:ticket_id>',views.invalid_ticket, name='invalid'),
]
