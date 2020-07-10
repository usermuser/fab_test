from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class PollsView(APIView):
    """
    TODO don't forget to add docstring
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Http404

    def get(self, request):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response({"polls":serializer.data})

    def post(self, request):
        poll = request.data.get("poll")
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response(
            {"success": f"Poll '{poll_saved.name}' created succesfully"}
        )

    def put(self, request, pk):
        saved_poll = get_object_or_404(Poll.objects.all(), pk=pk)
        data = request.data.get('poll')
        serializer = PollSerializer(instance=saved_poll, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()

        return Response(
            {"success": f"Poll '{poll_saved}' updated successfully"}
        )

    def delete(self, request, pk):
        poll = get_object_or_404(Poll.objects.all(), pk=pk)
        poll.delete()
        return Response(
            {"message": f"Poll with id {pk} has been deleted"}, status=204
        )


class QuestionsView(APIView):
    """
    TODO don't forget to add docstring
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        queryset = Question.objects.filter(poll__pk=pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
