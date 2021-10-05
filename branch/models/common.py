from django.db import models


class CommonBaseModel(models.Model):
    title = models.CharField(max_length=256, unique=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}.{1}".format(self.id, self.title)

    class Meta:
        abstract = True
