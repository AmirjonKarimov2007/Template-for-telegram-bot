from django.db import models

# Create your models here.
class Music(models.Model):
    user_id = models.BigIntegerField(verbose_name='Telegram_id',unique=True)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    duration = models.DurationField()
    file = models.FileField(upload_to='music_files/')
    cover_image = models.ImageField(upload_to='cover_images/', null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
            return self.title