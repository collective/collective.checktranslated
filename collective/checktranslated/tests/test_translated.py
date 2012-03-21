# -*- coding: UTF-8 -*-
import unittest2 as unittest

from collective.checktranslated.symptoms import check_translated
from collective.checktranslated.testing import CHECKTRANSLATED_INTEGRATION
from collective.checktranslated.testing import CHECKTRANSLATED_FUNCTIONAL
from Products.LinguaPlone.public import BaseContent
from Products.LinguaPlone.public import registerType
from Products.Archetypes.Schema.factory import instanceSchemaFactory
from Products.LinguaPlone.utils import LocateTranslation

from zope.component import testing
from zope.component import provideAdapter

from plone.app.testing import TEST_USER_NAME, TEST_USER_ID
from plone.app.testing import setRoles

class TestTranslated(unittest.TestCase):
    site_languages = ['fr', 'en', 'nl']
    '''
    def setUp(self):
        testing.setUp(self)
        provideAdapter(instanceSchemaFactory)
        # or provideAdapter(instanceSchemaFactory, [IBaseOjbect], ISchema)
        provideAdapter(LocateTranslation)
        #provideAdapter(LocateTranslation, [ILocateTranslation], ITranslatable)
    
    def tearDown(self):
        testing.tearDown(self)
    '''
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
        site.invokeFactory(type_name="Folder", id="object_current_test", language="fr")
        fr_object = site.object_current_test
        
        status, description  = check_translated(fr_object, self.site_languages, 'fr')
        self.assertTrue(status)
    '''
    def test_translated(self):
        site = self.layer['portal']
        setRoles(site, TEST_USER_ID, ('Manager',))
        site.invokeFactory(type_name="Folder", id="object_translated_test", language="fr")
        fr_object = site.object_translated_test
        

        site.invokeFactory(type_name="Folder", id="nl_object", language="nl")
        nl_object = site.nl_object
        fr_object.addTranslation(nl_object)
        status, description  = check_translated(fr_object, self.site_languages, 'nl')
        self.assertTrue(status)
        
        #status, description  = check_translated(nl_object, self.site_languages, 'fr')
        #self.assertTrue(status)
    '''
