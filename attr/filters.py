"""
Commonly useful filters for :func:`attr.asdict`.
"""

from __future__ import absolute_import, division, print_function

import inspect

from ._make import Attribute


def _split_what(what):
    """
    Returns a tuple of `frozenset`s of classes and attributes.
    """
    return (
        frozenset(cl for cl in what if inspect.isclass(cl)),
        frozenset(cl for cl in what if isinstance(cl, Attribute)),
    )


def include(*what):
    """
    Whitelist *what*.

    :param what: What to whitelist.
    :type what: :class:`list` of :class:`type` or :class:`attr.Attribute` s.

    :rtype: :class:`callable`
    """
    cls, attrs = _split_what(what)

    def include_(attribute, value):
        return value.__class__ in cls or attribute in attrs

    return include_


def exclude(*what):
    """
    Blacklist *what*.

    :param what: What to blacklist.
    :type what: :class:`list` of classes or :class:`attr.Attribute` s.

    :rtype: :class:`callable`
    """
    cls, attrs = _split_what(what)

    def exclude_(attribute, value):
        return value.__class__ not in cls and attribute not in attrs

    return exclude_
