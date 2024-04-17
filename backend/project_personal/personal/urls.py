from django.urls import path
from . import views

urlpatterns = [
    # path personal
    path('personal/list/', views.PersonalView.as_view({'get': 'list_all'})),
    path('personal/create/', views.PersonalView.as_view({'post': 'create'})),
    path('personal/<int:pk>/', views.PersonalView.as_view({'get': 'retrieve'})),
    # path appointment
    path('appointment/list/', views.AppointmentView.as_view({'get': 'list_all'})),
    path('appointment/create/', views.AppointmentView.as_view({'post': 'create'})),
    path('appointment/<int:pk>/', views.AppointmentView.as_view({'get': 'retrieve'})),
    path('appointment/list/<int:prof>/', views.AppointmentView.as_view({'get': 'list_from_personal'})),
    # path patient
    path('patient/list/', views.PatientView.as_view({'get': 'list_all'})),
    path('patient/create/', views.PatientView.as_view({'post': 'create'})),
    path('patient/<int:pk>/', views.PatientView.as_view({'get': 'retrieve'})),
    path('patient/list/<int:prof>/', views.PatientView.as_view({'get': 'list_from_personal'})),
    # path evaluation
    path("evaluation/list/", views.EvaluationView.as_view(actions={"get": "list_all"})),
    path("evaluation/create/", views.EvaluationView.as_view(actions={"post": "create"})),
    path("evaluation/<int:pk>/", views.EvaluationView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("evaluation_from_patient/<int:pk>/", views.EvaluationView.as_view(actions={"get": "retrieve_by_patient"})),
    # path evolution
    path("evolution/list/", views.EvolutionView.as_view(actions={"get": "list_all"})),
    path("evolution/create/", views.EvolutionView.as_view(actions={"post": "create"})),
    path("evolution/<int:pk>/", views.EvolutionView.as_view(actions={"get": "retrieve", "delete": "delete", "put": "update"})),
    path("evolution_from_patient/<int:pk>/", views.EvolutionView.as_view(actions={"get": "retrieve_by_patient"})),
    #path diet
    path("diet/list/", views.DietView.as_view(actions={"get": "list_all"})),
    path("diet/create/", views.DietView.as_view(actions={"post": "create"})),
    path("diet/<int:pk>/", views.DietView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("diet_from_patient/<int:pk>/", views.DietView.as_view(actions={"get": "retrieve_by_patient"})),
    #path training
    path("training/list/", views.DietView.as_view(actions={"get": "list_all"})),
    path("training/create/", views.DietView.as_view(actions={"post": "create"})),
    path("training/<int:pk>/", views.DietView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("training_from_patient/<int:pk>/", views.DietView.as_view(actions={"get": "retrieve_by_patient"})),
]
