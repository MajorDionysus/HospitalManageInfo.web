from rest_framework import serializers
from .models import ListItem, Hyperlink


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = '__all__'


class HyperlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hyperlink
        fields = '__all__'
