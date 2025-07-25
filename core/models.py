from django.db import models
from django.utils.crypto import get_random_string

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = get_random_string(6)  # generates short code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
