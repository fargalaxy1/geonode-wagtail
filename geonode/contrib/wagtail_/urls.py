# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.views.generic import TemplateView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from wagtail.wagtailcore.utils import WAGTAIL_APPEND_SLASH
from wagtail.wagtailcore import views

# if WAGTAIL_APPEND_SLASH:
#     # If WAGTAIL_APPEND_SLASH is True (the default value), we match a
#     # (possibly empty) list of path segments ending in slashes.
#     # CommonMiddleware will redirect requests without a trailing slash to
#     # a URL with a trailing slash
#     serve_pattern = r'^((?:[\w\-]+/)*)$'
# else:
#     # If WAGTAIL_APPEND_SLASH is False, allow Wagtail to serve pages on URLs
#     # with and without trailing slashes
#     serve_pattern = r'^([\w\-/]*)$'



# urlpatterns = patterns('geonode.people.views',
#                        url(r'^$', TemplateView.as_view(template_name='people/profile_list.html'),
#                            name='profile_browse'),
urlpatterns = patterns('',
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
   url(r'', include(wagtail_urls)),
    )

