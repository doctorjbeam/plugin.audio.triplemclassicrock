import sys
import xbmcgui
import xbmcplugin
import os
import xbmcaddon

addon = xbmcaddon.Addon()
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
addon_dir = addon.getAddonInfo('path')
url = os.path.join( addon_dir, 'resources', 'data', 'triplemclassicrock.strm' )

li = xbmcgui.ListItem('Triple M Classic Roc - Live Stream', iconImage='', thumbnailImage='')
li.setProperty('fanart_image', '')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)