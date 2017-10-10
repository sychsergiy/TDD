from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from solos.views import index, SoloDetailView
from solos.models import Solo


class SoloBaseTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.drum_solo = Solo.objects.create(
            instrument='drums',
            artist='Rich',
            track='Bugle Call Rag'
        )
        cls.sax_solo = Solo.objects.create(
            instrument='saxophone',
            artist='Coltrane',
            track='Mr. PC'
        )


class IndexViewTestCase(SoloBaseTestCase):
    def test_basic(self):
        """
        Test that the solo view returns a 200 response, uses
        the correct template, and has the correct context
        """
        request = self.factory.get('/solos/1/')

        response = SoloDetailView.as_view()(
            request,
            self.drum_solo.pk
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data['solo'].artist,
            'Rich'
        )
        with self.assertTemplateUsed('solo/solo_detail.html'):
            response.render()

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
