from django.urls import path
from.import views

urlpatterns=[
    path('SE/', views.ShowEmployee.as_view(), name='showEmp_url'),
    path('AE/', views.AddEmployee.as_view(), name='addEmp_url'),
    path('UE/<int:pk>/', views.UpdateEmployee.as_view(), name='update_url'),
    path('DE/<int:pk>/', views.DeleteEmployee.as_view(), name='delete_url'),
]