from rest_framework import viewsets
from .models import Teams, Person
from .serializers import TeamsSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
