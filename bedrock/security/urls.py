# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import patterns, url

from bedrock.mozorg.util import page
from bedrock.security.views import (
    AdvisoriesView,
    AdvisoryView,
    OldAdvisoriesListView,
    OldAdvisoriesView,
    ProductView,
    ProductVersionView,
)


urlpatterns = patterns('',  # noqa
    page('', 'security/index.html'),
    page('bug-bounty', 'security/bug-bounty.html'),
    page('bug-bounty-faq', 'security/bug-bounty-faq.html'),
    page('bug-bounty-faq-webapp', 'security/bug-bounty-faq-webapp.html'),
    url(r'^advisories/$',
        AdvisoriesView.as_view(), name='security.advisories'),
    url(r'^advisories/mfsa(?P<pk>\d{4}-\d{2,3})/$',
        AdvisoryView.as_view(), name='security.advisory'),

    page('known-vulnerabilities', 'security/known-vulnerabilities.html'),
    page('known-vulnerabilities/older-vulnerabilities', 'security/older-vulnerabilities.html'),
    url(r'^known-vulnerabilities/(?P<slug>[a-z-]+)/$',
        ProductView.as_view(), name='security.product-advisories'),
    url(r'^known-vulnerabilities/(?P<slug>[\w-]+-\d{1,3}(\.\d{1,3})?)/$',
        ProductVersionView.as_view(), name='security.product-version-advisories'),

    url(r'^announce/\d{4}/mfsa(?P<pk>\d{4}-\d{2,3})\.html$', OldAdvisoriesView.as_view()),
    url(r'^announce/$', OldAdvisoriesListView.as_view()),
)
