# -*- coding: utf-8 -*-

from rest_framework import serializers


class RecordsSerializer(serializers.Serializer):

    CHROM = serializers.CharField(max_length=200)
    POS = serializers.CharField(max_length=200)
    REF = serializers.CharField(max_length=200)
    ID = serializers.CharField(max_length=200)
    ALT = serializers.CharField(max_length=200)
