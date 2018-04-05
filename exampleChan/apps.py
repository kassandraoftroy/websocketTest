# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ExamplechanConfig(AppConfig):
    name = 'exampleChan'

    def ready(self):
        import exampleChan.signals