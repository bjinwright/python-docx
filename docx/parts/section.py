# encoding: utf-8

"""
Provides HeaderPart and related objects
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from ..opc.part import XmlPart
from ..shared import lazyproperty
from docx.blkcntnr import BlockItemContainer


class HeaderPart(XmlPart):
    """
    Proxy for the styles.xml part containing style definitions for a document
    or glossary.
    """

    @lazyproperty
    def header(self):
        """
        The |_Header| instance containing the header (<w:???> element
        proxies) for this header part.
        """
        return _Header(self._element, self)


class FooterPart(XmlPart):
    """"""

    @lazyproperty
    def footer(self):
        """"""
        return _Footer(self._element, self)


class _Header(BlockItemContainer):
    def __init__(self, header_elm, parent):
        super(_Header, self).__init__(header_elm, parent)
        self._header_elm = header_elm


class _Footer(BlockItemContainer):
    def __init__(self, footer_elm, parent):
        super(_Footer, self).__init__(footer_elm, parent)
        self._footer_elm = footer_elm