from django.test import LiveServerTestCase

from selenium import webdriver

from solos.models import Solo
from albums.models import Album, Track


class StudentTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)
        self.album1 = Album.objects.create(
            name='My Favorite Things', slug='my-favorite-things')
        self.track1 = Track.objects.create(
            name='My Favorite Things', slug='my-favorite-things',
            album=self.album1)
        self.solo1 = Solo.objects.create(
            instrument='saxophone', artist='John Coltrane',
            track=self.track1, slug='john-coltrane')
        self.album2 = Album.objects.create(
            name='Kind of Blue', slug='kind-of-blue')
        self.track2 = Track.objects.create(
            name='All Blues', slug='all-blues',
            album=self.album2, track_number=4)
        self.solo2 = Solo.objects.create(
            instrument='saxophone', artist='Cannonball Adderley',
            track=self.track2, start_time='4:05', end_time='6:04',
            slug='cannonball-adderley')
        self.album3 = Album.objects.create(
            name='Know What I Mean?', slug='know-what-i-mean')
        self.track3 = Track.objects.create(
            name='Waltz for Debby', slug='waltz-for-debby',
            album=self.album3)
        self.solo3 = Solo.objects.create(
            instrument='saxophone', artist='Cannonball Adderley',
            track=self.track3, slug='cannonball-adderley')
        self.track4 = Track.objects.create(name='Freddie Freeloader',
                                           album=self.album2)
        self.track5 = Track.objects.create(name='Blue in Green',
                                           album=self.album2)

    def tearDown(self):
        self.browser.quit()

    # def test_student_find_solos(self):
    #     """
    #     Test test a user can search for solos
    #     """
    #     # Steve is a jazz student who would like to find more
    #     # examples of solos so he can improve his own
    #     # improvisation. He visits the home page of JMAD.
    #     home_page = self.browser.get(self.live_server_url + '/')
    #
    #     # He knows he's in the right place because he can see
    #     # the name of the site in the heading.
    #     brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
    #     self.assertEqual('JMAD', brand_element.text)
    #
    #     # He sees the inputs of the search form, including labels and
    #     # placeholders.
    #     instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument')
    #     self.assertIsNotNone(self.browser.find_element_by_css_selector(
    #         'label[for="jmad-instrument"]'))
    #     self.assertEqual(instrument_input.get_attribute('placeholder'),
    #                      'i.e. trumpet')
    #     artist_input = self.browser.find_element_by_css_selector(
    #         'input#jmad-artist')
    #     self.assertIsNotNone(self.browser.find_element_by_css_selector(
    #         'label[for="jmad-artist"]'))
    #     self.assertEqual(artist_input.get_attribute('placeholder'),
    #                      'i.e. Davis')
    #
    #     # He types in the name of his instrument and submits it.
    #     instrument_input.send_keys('saxophone')
    #     artist_input.send_keys('Cannonball Adderley')
    #     self.browser.find_element_by_css_selector('form button').click()
    #
    #     # He sees too many search results...
    #     search_results = self.find_search_results()
    #
    #     # ...so he adds an artist to his search query and
    #     # gets a more manageable list.
    #
    #     # He clicks on a search result.
    #     self.assertEqual(len(search_results), 2)
    #     second_search_result = self.find_search_results()
    #     second_search_result[0].click()
    #
    #     # The solo page has the title, artist and album for
    #     # this particular solo.
    #     self.assertEqual(
    #         self.browser.current_url,
    #         self.live_server_url + '/recordings/kind-of-blue/all-blues/cannonball-adderley/'
    #     )
    #     # he sees the artist
    #     self.assertEqual(
    #         self.browser.find_element_by_css_selector(
    #             '#jmad-artist').text,
    #         'Cannonball Adderley'
    #     )
    #
    #     # and the album title(with track count) for this solo.
    #     self.assertEqual(
    #         self.browser.find_element_by_css_selector(
    #             '#jmad-album').text,
    #         'Kind of Blue [3 tracks]'
    #     )
    #
    #     self.assertEqual(
    #         self.browser.find_element_by_css_selector(
    #             '#jmad-track').text,
    #         'All Blues [1 solo]',
    #     )
    #     # He also sees the start time and end time of the solo.
    #     self.assertEqual(
    #         self.browser.find_element_by_css_selector(
    #             '#jmad-start-time').text,
    #         '4:05'
    #     )
    #     self.assertEqual(
    #         self.browser.find_element_by_css_selector(
    #             '#jmad-end-time').text,
    #         '6:04'
    #     )

    def find_search_results(self):
        return self.browser.find_elements_by_css_selector(
            '.jmad-search-result a'
        )

    def test_staff_can_add_content(self):
        """
        Tests that a 'staff' user can access the admin
        add Albums, Tracks, and Solos
        """
        # Bill would like to add a record and a number of
        # solos to JMAD. He visits the admin site
        admin_root = self.browser.get(
            self.live_server_url + '/admin/')

        # He can tell he's in the right place because of the
        # title of the page
        self.assertEqual(self.browser.title,
                         'Log in | Django site admin')
        self.fail('Incomplete Test')

        # He enters his username and password and submits the
        # form to log in

        # He sees links to Albums, Tracks and Solos

        # He clicks on Albums and sees all of the Albums that
        # have been added so far

        # Going back to the home page, he clicks the Tracks
        # link and sees the Tracks that have been added.
        # They're ordered first by Album, then by track
        # number.

        # Heads a track to an album that already exists

        # He adds another track, this time on an album that
        # is not in JMAD yet

        # After adding the basic Track info, he clicks on the
        # plus sign to add a new album.

        # THe focus shifts to the newly opened window, where
        # he sees an Album form

        # After creating the Album, he goes back to finish
        # the Track

        # He goes back to the root of the admin site and
        # clicks on 'Solos'

        # He sees Solos listed by Album, then Track, then
        # start time

        # He adds a Solo to a Track that already exists

        # He then adds a Solo for which the Track and Album
        # do not yet exist

        # He adds a Track from the Solo page

        # He adds an Album from the Track popup

        # He finishes up both parent objects, and saves the
        # Solo


