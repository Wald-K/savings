from django.urls import path
from . import views




app_name = 'savings'

urlpatterns = [
    path('', views.test),
    path('banks/', views.BankList.as_view(), name='bank_list'),
    path('banks/new/', views.BankCreate.as_view(), name='bank_new'),
    path('banks/delete/<int:pk>', views.BankDelete.as_view(), name='bank_delete'),
    path('banks/update/<int:pk>', views.BankUpdate.as_view(), name='bank_update'),


    path('clients/', views.client_list, name='client_list' ),
    path('clients/new/', views.client_create, name='client_new'),
    path('clients/update/<int:pk>', views.client_update, name='client_update'),
    path('clients/delete/<int:pk>', views.client_delete, name='client_delete'),
    # display information about client and his all deposits 
    path('clients/detail/<int:pk>', views.client_detail, name='client_detail'),

    # deposit_status: hold, history
    # path('deposits/new/', views.DepositCreate.as_view(), name='deposit_new'),


    # proba z deposit_new as function
    path('deposits/new/', views.deposit_create, name='deposit_new'),
    path('deposits/<str:deposit_status>', views.deposit_list, name='deposit_list'),





]





