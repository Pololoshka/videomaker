from django.db import models


class Phrase(models.Model):
    text = models.CharField(unique=True, primary_key=True, max_length=50)

    objects = models.Manager()

    class Meta:
        db_table = "phrases"

    def __str__(self) -> str:
        return str(self.text)
