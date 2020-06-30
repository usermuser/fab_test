from django.urls import path

from .views import PollsView, QuestionsView

app_name = 'poll_app'

urlpatterns = [
    # добавление/изменение/удаление опросов.
    path('v1/polls', PollsView.as_view(), name='create_or_get_polls'),
    path('v1/polls/<int:pk>', PollsView.as_view(), name='update_or_delete_polls'),

    # добавление/изменение/удаление вопросов в опросе
    path('v1/polls/<int:pk>/questions', QuestionsView.as_view(), name='create_or_get_questions'),
    path('v1/polls/<int:pk>/questions/<int:pk>', QuestionsView.as_view(), name='create_or_get_questions'),

]