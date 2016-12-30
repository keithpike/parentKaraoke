from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.TextField()
	rating = models.IntegerField(blank = True, null=True)
	artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
	disc = models.ForeignKey("KaraokeDisc", on_delete=models.PROTECT)
	track = models.IntegerField(blank = True, null=True)
	tag = models.ManyToManyField("Tag", blank = True)
	def __str__(self):
		return self.name

	def get_disc_number(self):
		return self.disc.disc_number

	def get_artist(self):
		return self.artist.name

	def get_disc(self):
		return self.disc.name

class Tag(models.Model):
	name = models.TextField()
	class Meta:
		ordering = ("name",)
	def __str__(self):
		return self.name

class Artist(models.Model):
	name = models.TextField()

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class KaraokeDisc(models.Model):
	name = models.TextField()
	disc_number = models.IntegerField()

	class Meta:
		ordering = ('name',)
	def __str__(self):
		return self.name + " disc #" + str(self.disc_number)

	def get_songs(self):
		print self.song_set
		return list(self.song_set.all())