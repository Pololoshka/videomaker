import tempfile

from django.http import FileResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from videomaker.handlers import Constant, create_video
from videomaker.models import Phrase
from videomaker.serializers import PhraseSerializer


class VideoAPIView(APIView):
    def get(self, request: Request) -> FileResponse:
        serializer = PhraseSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        phrase = Phrase.objects.get_or_create(text=serializer.validated_data["text"])[0]

        with tempfile.TemporaryDirectory() as tmpdirname:
            path_to_file = create_video(
                video_name="my_video",
                text=phrase.text,
                const=Constant(),
                dir_name=tmpdirname,
            )

            return FileResponse(path_to_file.open(mode="rb"), as_attachment=True)
