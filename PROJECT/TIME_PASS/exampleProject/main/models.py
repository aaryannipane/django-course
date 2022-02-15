from django.db import models
from django.forms import CharField

class SubPlan(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return self.title 

class SubPlanFeature(models.Model):
    subplan = models.ForeignKey(SubPlan, on_delete=models.CASCADE, null=True)
    feature = CharField(max_length=150)

