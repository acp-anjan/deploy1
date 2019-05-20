from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    name_hospital = models.CharField(max_length = 100)
    location_hospital = models.CharField(max_length = 256)

    def __str__(self):
        return self.name_hospital

    def get_absolute_url(self):
        return reverse("app_cbv:detail", kwargs={"pk": self.pk})
    

class PatientQuery(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    patient_query = models.TextField()
    hospital = models.ForeignKey(Hospital, related_name='patient_query', on_delete = models.CASCADE)

    def __str__(self):
        return self.patient_name

