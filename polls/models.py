from django.db import models


STATUS = ((0, "Draft"), (1, "Published"))


class Poll(models.Model):
    approved = models.BooleanField(default=False)
    question = models.TextField()
    choice_one = models.CharField(max_length=30)
    choice_two = models.CharField(max_length=30)
    choice_three = models.CharField(max_length=30)
    choice_one_count = models.IntegerField(default=0)
    choice_two_count = models.IntegerField(default=0)
    choice_three_count = models.IntegerField(default=0)

    def total(self):
        return self.choice_one_count + self.choice_two_count + self.choice_three_count  # noqa
