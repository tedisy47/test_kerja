from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



from .models import Geenre, Film, Teather, Schedule
from .serializers import GeenreSerializer, FilmSerializer, TeatherSerializer, ScheduleSerializer

cache.set('greeting', 'Hello world', 30)

class GeenreList(generics.ListCreateAPIView):	
    # permission_classes = (IsAuthenticated,)
    if 'geenre' in cache:
    	queryset = cache.get('geenre')
    	serializer_class = GeenreSerializer
    	# print('ech');
    else:
    	queryset = Geenre.objects.all()
    	cache.set('geenre',queryset,timeout=CACHE_TTL)
    	serializer_class = GeenreSerializer


class GeenreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Geenre.objects.all()
    serializer_class = GeenreSerializer

class TeatherList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    if 'teather' in cache:
    	queryset = cache.get('teather')
    else:
    	queryset = Teather.objects.all()
    	cache.set('teather',queryset,timeout=CACHE_TTL)
    serializer_class = TeatherSerializer

class TeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Teather.objects.all()
    serializer_class = TeatherSerializer

class FilmList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = FilmSerializer
	def get_queryset(self):
		if 'film' in cache:
			queryset = cache.get('film')
		else:
			queryset = Film.objects.all()
			cache.set('film',queryset,timeout=CACHE_TTL)
		status = self.request.query_params.get('status', None)
		geenre = self.request.query_params.get('geenre', None)
		if status is not None:
			if 'film_status' in cache:
				print('test')
				queryset = cache.get('film_status');
			else:
				queryset = queryset.filter(status=status)
				cache.set('film_status',queryset,timeout=CACHE_TTL)
		if geenre is not None:
			if 'film_geenre' in cache:
				queryset = cache.get('film_geenre');
			else:
				
				queryset = queryset.filter(geenre_id=geenre)
				cache.set('film_geenre',queryset,timeout=CACHE_TTL)
		return queryset
	# print(queryset)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
	# permission_classes = (IsAuthenticated,)
	queryset = Film.objects.all()
	serializer_class = FilmSerializer

class ScheduleList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ScheduleSerializer
	def get_queryset(self):
		if 'schedule' in cache:
			queryset = cache.get('schedule')
		else:
			queryset = Schedule.objects.all()
			cache.set('schedule',queryset,timeout=CACHE_TTL)
		film = self.request.query_params.get('film', None)
		if film is not None:
			if 'schedule_film' in cache:
				queryset = cache.get('schedule_film')
			else:
				queryset = queryset.filter(film=film)
				cache.set('schedule_film'.queryset,timeout=CACHE_TTL)
		return queryset
	# print(queryset)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer