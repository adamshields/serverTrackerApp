from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Publisher(models.Model):
    name     = models.CharField(max_length=200, unique=True, verbose_name='Software Publisher Name')
    slug     = models.SlugField(unique=True, null=True, verbose_name='Software Publisher Slug')
    status   = models.BooleanField(default=False, verbose_name='Active')
           
    class Meta:
        verbose_name = ('Publisher')
        verbose_name_plural = ('Publishers')
        ordering = ('id', 'name')

    def __str__(self):
        return self.name

class Software(models.Model):
    name            = models.CharField(max_length=200, unique=True, verbose_name='Software Name')
    slug            = models.SlugField(unique=True, null=True)
    status          = models.BooleanField(default=False, verbose_name='Active')
    version         = models.CharField(max_length=200, unique=True, verbose_name='Software Version')
    publisher       = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Software')
        verbose_name_plural = ('Software')
        ordering = ('id', 'name')
        unique_together = ('name', 'publisher')

    def __str__(self):
        return self.name


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Version, self).save(*args, **kwargs)

def pre_save_software(sender, instance, *args, **kwargs):
	slug = slugify(instance.publisher) + "-" + slugify(instance.name)
	instance.slug = slug

pre_save.connect(pre_save_software, sender=Software)


class Server(models.Model):
    name            = models.CharField(max_length=200, unique=True, verbose_name='Server Name')
    slug            = models.SlugField(unique=True, null=True)
    status          = models.BooleanField(default=False, verbose_name='Active')
    software        = models.ManyToManyField(Software, blank=True)


    class Meta:
        verbose_name = ('Server')
        verbose_name_plural = ('Servers')
        ordering = ('id', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Server, self).save(*args, **kwargs)


        """

        """