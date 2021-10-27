from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Ait(models.Model):
    """
    Ait can have many Sub Projects
    Ait can support Many Devices
    ait_number must be a number
    """
    ait_number          = models.IntegerField(unique=True, verbose_name='Ait #')
    ait_slug            = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = ('AIT')
        verbose_name_plural = ('AITs')
        ordering = ('id', 'ait_number')

    def __str__(self):
        return str(self.ait_number)

    def save(self, *args, **kwargs):
        self.ait_slug = slugify(self.ait_number)
        super(Ait, self).save(*args, **kwargs)


class Project(models.Model):
    """
    Project can have many Devices
    project can have multiple AIT's
    project_ait is a foreign key
    """
    project_name            = models.CharField(max_length=200, verbose_name='Project Name')
    project_slug            = models.SlugField(unique=True, null=True)
    project_status          = models.BooleanField(default=False, verbose_name='Active')

    # Foreign Relationships
    project_ait             = models.ForeignKey(Ait, verbose_name='Project AIT #', blank=True, null=True, on_delete=models.CASCADE)
    # project_environment     = models.ForeignKey(Project, verbose_name='Project Environment', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Project')
        verbose_name_plural = ('Projects')
        ordering = ('id', 'project_name')
        unique_together = ('project_name', 'project_ait')


    def __str__(self):
        # return (f'{self.project_name}-{self.project_ait}')
        # return (self.project_name + str(self.project_ait))
        return self.project_name

    def save(self, *args, **kwargs):
        self.project_slug = slugify(self.project_name + '-' + slugify(self.project_ait))
        # self.project_slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)


class Environment(models.Model):
    """
    Environment must have a project
    save() method unique slug
    Multiple devices can be tied to single environment
    """
    environment_name            = models.CharField(max_length=200, verbose_name='Environment Name')
    environment_slug            = models.SlugField(unique=True, null=True)
    environment_status          = models.BooleanField(default=False, verbose_name='Active')
    # environment_software        = models.ManyToManyField(Software, blank=True)
    # environment_project         = models.ForeignKey(Project, verbose_name='Environment Project', on_delete=models.CASCADE)
    environment_project         = models.ForeignKey(Project, verbose_name=' environment_project - Project Environment', on_delete=models.CASCADE)


    class Meta:
        verbose_name = ('Environment')
        verbose_name_plural = ('Environments')
        ordering = ('id', 'environment_name')
        unique_together = ('environment_name', 'environment_project')

    def __str__(self):
        return self.environment_name

    # def save(self, *args, **kwargs):
    #     self.environment_slug = slugify(self.environment_name)
    #     super(Environment, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.environment_slug = slugify(self.environment_name + '-' + slugify(self.environment_project))
        super(Environment, self).save(*args, **kwargs)



# class Team(models.Model):
#     team_name            = models.CharField(max_length=200, unique=True, verbose_name='Team Name')
#     team_slug            = models.SlugField(unique=True, null=True)
#     team_status          = models.BooleanField(default=False, verbose_name='Active')
#     # team_software        = models.ManyToManyField(Software, blank=True)


#     class Meta:
#         verbose_name = ('Team')
#         verbose_name_plural = ('Teams')
#         ordering = ('id', 'team_name')

#     def __str__(self):
#         return self.team_name

#     def save(self, *args, **kwargs):
#         self.team_slug = slugify(self.team_name)
#         super(Team, self).save(*args, **kwargs)

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
    software_name            = models.CharField(max_length=200, verbose_name='Software Name')
    software_slug            = models.SlugField(unique=True, null=True)
    software_status          = models.BooleanField(default=False, verbose_name='Active')
    software_version         = models.CharField(max_length=200, verbose_name='Software Version', null=True)
    software_publisher       = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Software')
        verbose_name_plural = ('Software')
        ordering = ('id', 'software_name')
        unique_together = ('software_name', 'software_version')

    def __str__(self):
        return self.software_name


    def save(self, *args, **kwargs):
        self.software_slug = slugify(self.software_name + "-" + slugify(self.software_version))
        super(Software, self).save(*args, **kwargs)

# def pre_save_software(sender, instance, *args, **kwargs):
# 	slug = slugify(instance.software_publisher) + "-" + slugify(instance.software_name)
# 	instance.software_slug = slug

# pre_save.connect(pre_save_software, sender=Software)


class Device(models.Model):
    """
    Device can have many software associated
    Device can be created without software
    Device can be part of multiple AIT's
    Device can only be a part of a single project
    Device can only be part of a single environment
    """
    
    device_name            = models.CharField(max_length=200, unique=True, verbose_name='Device Name')
    device_slug            = models.SlugField(unique=True, null=True)
    device_status          = models.BooleanField(default=False, verbose_name='Active')

    # ManyToMany
    device_software        = models.ManyToManyField(Software, blank=True, verbose_name='Device Software')

    # Foreign Relationships
    device_ait             = models.ForeignKey(Ait, verbose_name='Device AIT', blank=True, null=True, on_delete=models.CASCADE)
    device_project         = models.ForeignKey(Project, verbose_name='Device Project', blank=True, null=True, on_delete=models.CASCADE)
    device_environment     = models.ForeignKey(Environment, verbose_name='Device Environment', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Device')
        verbose_name_plural = ('Devices')
        ordering = ('id', 'device_name')

    def __str__(self):
        return self.device_name

    def save(self, *args, **kwargs):
        self.device_slug = slugify(self.device_name)
        super(Device, self).save(*args, **kwargs)

