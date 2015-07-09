==============
Pelican LinkedIn
==============

Extract a LinkedIn profile and allow the use of his informations in Pelican's pages

Installation
============

To install pelican-linkedin, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-linkedin-profile

Configuration
=============

Enable the plugin in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican-linkedin-profile',
        # ...
    ]

Add mandatory settings containing your LinkedIn Api Keys.

.. code-block:: python

    LINKEDIN_USER_TOKEN = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
    LINKEDIN_USER_SECRET = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
    LINKEDIN_CONSUMER_KEY = 'XXXXXXXXXXXXXX'
    LINKEDIN_CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
    LINKEDIN_RETURN_URL = 'http://example.com/'

Available data
==============
:formattedName:
    The member's name, formatted based on language.
:headline:
    The member's headline.
:summary:
    A long-form text area describing the member's professional profile.
:pictureUrl:
    A URL to the member's formatted profile picture, if one has been provided.
:emailAddress:
    The LinkedIn member's primary email address.
:primaryTwitterAccount:
    The primary Twitter account associated with the member.
:publicProfileUrl:
    The URL to the member's public profile on LinkedIn.
:phoneNumbers:
    A list of phone number objects containing those fields : phoneNumber, phoneType (home, work or mobile.)
:skills:
    A list of skill's name
:languages:
    A list of language's name
:educations:
    A list of eduction objects containing those fields : startDate, endDate, degree, schoolName, fieldOfStudy
:positions:
    A list of position objects containing those fields : startDate, endDate, title, company, summary, isCurrent. A company object contains those fields : industry, size, type, name

Usage
=====
In your templates you will have access to a linkedin_profile variable as below.

.. code-block:: html

    <div>
		<h2>{{ linkedin_profile.formattedName }}</h2>
		<p>{{ linkedin_profile.headline }}</p>
	</div>

License
=======

`GPLv2`_ license.

.. _GPLv2: http://opensource.org/licenses/GPL-2.0
