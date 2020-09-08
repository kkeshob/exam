from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),#should be home page
    
    path('login/', views.login, name='login'),
    path('home/', views.student_home, name='student_home'),
    path('logout/', views.logout_view, name='logout'),
    path('Questions/<int:qno>', views.exam_home, name='exam_home'),
]

