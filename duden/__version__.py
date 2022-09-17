# -*- coding: utf-8 -*-
"""
Contains module version constant
"""
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('duden').version
except Exception:
    __version__ = 'unknown'
