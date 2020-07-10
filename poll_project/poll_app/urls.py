from django.urls import path

from .views import PollsView, QuestionsView

app_name = 'poll_app'

urlpatterns = [
    # добавление/изменение/удаление опросов.
    path('v1/polls', PollsView.as_view(), name='create_or_get_polls'),
    path('v1/polls/<int:pk>', PollsView.as_view(), name='update_or_delete_polls'),

    # прохождение опроса
    path('v1/polls/<int:pk>/questions', QuestionsView.as_view(), name='get_or_answer_questions'),


    # добавление/изменение/удаление вопросов в опросе
    path('v1/questions', QuestionsView.as_view(), name='create_or_get_questions'),
    path('v1/questions/<int:pk>', QuestionsView.as_view(), name='create_or_get_questions'),

]