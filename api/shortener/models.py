from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=2000)
    short_url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url[:30]} -> {self.short_url}"

    class Meta:
        verbose_name = "URLs"
        verbose_name_plural = "URLs"

    def save(self, *args, **kwargs):
        if not len(URL.objects.filter(short_url=self.short_url)):
            super().save(*args, **kwargs)
