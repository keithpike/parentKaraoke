from django.contrib import admin
from karaoke.models import Song
from karaoke.models import KaraokeDisc
from karaoke.models import Artist
from karaoke.models import Tag
# Register your models here.

class ArtistInline(admin.StackedInline):
	model = Artist
	extra = 0

class SongAdmin(admin.ModelAdmin):
	list_display = ("name", "get_artist", "get_disc", "get_disc_number", "track")
	list_filter = ["artist_id", "tag"]
	search_fields = ["name"]
	filter_horizontal = ('tag',)
	# inlines = [ArtistInline]

class TagAdmin(admin.ModelAdmin):
	list_display = ["name"]

class ArtistAdmin(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["name"]

class KaraokeDiscAdmin(admin.ModelAdmin):
	# fields = {None: []}
	list_display = ["name", "disc_number", "get_songs"]
	search_fields = ["name"]


admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(KaraokeDisc, KaraokeDiscAdmin)
admin.site.register(Tag, TagAdmin)