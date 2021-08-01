from django.db import models

class SampleName(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter your first name')
    last_name = models.CharField(max_length=50, help_text='Enter your last name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'