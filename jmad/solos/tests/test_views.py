from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from solos.views import index, solo_detail
from solos.models import Solo
from albums.models import Album, Track


class SoloBaseTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.no_funny_hats = Album.objects.create(
            name='No Funny Hats', slug='no-funny-hats')
        cls.bugle_call_rag = Track.objects.create(
            name='Bugle Call Rag', slug='bugle-call-rag',
            album=cls.no_funny_hats)
        cls.drum_solo = Solo.objects.create(
            instrument='drums', artist='Buddy Rich',
            track=cls.bugle_call_rag, slug='rich')
        cls.giant_steps = Album.objects.create(
            name='Giant Steps', slug='giant-steps')
        cls.mr_pc = Track.objects.create(
            name='Mr. PC', slug='mr-pc', album=cls.giant_steps)
        cls.sax_solo = Solo.objects.create(
            instrument='saxophone', artist='Coltrane',
            track=cls.mr_pc, slug='coltrane')


class IndexViewTestCase(SoloBaseTestCase):
    def test_basic(self):
        """
        Test that the solo view returns a 200 response, uses
        the correct template, and has the correct context
        """
        request = self.factory.get('/solos/no-funny-hats/bugle-call-rag/buddy-rich/')

        response = solo_detail(
            request,
            album=self.no_funny_hats.slug,
            track=self.bugle_call_rag.slug,
            artist=self.drum_solo.slug
        )

        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed('solos/solo_detail.html'):
            response = solo_detail(request,
                                   album=self.no_funny_hats.slug,
                                   track=self.bugle_call_rag.slug,
                                   artist=self.drum_solo.slug)
        self.assertEqual(response.status_code, 200)
        page = response.content.decode()
        self.assertInHTML('<p id="jmad-artist">Buddy Rich</p>', page)

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses
        correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_index_view_return_solos(self):
        """
        Test that the index view will attempt to return
        Solos if query parameters exist
        """
        response = self.client.get(
            '/',
            {'instrument': 'drums'}
        )
        self.assertIs(
            type(response.context['solos']),
            QuerySet
        )
