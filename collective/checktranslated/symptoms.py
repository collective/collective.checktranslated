# -*- coding: utf-8 -*-
from zope.component.hooks import getSite
from collective.jekyll.symptoms import SymptomBase

from collective.checktranslated import checktranslatedMessageFactory as _


class HasTranslatedNL(SymptomBase):
    title = _(u"NL translated")
    help = _(u"")

    def _update(self):
        site = getSite()
        languages = site.portal_languages.getAvailableLanguages().keys()
        self.status, self.description = check_translated(self.context, languages, 'nl')

class HasTranslatedEN(SymptomBase):
    title = _(u"EN translated")
    help = _(u"")

    def _update(self):
        site = getSite()
        languages = site.portal_languages.getAvailableLanguages().keys()
        self.status, self.description = check_translated(self.context, languages, 'en')

class HasTranslatedFR(SymptomBase):
    title = _(u"FR translated")
    help = _(u"")

    def _update(self):
        site = getSite()
        languages = site.portal_languages.getAvailableLanguages().keys()
        self.status, self.description = check_translated(self.context, languages, 'fr')


def check_translated(context, languages, lang):
    site_languages = languages
    current_lang = context.Language()
    status = ''
    description = ''
    if len(site_languages) > 1 and current_lang in site_languages:
        site_languages.remove(current_lang)
    else:
        status = False
        description = _(u"This is a neutral language object.")
        return status, description

    if current_lang == lang:
        status = True
        description = _("This is the current language.")
    elif not languages:
        status = False
        description = _(u"There is only one language installed on your site ({0}).".format(current_lang))
    elif lang not in languages:
        status = False
        description = _(u"{0} is not installed on your site.".format(lang))
    else:
        if hasattr(context, 'getTranslation'):
            translate_context = context.getTranslation(lang)
            if translate_context is None:
                status = False
                description = _(u"There is no {0} translation".format(lang))
            else:
                status = True
                description = _(u"All right.")

    return status, description
