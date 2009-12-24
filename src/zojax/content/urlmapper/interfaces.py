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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory

from z3c.schema.baseurl import BaseURL

_ = MessageFactory('zojax.content.urlmapper')


class IURLMapper(interface.Interface):
    """ mapped section """

    enabled = schema.Bool(
        title = _('Map URL'),
        description = _('If enabled, content URL will be mapped'),
        default=False)

    url = BaseURL(
        title = _(u'URL'),
        description = _(u'Define url mapper for content.'),
        required = True)


class IURLMappable(interface.Interface):
    """ url mappable marker """


class IURLMapperAware(interface.Interface):
    """ url mapper aware marker """
