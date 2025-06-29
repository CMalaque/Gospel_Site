from django.db import models

class SundayInfo(models.Model):
    sunday_title = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.sunday_title} | {self.date}"

class GospelReflection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    gospel_text = models.TextField()
    reflection_text = models.TextField()
    sunday_info = models.ForeignKey(SundayInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
