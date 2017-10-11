from django.test import TestCase

from solos.models import Solo
from albums.models import Album, Track


class SoloModelTestCase(TestCase):
    def setUp(self):
        self.album = Album.objects.create(
            name='At the Stratford Shakespearean Festival',
            artist='Oscar Peterson Trio',
            slug='at-the-stratford-shakespearean-festival',
        )

        self.track = Track.objects.create(
            name='Falling in Love with Love',
            album=self.album,
            track_number=1,
            slug='falling-in-love-with-love',
        )

        self.solo = Solo.objects.create(
            track='Falling in Love with Love',
            artist='Oscar Peterson',
            instrument='piano',
            album='At the Stratford Shakespearean Festival',
            start_time='1:24',
            end_time='4:06'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
        self.assertEqual(self.solo.end_time, '4:06')

    def test_get_absolute_url(self):
        """
        Test that we can build a URL fora solo
        """
        self.assertEqual(
            self.solo.get_absolute_url(),
            '/recordings/at-the-stratford-shakespearean-festival/falling-in-love-with-love/oscar-peterson/'
        )
