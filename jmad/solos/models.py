from django.db import models
from django.urls import reverse

from albums.models import Track, Album


class Solo(models.Model):
    slug = models.SlugField()
    track = models.ForeignKey(Track)
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('solo_detail', kwargs={
            'album': self.track.album.slug,
            'track': self.track.slug,
            'artist': self.slug
        })
