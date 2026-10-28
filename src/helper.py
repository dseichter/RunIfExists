# Copyright (c) 2024 Daniel Seichter
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
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import logging

import urllib3
from packaging import version

logger = logging.getLogger(__name__)

VERSION = "v2025-12-21"
UPDATEURL = 'https://api.github.com/repos/dseichter/RunIfExists/releases/latest'
RELEASES = 'https://github.com/dseichter/RunIfExists/releases'
NAME = 'RunIfExists'
LICENCE = 'GPL-3.0'


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', UPDATEURL)
        releases = json.loads(r.data.decode('utf-8'))
        # Find the latest stable (not prerelease) release
        for release in releases:
            if not release.get('prerelease', False):
                latest_version = release.get('tag_name')
                if not isinstance(latest_version, str):
                    continue
                return version.parse(latest_version) > version.parse(VERSION)
        return False  # No stable release found
    except (
        urllib3.exceptions.HTTPError,
        UnicodeDecodeError,
        json.JSONDecodeError,
        version.InvalidVersion,
    ) as e:
        logger.error(f"Error checking for new release: {e}")
        return False
