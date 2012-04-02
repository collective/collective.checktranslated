# -*- coding: UTF-8 -*-
import unittest2 as unittest

from collective.checktranslated.symptoms import check_translated
from collective.checktranslated.testing import CHECKTRANSLATED_INTEGRATION

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class TestTranslated(unittest.TestCase):
    site_languages = ['fr', 'en', 'nl']
    layer = CHECKTRANSLATED_INTEGRATION

    def test_translated_in_nl(self):
        site = self.layer['portal']
        setRoles(site, TEST_USER_ID, ('Manager',))
        site.invokeFactory(type_name="Folder", id="fr_object", language="fr")
        fr_object = site.fr_object
        status, description  = check_translated(fr_object, self.site_languages, 'nl')
        self.assertFalse(status)

    def test_neutral(self):
        site = self.layer['portal']
        setRoles(site, TEST_USER_ID, ('Manager',))
        site.invokeFactory(type_name="Folder", id="neutral_object", language="")
        neutral_object = site.neutral_object
        status, description  = check_translated(neutral_object, self.site_languages, 'nl')
        self.assertFalse(status)
    
    def test_current_language(self):
        site = self.layer['portal']
        setRoles(site, TEST_USER_ID, ('Manager',))
        site.invokeFactory(type_name="Folder", id="object_current_test", language="en")
        fr_object = site.object_current_test

        status, description  = check_translated(fr_object, self.site_languages, 'en')
        self.assertTrue(status)

    def test_translated(self):
        site = self.layer['portal']
        setRoles(site, TEST_USER_ID, ('Manager',))
        site.invokeFactory(type_name="Document", id="fr", language="fr")
        fr = site.fr

        site.invokeFactory(type_name="Document", id="nl", language="nl")
        nl = site.nl
        fr.addTranslationReference(nl)

        self.site_languages = ['fr', 'nl']
        status  = check_translated(fr, self.site_languages, 'nl')
        self.assertTrue(status)

        self.site_languages = ['fr', 'nl']
        status, description  = check_translated(nl, self.site_languages, 'fr')
        self.assertTrue(status)
