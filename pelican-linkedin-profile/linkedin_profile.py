# -*- coding: utf-8 -*-
'''
pelican-linked
-------

The linked plugin generates a new Jinja variable containing all your LinkedIn profile information
'''

from __future__ import unicode_literals
from pelican import signals
from pelican.generators import Generator
from linkedin import linkedin
from linkedin.exceptions import LinkedInError
import logging

logger = logging.getLogger(__name__)

# Link pelican lang to linkedin language-code
_LANGUAGE_ASSOCIATION = {
    "en" : "en-US",
    "ar" : "ar-AE",
    "zh" : "zh-CN",
    "zh" : "zh-TW",
    "cs" : "cs-CZ",
    "da" : "da-DK",
    "nl" : "nl-NL",
    "fr" : "fr-FR",
    "de" : "de-DE",
    "in" : "in-ID",
    "it" : "it-IT",
    "ja" : "ja-JP",
    "ko" : "ko-KR",
    "ms" : "ms-MY",
    "no" : "no-NO",
    "pl" : "pl-PL",
    "pt" : "pt-BR",
    "ro" : "ro-RO",
    "ru" : "ru-RU",
    "es" : "es-ES",
    "sv" : "sv-SE",
    "tl" : "tl-PH",
    "th" : "th-TH",
    "tr" : "tr-TR"
}

_SELECTORS = [
    'last-modified-timestamp',
    'formatted-name',
    'headline',
    'summary',
    'picture-url',
    'email-address',
    'public-profile-url',
    'primary-twitter-account',
    'phone-numbers',
    'skills',
    'languages',
    'positions',
    'educations'
]


class LinkedInProfileGenerator(Generator):
    def __init__(self, *args, **kwargs):
        super(LinkedInProfileGenerator, self).__init__(*args, **kwargs)
        self.linkedin_lang = "en_US"
        self.linkedin_profile = None

        user_token = None
        user_secret = None
        consumer_key = None
        consumer_secret = None
        return_url = None

        if 'LINKEDIN_USER_TOKEN' in self.settings:
            user_token = self.settings['LINKEDIN_USER_TOKEN']
        else:
            logger.error("Missing LINKEDIN_USER_TOKEN in settings")
            return
        if 'LINKEDIN_USER_SECRET' in self.settings:
            user_secret = self.settings['LINKEDIN_USER_SECRET']
        else:
            logger.error("Missing LINKEDIN_USER_SECRET in settings")
            return
        if 'LINKEDIN_CONSUMER_KEY' in self.settings:
            consumer_key = self.settings['LINKEDIN_CONSUMER_KEY']
        else:
            logger.error("Missing LINKEDIN_CONSUMER_KEY in settings")
            return
        if 'LINKEDIN_CONSUMER_SECRET' in self.settings:
            consumer_secret = self.settings['LINKEDIN_CONSUMER_SECRET']
        else:
            logger.error("Missing LINKEDIN_CONSUMER_SECRET in settings")
            return
        if 'LINKEDIN_RETURN_URL' in self.settings:
            return_url = self.settings['LINKEDIN_RETURN_URL']
        else:
            logger.error("Missing LINKEDIN_RETURN_URL in settings")
            return

        current_lang = self.settings['DEFAULT_LANG']
        if current_lang in _LANGUAGE_ASSOCIATION.keys():
            self.linkedin_lang = _LANGUAGE_ASSOCIATION[current_lang]
        self.headers = {'Accept-Language': self.linkedin_lang}

        try:
            authentication = linkedin.LinkedInDeveloperAuthentication(
                consumer_key, consumer_secret, user_token, user_secret,
                return_url, linkedin.PERMISSIONS.enums.values())
            application = linkedin.LinkedInApplication(authentication)
            self.linkedin_profile = application.get_profile(
                selectors=_SELECTORS,
                headers=self.headers)
        except LinkedInError as exception:
            logger.error(str(exception))
            return

    def generate_context(self):
        logger.info('Adding LinkedIn profile to context')
        if self.linkedin_profile is None:
            return
        # linkedin profile refactoring
        profile = {}
        # PersonalInfo
        if 'summary' in self.linkedin_profile:
            profile['summary'] = self.linkedin_profile['summary']
        else:
            profile['summary'] = 'Empty'
        profile['formattedName'] = self.linkedin_profile['formattedName']
        profile['headline'] = self.linkedin_profile['headline']
        profile['pictureUrl'] = self.linkedin_profile['pictureUrl']
        profile['emailAddress'] = self.linkedin_profile['emailAddress']
        profile['primaryTwitterAccount'] = self.linkedin_profile['primaryTwitterAccount']
        profile['publicProfileUrl'] = self.linkedin_profile['publicProfileUrl']
        profile['phoneNumbers'] = self.linkedin_profile['phoneNumbers']['values']
        # Skills
        skills = []
        for skill in self.linkedin_profile['skills']['values']:
            skills.append(skill['skill']['name'])
        profile['skills'] = skills
        # Languages
        languages = []
        for language in self.linkedin_profile['languages']['values']:
            languages.append(language['language']['name'])
        profile['languages'] = languages
        # Educations
        educations = []
        for education in self.linkedin_profile['educations']['values']:
            if 'fieldOfStudy' not in education:
                education['fieldOfStudy'] = "Empty"
            educations.append(education)
        profile['educations'] = educations
        # Positions
        positions = []
        for position in self.linkedin_profile['positions']['values']:
            if position['isCurrent']:
                position['endDate'] = None
            if 'summary' not in position:
                position['summary'] = "Empty"
            positions.append(position)
        profile['positions'] = positions

        self.context['linkedin_profile'] = profile


def get_generators(generators):
    return LinkedInProfileGenerator


def register():
    signals.get_generators.connect(get_generators)
