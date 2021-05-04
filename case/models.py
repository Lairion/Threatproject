from django.db import models

# Create your models here.
class Case(models.Model):

    name = models.CharField(max_length=100)
    message = models.TextField()


class CaseResult(models.Model):

    message = models.TextField()
    data_create = models.DateTimeField(auto_now=True)
    case = models.ForeignKey("Case", on_delete=models.CASCADE, related_name="results")

