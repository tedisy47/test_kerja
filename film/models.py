from django.db import models



class Geenre(models.Model):
    geenre_title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.geenre
class Film(models.Model):
	status_choice = [
	('Coming Soon', 'Coming Soon'),
	('Now', 'Now')
	]
	geenre = models.ForeignKey(Geenre, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	cover = models.FileField(blank=False, null=False)
	sinopsis = models.TextField()
	status = models.CharField(max_length=20, choices=status_choice)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
class Teather(models.Model):
    room = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    		
    def __str__(self):
        return self.room

class Schedule(models.Model):
    teather = models.ForeignKey(Teather,on_delete=models.CASCADE)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    durations = models.IntegerField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    