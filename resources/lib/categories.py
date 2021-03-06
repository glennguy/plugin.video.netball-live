import sys

from aussieaddonscommon import utils

from resources.lib import config

import xbmcgui

import xbmcplugin

_handle = int(sys.argv[1])
_url = sys.argv[0]


def list_categories():
    try:
        listing = []
        categories = config.CATEGORIES
        for category in sorted(categories.keys()):
            li = xbmcgui.ListItem(category[2:])
            urlString = '{0}?action=listcategories&category={1}'
            url = urlString.format(_url, categories[category])
            is_folder = True
            listing.append((url, li, is_folder))

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)
    except Exception:
        utils.handle_error('Unable to display categories')
