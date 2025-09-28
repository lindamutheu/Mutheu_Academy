from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration = models.CharField(max_length=10)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

