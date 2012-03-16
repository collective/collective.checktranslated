# -*- coding: UTF-8 -*-
import unittest2 as unittest

from collective.checktranslated.symptoms import check_translated
from collective.checktranslated.testing import CHECKTRANSLATED

from Products.LinguaPlone.public import BaseContent
from Products.LinguaPlone.public import registerType
from Products.Archetypes.Schema.factory import instanceSchemaFactory
from Products.LinguaPlone.utils import LocateTranslation
from Products.LinguaPlone.interfaces import ILocateTranslation
from Products.LinguaPlone.interfaces import ITranslatable

from zope.component import testing
from zope.component import provideAdapter

class testBaseContent(BaseContent):
    '''
    def __init__(self):
        super(testBaseObject, self).__init__()
        self._language = None

    def Language(self):
        return self._language

    def UID(self):
        return None
    '''

registerType(testBaseContent)

class TestTranslated(unittest.TestCase):
    site_languages = ['fr', 'en', 'nl']
    def setUp(self):
        testing.setUp(self)
        provideAdapter(instanceSchemaFactory)
        # or provideAdapter(instanceSchemaFactory, [IBaseOjbect], ISchema)
        provideAdapter(LocateTranslation)
        #provideAdapter(LocateTranslation, [ILocateTranslation], ITranslatable)
    
    def tearDown(self):
        testing.tearDown(self)

    def test_translated_in_nl(self):
        fr_object = testBaseContent('fr_object')
        fr_object.setLanguage('fr')
        status, description  = check_translated(fr_object, self.site_languages, 'nl')
        self.assertFalse(status)

    def test_neutral(self):
        neutral_object = testBaseContent('neutral_object')
        status, description  = check_translated(neutral_object, self.site_languages, 'nl')
        self.assertFalse(status)
    
    def test_current_language(self):
        fr_object = testBaseContent('fr_object')
        fr_object.setLanguage('fr')
        status, description  = check_translated(fr_object, self.site_languages, 'fr')
        self.assertFalse(status)

    def test_translated(self):
        fr_object = testBaseContent('fr_object')
        fr_object.setLanguage('fr')
        nl_object = testBaseContent('nl_object')
        nl_object.setLanguage('nl')

        fr_object.addTranslation(nl_object)
        status, description  = check_translated(fr_object, self.site_languages, 'nl')
        self.assertTrue(status)
        
        status, description  = check_translated(nl_object, self.site_languages, 'fr')
        self.assertTrue(status)

