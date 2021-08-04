from django.db import models
from datetime import date

class Practice(models.Model):
    practice_name = models.CharField(max_length=30)
    current_value = models.IntegerField(default = 0)
    total_value = models.IntegerField(default = 111111)

    def __str__(self):
        return self.practice_name


class Session(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    session_value = models.IntegerField(null=True)
    session_date = models.DateTimeField(default=date.today)

    def __str__(self):
        return f"{self.practice.practice_name}: {self.session_value} mantras, date: {self.session_date}"

