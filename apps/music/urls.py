from django.urls import path

from apps.music.api_endpoint.Album import (
    AlbumCreateView,
    AlbumListView,
    AlbumRetrieveUpdateDestroyView,
)
from apps.music.api_endpoint.Artist import (
    ArtistListView,
    ArtistCreateView,
    ArtistRetrieveUpdateDestroyView,
)
from apps.music.api_endpoint.Genres import GenresCreateView, GenresListView, GenresRetrieveUpdateDestroyView
from apps.music.api_endpoint.Song import (
    SongCreateView,
    SongListView,
    SongRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("song/create", SongCreateView.as_view(), name="song-create"),
    path("song/", SongListView.as_view()),
    path("song/<pk>/", SongRetrieveUpdateDestroyView.as_view()),
    path("artist/", ArtistListView.as_view()),
    path("artist/create", ArtistCreateView.as_view(), name="artist-create"),
    path("artist/<pk>", ArtistRetrieveUpdateDestroyView.as_view()),
    path("album/create", AlbumCreateView.as_view()),
    path("album/", AlbumListView.as_view()),
    path("album/<pk>/", AlbumRetrieveUpdateDestroyView.as_view()),
    path("genres/create", GenresCreateView.as_view()),
    path("genres/", GenresListView.as_view()),
    path("genres/<pk>/", GenresRetrieveUpdateDestroyView.as_view()),
]
