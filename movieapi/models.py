from django.db import models
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


def round_up_rating(instance, rate):
  if rate>10:
    rate=10
  elif rate<0:
    rate=0


class MovieDB(models.Model):
  name = models.CharField(max_length=100)
  rating = models.FloatField(validators=[round_up_rating])
  release = models.DateField()
  duration = models.CharField(max_length=3)
  description = models.CharField(max_length=200)

  
  def __str__(self):
    return f"{self.name} | {self.duration}"

  class Meta:
    verbose_name = "Movies"
    unique_together = [("name", "release")]
    ordering = ("-rating", "-release", "name")
