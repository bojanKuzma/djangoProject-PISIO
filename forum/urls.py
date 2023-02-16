from django.urls import path

from forum.views import HomeView, MyQuestionsView, CreateQuestionView, DetailQuestionView, CreateAnswerView, \
    DeleteQuestionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my_questions', MyQuestionsView.as_view(), name='my_questions'),
    path('question/create', CreateQuestionView.as_view(), name='create_question'),
    path('question/<int:pk>', DetailQuestionView.as_view(), name='question_detail'),
    path('question/<int:pk>/delete', DeleteQuestionView.as_view(), name='delete_question'),
    path('question/<int:question_id>/anwser', CreateAnswerView.as_view(), name='add_answer'),
]
