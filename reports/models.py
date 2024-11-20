from django.db import models


class Report(models.Model):
    description = models.TextField()
    vehicle_involved = models.CharField(max_length=252)
    other_vehicle_involved = models.CharField(
        max_length=252,
        null=True,
        blank=True
    )
    incident_type = models.CharField(max_length=252)
    cause = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='reports/%Y/%m')

    class Meta:
        ordering = ['-creation_time',]


    def __str__(self):
        return str(self.pk)
