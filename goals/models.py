import uuid
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Goal(models.Model):
    # TODO: Fix UUID problem with postgresql
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    current = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    measure = models.CharField(max_length=100)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self):
        pass

    class Meta:
        managed = True
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

class Diary(models.Model):
    # TODO: Fix UUID problem with postgresql
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    data=models.TextField()
    
    def __str__(self):
        pass

    class Meta:
        managed = True
        verbose_name = 'Diary'
        verbose_name_plural = 'Diaries'

class ActionPlan(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_list = ArrayField(base_field=models.CharField(max_length=100))
    due_date = models.DateTimeField()

    class Meta:
        managed = True
        verbose_name = 'Action Plan'
        verbose_name_plural = 'Action Plans'