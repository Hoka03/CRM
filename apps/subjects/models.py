from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    price = models.DecimalField(max_digits=20, decimal_places=2, help_text='Add in UZS')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    url = models.URLField(max_length=150, blank=True, null=True)
    published_at = models.DateField()

    def __str__(self):
        return self.name
