# import json
# from django.urls import reverse
# from rest_framework.test import APITestCase
#
# from apps.music.models import Artist
#
#
# class ArtistCreateTest(APITestCase):
#
#     def test_song_create(self):
#         url = reverse("artist-create")
#         data = {
#             "fullname": "Song Title",
#             "avatar": open("media/song.jpg", "rb"),
#
#         }
#         response = self.client.post(url, data)
#         artist = Artist.objects.create()
#         data = json.loads(response.content)
#         self.assertEqual(response.status_code, 201)
#         # self.assertEqual(data["fullname"], artist.fullname)
