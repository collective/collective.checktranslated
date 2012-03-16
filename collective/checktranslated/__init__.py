# -*- extra stuff goes here -*-

from zope.i18nmessageid import MessageFactory
checktranslatedMessageFactory = MessageFactory('collective.checktranslated')

'''
from collective.jekyll.diagnosis import DiagnosisFactory
from collective.jekyll.diagnosis import Diagnosis

from collective.checktranslated import checktranslatedMessageFactory as _

from zope.app.component.hooks import getSite

def __init__(self, lang):
    import pdb; pdb.set_trace()
    self.lang = lang

def __call__(self, value):
    import pdb; pdb.set_trace()
    pass

site = getSite()
for lang in site.portal_languages.getAvailableLanguages().keys():
    exec "CheckTranslated{0} = type('CheckTranslated{0}', (DiagnosisFactory,), {'__init__':__init__('lang'={0}),'__call__':__call__('value')}".format(lang)
'''
def initialize(context):
    """Initializer called when used as a Zope 2 product."""
