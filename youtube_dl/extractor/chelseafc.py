from __future__ import unicode_literals
import re
from .common import InfoExtractor
from ..compat import (
    compat_parse_qs,
    compat_urllib_parse_urlparse,
)
from ..utils import (
    parse_duration,
    parse_iso8601,
    traverse_obj,
    float_or_none,
    int_or_none,
    remove_start,
)

class ChelseafcIE(InfoExtractor):
    #https?: Matches either http or https.
    #://: Matches the literal characters ://.
    #(?:www\.)?: Matches an optional www. prefix, using a non-capturing group (?:...)
    #(?:/[a-z]+)?: Matches an optional path component, where [a-z]+ matches one or more lowercase letters.

    _VALID_URL = r'https?://(?:www\.)?chelseafc\.com/en/video/(?P<id>[a-z0-9]+(?:-[a-z0-9]+)*)'

    _TEST = {
        'url': 'https://www.chelseafc.com/en/video/extended-chelsea-0-2-brentford-28-10-2023',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'Video title goes here',
            'thumbnail': r're:^https?://.*\.jpg$',
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
    