from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Vaccine(models.Model):
    name = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, blank=True, null=True)
    company = models.CharField(max_length=225)
    count_immunization = models.IntegerField(default=1, blank=True, null=True)
    description = models.TextField(max_length=1500)
    available = models.IntegerField(default=0)
    in_holding = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_in_stock(self):
        return self.available + self.in_holding

    def save(self, *args, **kwargs):
        if self.available < 1:
            self.availability = False
        else:
            self.availability = True
        super().save(*args, **kwargs)


def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == "":
        new_slug = slugify(instance.name)
        klass = instance.__class__
        qs = klass.objects.filter(slug__icontains=new_slug).exclude(id=instance.id)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f"{new_slug}-{qs.count()}"


pre_save.connect(slugify_pre_save, sender=Vaccine)
