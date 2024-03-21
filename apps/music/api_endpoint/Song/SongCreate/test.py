# import json
# from django.urls import reverse
# from rest_framework.test import APITestCase
#
# from apps.music.models import Song
#
#
# class SongCreateTest(APITestCase):
#
#     def test_song_create(self):
#         url = reverse("song-create")
#         data = {
#             "title": "Song Title",
#             "cover": open("media/song.jpg", "rb"),
#             "file": "media",
#             "genres": 1,
#             # "album": 1,
#         }
#         response = self.client.post(url, data)
#         song = Song.objects.create()
#         data = json.loads(response.content)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Song.objects.count(), 1)
#         self.assertEqual(data["title"], song.title)
