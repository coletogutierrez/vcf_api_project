from __future__ import unicode_literals

from django.db import models

# from django.db.models import signals
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.db import connection

# from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# from datetime import datetime
# from django.utils import timezone

# from decimal import Decimal, ROUND_HALF_UP

# from openpyxl import load_workbook
# import unidecode
# import unicodedata
# import os.path
# import pandas as pd
# import xlrd

# from dateutil import parser


class VcfFile(models.Model):
    '''
    VCF File
    '''

    name = models.CharField('Name', max_length=255, blank=False,
                            help_text='Short description of the file')
    recap = models.TextField(blank=True, verbose_name='Recap')

    created_at = models.DateTimeField(auto_now_add=True, blank=True,
                                      verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, blank=True,
                                      verbose_name='Updated')

    is_active = models.BooleanField(default=False, verbose_name="Active")

    data_file = models.FileField(
        "Archivo",
        max_length=255,
        upload_to='reports/files/%Y/%m/%d/',
        # content_types=['application/pdf', 'application/zip'],
        # content_types=['image/jpeg', ],
        # max_upload_size=1048576,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['vcf'])]
      )

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = "VCF File"
        verbose_name_plural = "VCF Files"

    def __str__(self):
        return u'%s' % self.name
