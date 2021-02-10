from django.db import models
from django.urls import reverse


class Artwork(models.Model):
  title = models.CharField(max_length=50)
  year = models.IntegerField()
  medium = models.CharField(max_length=50)
  substrate = models.CharField(max_length=50)
  size = models.CharField(max_length=20)
  image = models.ImageField(upload_to="artwork/", blank=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('art_detail', args=[str(self.id)])

  class Meta:
    verbose_name_plural = "Artwork"
