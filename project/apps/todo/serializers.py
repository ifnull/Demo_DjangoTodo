from tastypie.serializers import Serializer


class MyDatetimeSerializer(Serializer):
    def format_datetime(self, data):
        return data.strftime("%s")
