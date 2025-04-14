from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.models import SiteSettings, Question, Answer
from apps.serializers import SiteModelSerializer, QuestionModelSerializer, AnswerModelSerializer


@extend_schema(tags=['SiteSettings'])
class SiteListCreateAPIView(ListCreateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['SiteSettings'])
class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['SiteSettings'])
class AnswerListCreateAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer
    permission_classes = AllowAny,
