##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from threading import local
from zope import component, interface
from zope.publisher.interfaces.http import IHTTPRequest

from zope.traversing.namespace import view
from zope.traversing.browser.interfaces import IAbsoluteURL
from zope.traversing.browser.absoluteurl import AbsoluteURL

from interfaces import IURLMapper, IURLMapperAware


class SectionAbsoluteURL(AbsoluteURL):
    interface.implementsOnly(IAbsoluteURL)
    component.adapts(IURLMapperAware, IHTTPRequest)

    def __str__(self):
        mapper = IURLMapper(self.context, None)
        if mapper is not None and mapper.enabled:
            value = mapper.url
            if value and sectionProcessing.process:
                return value[:-1]

        return super(SectionAbsoluteURL, self).__str__()

    __call__ = __str__


class SectionPrcessing(local):

    process = True

sectionProcessing = SectionPrcessing()


class SectionURL(view):

    def traverse(self, name, ignored):
        self.request.shiftNameToApplication()
        sectionProcessing.process = True
        return self.context


class NoSectionURL(view):

    def traverse(self, name, ignored):
        self.request.shiftNameToApplication()
        sectionProcessing.process = False
        return self.context
