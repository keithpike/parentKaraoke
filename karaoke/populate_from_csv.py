import csv
import string

from karaoke.models import Song
from karaoke.models import Artist
from karaoke.models import KaraokeDisc

def get_model(my_model, kwargs):
		result = None
		try:
			 result = my_model.objects.filter(**kwargs)
		except Exception, e:
			pass
		return result

def add_to_db(my_model, kwargs):
	return my_model.objects.create(**kwargs)

def populate_artists(item, existing_items):
	artist = string.capwords(item[1])
	flag = True
	try:
		result = existing_items[artist]
		flag = False
	except Exception, e:
		pass
	if flag:
		result_set = get_model(Artist, {"name": artist})
		my_artist = result_set.first()
		if my_artist:
			artist = my_artist.name
			existing_items[artist] = my_artist
			result = existing_items[artist]
		else:
			result = add_to_db(Artist, {"name": artist})
	return result

def populate_discs(item, existing_items):
	name = item[2]
	disc_number = item[3]
	disc_name = name
	flag = True
	try:
		result = existing_items[item]
		flag = False
	except Exception, e:
		pass
	
	if flag:
		result_set = get_model(KaraokeDisc, {"name": disc_name, "disc_number": disc_number})
		disc = result_set.first()
		if disc:
			disc_name = disc.name
			existing_items[disc_name] = disc
			result = existing_items[disc_name]
		else:
			result = add_to_db(KaraokeDisc, {"name": disc_name, "disc_number": disc_number})
		return result
def populate_songs(item, artist_id, disc_id):
	name = string.capwords(item[0])
	add_to_db(Song, {"name": name, "artist_id": artist_id, "disc_id": disc_id})



def populate_db():
	artists = {}
	discs = {}

	with open('./karaoke/import.csv', 'rb') as file:
		reader = csv.reader(file, delimiter=";", quotechar='"')
		my_list = list(reader)

	for item in my_list:
		artist = populate_artists(item, artists)
		artist_id = artist.id
		disc = populate_discs(item, discs)
		disc_id = disc.id
		populate_songs(item, artist_id, disc_id)