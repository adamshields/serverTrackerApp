from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Ait(models.Model):
    """
    Ait can have many Sub Projects
    Ait can support Many Servers
    ait_number must be a number
    """
    ait_number          = models.IntegerField(unique=True, verbose_name='Ait #')
    ait_slug            = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = ('AIT')
        verbose_name_plural = ('AITs')
        ordering = ('id', 'ait_number')

    def __str__(self):
        return self.ait_number

    def save(self, *args, **kwargs):
        self.ait_slug = slugify(self.ait_number)
        super(Ait, self).save(*args, **kwargs)


class Project(models.Model):
    """
    Project can have many Servers
    project can have multiple AIT's
    project_ait is a foreign key
    """
    project_name            = models.CharField(max_length=200, unique=True, verbose_name='Project Name')
    project_slug            = models.SlugField(unique=True, null=True)
    project_status          = models.BooleanField(default=False, verbose_name='Active')

    # Foreign Relationships
    project_ait             = models.ForeignKey(Ait, verbose_name='Project AIT #', blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ('Project')
        verbose_name_plural = ('Projects')
        ordering = ('id', 'project_name')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        self.project_slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)


class Environment(models.Model):
    """
    Environment must have a project
    save() method unique slug
    Multiple servers can be ties to single environment
    """
    environment_name            = models.CharField(max_length=200, unique=True, verbose_name='Environment Name')
    environment_slug            = models.SlugField(unique=True, null=True)
    environment_status          = models.BooleanField(default=False, verbose_name='Active')
    # environment_software        = models.ManyToManyField(Software, blank=True)
    # environment_project         = models.ForeignKey(Project, verbose_name='Environment Project', on_delete=models.CASCADE)
    environment_project         = models.ForeignKey(Project, verbose_name='Environment Project', on_delete=models.CASCADE)


    class Meta:
        verbose_name = ('Environment')
        verbose_name_plural = ('Environments')
        ordering = ('id', 'environment_name')

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


class Server(models.Model):
    """
    Server can have many software associated
    Server can be created without software
    Server can be part of multiple AIT's
    Server can only be a part of a single project
    Server can only be part of a single environment
    """
    
    server_name            = models.CharField(max_length=200, unique=True, verbose_name='Server Name')
    server_slug            = models.SlugField(unique=True, null=True)
    server_status          = models.BooleanField(default=False, verbose_name='Active')

    server_software        = models.ManyToManyField(Software, blank=True)

    # Foreign Relationships
    server_project         = models.ForeignKey(Project, verbose_name='Server Project', blank=True, null=True, on_delete=models.CASCADE)
    server_environment     = models.ForeignKey(Environment, verbose_name='Server Environment', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Server')
        verbose_name_plural = ('Servers')
        ordering = ('id', 'server_name')

    def __str__(self):
        return self.server_name

    def save(self, *args, **kwargs):
        self.server_slug = slugify(self.server_name)
        super(Server, self).save(*args, **kwargs)

