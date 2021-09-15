from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Publisher(models.Model):
    publisher_name     = models.CharField(max_length=200, unique=True, verbose_name='Publisher Name')
    publisher_slug     = models.SlugField(unique=True, null=True, verbose_name='Publisher Slug')
    publisher_status   = models.BooleanField(default=False, verbose_name='Active')
           
    class Meta:
        verbose_name = ('Publisher')
        verbose_name_plural = ('Publishers')
        ordering = ('id', 'publisher_name')

    def __str__(self):
        return self.publisher_name
        
    def save(self, *args, **kwargs):
        self.publisher_slug = slugify(self.publisher_name)
        super(Publisher, self).save(*args, **kwargs)

class Software(models.Model):
    software_name            = models.CharField(max_length=200, unique=True, verbose_name='Software Name')
    software_slug            = models.SlugField(unique=True, null=True)
    software_status          = models.BooleanField(default=False, verbose_name='Active')
    software_version         = models.CharField(max_length=200, verbose_name='Software Version', null=True)
    software_publisher       = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Software')
        verbose_name_plural = ('Software')
        ordering = ('id', 'software_name')
        unique_together = ('software_name', 'software_publisher')

    def __str__(self):
        return self.software_name


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Version, self).save(*args, **kwargs)

def pre_save_software(sender, instance, *args, **kwargs):
	slug = slugify(instance.software_publisher) + "-" + slugify(instance.software_name)
	instance.slug = slug

pre_save.connect(pre_save_software, sender=Software)


class Server(models.Model):
    server_name            = models.CharField(max_length=200, unique=True, verbose_name='Server Name')
    server_slug            = models.SlugField(unique=True, null=True)
    server_status          = models.BooleanField(default=False, verbose_name='Active')
    server_software        = models.ManyToManyField(Software, blank=True)


    class Meta:
        verbose_name = ('Server')
        verbose_name_plural = ('Servers')
        ordering = ('id', 'server_name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.server_slug = slugify(self.server_name)
        super(Server, self).save(*args, **kwargs)