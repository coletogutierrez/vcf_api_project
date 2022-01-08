from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import get_object_or_404

import vcfpy
# import json
# from django.http import JsonResponse

from . models import VcfFile
from . serializers import RecordsSerializer

from django.conf import settings
BASE_DIR = getattr(settings, "BASE_DIR", None)


class TokenAuthSupportQueryString(TokenAuthentication):
    """
    Extend the TokenAuthentication class to support querystring authentication
    in the form of "http://www.example.com/?auth_token=<token_key>"
    """
    def authenticate(self, request):
        # Check if 'token_auth' is in the request query params.
        # Give precedence to 'Authorization' header.
        if 'auth_token' in request.query_params and \
                        'HTTP_AUTHORIZATION' not in request.META:
            return self.authenticate_credentials(
                request.query_params.get('auth_token'))
        else:
            return super(
                TokenAuthSupportQueryString, self).authenticate(request)


class HomeView(APIView):
    def get(self, request):
        content = {'message': 'Home'}
        return Response(content)


class CustomAuthTokenView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthSupportQueryString,)
    # authentication_classes = (TokenAuthentication,)
    api_view = ['GET']

    def get(self, request):
        content = {'message': 'Token OK'}
        return Response(content)


def populate_content(content, record):
    # dictionary = {}
    # dictionary["CHROM"] = str(record.CHROM)
    # dictionary["POS"] = str(record.POS)
    # dictionary["REF"] = str(record.REF)
    # dictionary["ID"] = str(record.ID)
    # dictionary["ALT"] = str(record.ALT)
    #
    # # content.append(json.dumps(dictionary, indent = 4))
    # content.append(dictionary)

    res = Record(
        CHROM=str(record.CHROM),
        POS=str(record.POS),
        REF=str(record.REF),
        ID=str(record.ID),
        ALT=str(record.ALT))
    content.append(res)
    return content


class Record(object):
    def __init__(self, CHROM, POS, REF, ID, ALT):
        self.CHROM = CHROM
        self.POS = POS
        self.REF = REF
        self.ID = ID
        self.ALT = ALT


# class RecordsView(APIView, PageNumberPagination):
class RecordsView(APIView, LimitOffsetPagination):
    # renderer_classes = (BrowsableAPIRenderer, JSONRenderer, XMLRenderer,)
    renderer_classes = (JSONRenderer, XMLRenderer, BrowsableAPIRenderer,)

    def get(self, request, idfile=''):

        id = request.query_params.get('id', None)
        file = get_object_or_404(VcfFile, id=idfile)

        reader = vcfpy.Reader.from_path(
            str(BASE_DIR) + "/media/" + str(file.data_file))

        content = []
        # dictionary = {}

        for record in reader:
            if not record.is_snv():
                continue

            if id is not None:
                if id in record.ID:
                    content = populate_content(content, record)
            else:
                content = populate_content(content, record)

        # return Response(content)
        # return JsonResponse(content, safe=False)

        results = self.paginate_queryset(content, request, view=self)
        serializer = RecordsSerializer(results, many=True)
        # return Response(serializer.data)
        if len(content) == 0:
            return Response(
                {'detail': 'nothing here'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return self.get_paginated_response(serializer.data)
