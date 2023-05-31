from django.contrib import admin
from .models import Song, Playlist


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'duration')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('songs',)
