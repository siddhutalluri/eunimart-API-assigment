from rest_framework import serializers
from .models import Userdata,Tweet


class UserdataSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userdata
        fields = "__all__"


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = Tweet
        fields = "__all__"