from django.urls import path

from . import views

urlpatterns = [
	# geenre url
    path('geenre', views.GeenreList.as_view()),
    path('geenre/<int:pk>', views.GeenreDetail.as_view()),

    # film url
    path('film', views.FilmList.as_view()),
    path('film/<int:pk>', views.FilmDetail.as_view()),

    # shadule
    path('teather', views.TeatherList.as_view()),
    path('teather/<int:pk>', views.TeatherDetail.as_view()),

    # schedule
    path('schedule', views.ScheduleList.as_view()),
    path('schedule/<int:pk>', views.ScheduleDetail.as_view()),

]