from django.db import models


class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()


    objects = models.Manager()


    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"

    def __str__(self):
        return self.campus_name



