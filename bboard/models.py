from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Content')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Published')

    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Notifications'
        verbose_name = 'Notification'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']
