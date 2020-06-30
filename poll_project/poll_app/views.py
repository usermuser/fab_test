from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Poll, Question
from .serializers import PollSerializer


class PollsViewset(viewsets.ViewSet):
    """
    TODO don't forget to add docstring
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """ Get all Polls"""
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ Get One Poll """
        queryset = Poll.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(user)
        return Response(serializer.data)


class