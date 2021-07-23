from rest_framework import serializers
from . import models


class GeenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'geenre_title')
        model = models.Geenre

class TeatherSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'room')
        model = models.Teather

class FilmSerializer(serializers.ModelSerializer):
	geenre = GeenreSerializer(read_only=True)
	geenre_id = serializers.IntegerField(write_only=True)

	class Meta:
		fields = ('id','geenre_id','cover','title','sinopsis','geenre','status')
		model = models.Film
		

class ScheduleSerializer(serializers.ModelSerializer):
	film = FilmSerializer(read_only=True)
	film_id = serializers.IntegerField(write_only=True)
	teather = TeatherSerializer(read_only=True)
	teather_id = serializers.IntegerField(write_only=True)

	class Meta:
		fields = ('id','film_id','teather_id','time','durations','film','teather')
		model = models.Schedule
		