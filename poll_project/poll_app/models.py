from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название опроса', db_index=True, unique=True)
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата старта опроса')
    end_date = models.DateField(verbose_name='Дата окончания опроса')
    description = models.TextField(verbose_name='Описание опроса')

    class Meta:
        ordering = ('start_date',)
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.name} Дата старта опроса: {self.start_date}'


class Question(models.Model):
    CHOICES_TYPES = [
        ('Text answer', 'Ответ текстом'),
        ('Single checkbox answer', 'Ответ с выбором одного варианта'),
        ('Multiple checkbox answer', 'Ответ с выбором нескольких вариантов'),

    ]
    text = models.TextField(verbose_name='Текст вопроса')
    poll = models.ForeignKey('Poll', related_name='questions', on_delete=models.CASCADE)
    type = models.CharField(choices=)


    def __str__(self):
        return self.text[:20]




