from rest_framework.serializers import ModelSerializer
from .models import Person, Teams


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email', 'team_id')


class TeamsSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'name')
