from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    question_categories = models.CharField('subject', max_length=50)
    message = models.TextField('Write your message here', max_length=3000)

    def __str__(self):
        return self.email
