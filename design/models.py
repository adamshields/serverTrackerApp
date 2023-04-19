from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Approval(models.Model):
    is_fully_approved     = models.BooleanField(default=False, verbose_name='Fully Approved')
    level_1_approval      = models.CharField(max_length=200, unique=False, verbose_name='Level 1 Approver User Name')
    level_2_approval      = models.CharField(max_length=200, unique=False, verbose_name='Level 2 Approver User Name')
    level_3_approval      = models.CharField(max_length=200, unique=False, verbose_name='Level 3 Approver User Name')
           
    class Meta:
        verbose_name = ('Approval')
        verbose_name_plural = ('Approvals')


class Design(models.Model):
    design_name         = models.CharField(max_length=200, unique=True, verbose_name='Design Name')
    design_slug         = models.SlugField(unique=True, null=True, verbose_name='Design Slug')
    is_editable         = models.BooleanField(default=False, verbose_name='Editable')
    design_approval     = models.ForeignKey(Approval, verbose_name='Design Approval', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Design')
        verbose_name_plural = ('Designs')
        ordering = ('id', 'design_name')

    def __str__(self):
        return self.design_name
        
    def save(self, *args, **kwargs):
        self.design_slug = slugify(self.design_name)
        super(Design, self).save(*args, **kwargs)