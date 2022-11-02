from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_study, name = 'start_study'),
    path('finish/', views.finish_study, name = 'start_study'),
    path('check/', views.check_study, name = 'start_study'),
    path('memo/', views.create_memo, name = 'create_memo'),
    path('log/', views.get_log, name = 'get_log'),
    path('callback/', views.callback_log, name = 'callback_log'),
]