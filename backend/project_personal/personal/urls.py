from django.urls import path, re_path
from . import views

urlpatterns = [
    path('personal/list/', views.PersonalView.as_view({'get': 'list_all'})),
    path('personal/create/', views.PersonalView.as_view({'post': 'create'})),
    path('personal/<int:pk>/', views.PersonalView.as_view({'get': 'retrieve'})),
    path('appointment/list/', views.AppointmentView.as_view({'get': 'list_all'})),
    path('appointment/create/', views.AppointmentView.as_view({'post': 'create'})),
    path('appointment/<int:pk>/', views.AppointmentView.as_view({'get': 'retrieve'})),
    path('appointment/list/<int:prof>/', views.AppointmentView.as_view({'get': 'list_from_personal'})),
    path('patient/list/', views.PatientView.as_view({'get': 'list_all'})),
    path('patient/create/', views.PatientView.as_view({'post': 'create'})),
    path('patient/<int:pk>/', views.PatientView.as_view({'get': 'retrieve'})),
    path('patient/list-group/', views.PatientView.as_view({'post': 'list_from_personal'})),
]
