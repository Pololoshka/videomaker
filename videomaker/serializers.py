from rest_framework import serializers

from videomaker.models import Phrase


class PhraseSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=50)

    class Meta:
        model = Phrase
        fields = ("text",)
