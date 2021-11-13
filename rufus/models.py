from django.db import models
# from django_mysql.models import JSONField
from django.utils.safestring import mark_safe
import json
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer

# Create your models here.
class ContactInfo(models.Model):

    data = models.JSONField()

    class Meta:
        verbose_name = ('Contact Info')
        verbose_name_plural = ('Contacts Info')
        # ordering = ('id', 'ait_number')

    def __str__(self):
        return str(self.data)




class BookExample(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    detail_text = models.TextField()
    detail_json = models.JSONField()  # requires Django-Mysql package

    def detail_json_formatted(self):

        # dump the json with indentation set

        # example for detail_text TextField
        # json_obj = json.loads(self.detail_text)
        # data = json.dumps(json_obj, indent=2)

        # with JSON field, no need to do .loads
        data = json.dumps(self.detail_json, indent=2)

        # format it with pygments and highlight it
        formatter = HtmlFormatter(style='xcode')
        response = highlight(data, JsonLexer(), formatter)

         # include the style sheet
        style = "<style>" + formatter.get_style_defs() + "</style><br/>"

        return mark_safe(style + response)

    detail_json_formatted.short_description = 'Details Formatted'

    class Meta:
        managed = True
        db_table = 'book_example'
        verbose_name = 'Book Example'
        verbose_name_plural = 'Book Examples'