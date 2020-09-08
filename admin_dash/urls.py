from django.urls import path
from . import views
urlpatterns = [
    path('', views.exam_admin_home, name='exam_admin_home'),
    path('add_question/', views.new_question, name='add_question'),
    path('view_questions/', views.view_question, name='view_question'),
    path('edit_questions/<int:qid>', views.edit_questions, name='edit_questions'),
    path('delete_questions/<int:qid>', views.delete_questions, name='delete_questions'),
    path('view_results/', views.view_results, name='view_results'),
    path('students/', views.students, name='student_list'),
    path('answerd_questions/<int:stdid>',views.answerd_questions,name='answerd_questions'),
    path('result/<int:stdid>',views.result,name='result'),
    path('generate', views.generate, name='generate_report'),
     
    
]

