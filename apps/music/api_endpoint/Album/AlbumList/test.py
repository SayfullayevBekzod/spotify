# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# import json
# from apps.music.models import Album, Artist
#
# class AlbumCreateTest(APITestCase):
#
#     def test_album_create(self):
#         url = reverse("album-create")
#         data = {
#             "title": "Album Title",
#             "author": "6bf66d4a-6a8d-4b9d-807e-9856b415a708"
#         }
#         response = self.client.post(url, data)
#         # self.assertEqual(response.status_code, 201)
#         # self.assertEqual(Album.objects.count(), 1)
#         return response
#
#
# class AlbumListTest(APITestCase):
#
#     def test_album_list(self):
#         url = reverse('album-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         albums = Album.objects.all()
#         self.assertEqual(len(response.data), albums.count())
#         for i, album in enumerate(albums):
#             self.assertEqual(response.data[i]['title'], album.title)
#             self.assertEqual(response.data[i]['author'], str(album.author))


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Album, Artist


class AlbumRetrieveUpdateDestroyViewTest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(id="6bf66d4a-6a8d-4b9d-807e-9856b415a708")
        self.album = Album.objects.create(title="Test Album", author=self.artist)

    def test_album_retrieve(self):
        url = reverse("album-detail", kwargs={"pk": self.album.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.album.title)
        # Ensure response.data["author"] is the artist's ID or other unique identifier
        self.assertEqual(response.data["author"], str(self.artist.id))

    def test_album_update(self):
        url = reverse("album-detail", kwargs={"pk": self.album.pk})
        update_data = {"title": "Update Title"}
        response = self.client.put(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.album.refresh_from_db()
        self.assertEqual(self.album.title, update_data["title"])

    def test_album_delete(self):
        url = reverse("album-detail", kwargs={"pk": self.album.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Album.objects.filter(pk=self.album.pk).exists())
