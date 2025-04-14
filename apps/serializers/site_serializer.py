from rest_framework.serializers import ModelSerializer

from apps.models import Question, Answer, SiteSettings


class SiteModelSerializer(ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = 'region_to_region',


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = 'text', 'created_at',

    extra_kwargs = {
        'created_at': {'read_only': True},
    }


class AnswerModelSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = 'text', 'question', 'created_at',

    extra_kwargs = {
        'created_at': {'read_only': True},
    }
