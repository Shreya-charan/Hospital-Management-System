from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='user_login'),
    path('login/', user_login, name='user_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('view_doctors/', view_doctors, name='view_doctors'),
    path('delete_doctor/', delete_doctor, name='delete_doctors'),
    path('get-doctor-id/', get_doctor_id, name='get_doctor_id'),
    path('update_doctor/<str:d_id>/', update_doctors, name='update_doctor'),
    path('view_patients/', view_patients, name='view_patients'),
    path('delete_patients/', delete_patient, name='delete_patients'),
    path('get-patient-id/', get_patient_id, name='get_patient_id'),
    path('update_patient/<str:p_id>/', update_patients, name='update_patient'),
    path('create_patients/', create_patients, name='create_patients'),
    path('create_doctors/', create_doctors, name='create_doctors'),
    path('delete/failure/', delete_failure, name='delete_failure'),
    path('view_departments/', view_departments, name = 'view_departments'),
    path('create_departments/', create_departments, name= 'create_departments'),
    path('delete_department/', delete_department, name='delete_department'),
]
