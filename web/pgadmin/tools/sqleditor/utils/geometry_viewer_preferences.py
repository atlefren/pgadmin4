##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2018, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

"""Register preferences for geometry view"""
from flask_babelex import gettext


fields = [
    {
        'name': 'name',
        'type': 'text',
        'label': gettext('Layer Name'),
        'required': True,
    },
    {
        'name': 'tileUrl',
        'type': 'text',
        'label': gettext('Tile Url'),
        'required': True,
    },
    {
        'name': 'maxZoom',
        'type': 'int',
        'label': gettext('Max Zoom'),
    },
    {
        'name': 'attribution',
        'type': 'text',
        'label': gettext('Attribution'),
    },
    {
        'name': 'subdomains',
        'type': 'text',
        'label': gettext('Subdomains'),
    },
]

default_layers = [
    {
        'name': 'Street',
        'tileUrl': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
    },
    {
        'name': 'Topography',
        'tileUrl': 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        'maxZoom': 17,
        'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>, &copy; <a href="http://viewfinderpanoramas.org" target="_blank">SRTM</a>, &copy; <a href="https://opentopomap.org" target="_blank">OpenTopoMap</a>',
    },
    {
        'name': 'Gray Style',
        'tileUrl': 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}{r}.png',
        'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>, &copy; <a href="http://cartodb.com/attributions" target="_blank">CartoDB</a>',
        'subdomains': 'abcd'
    },
    {
        'name': 'Light Color',
        'tileUrl': 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>, &copy; <a href="http://cartodb.com/attributions" target="_blank">CartoDB</a>',
        'subdomains': 'abcd'
    },
    {
        'name': 'Dark Matter',
        'tileUrl': 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}{r}.png',
        'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>, &copy; <a href="http://cartodb.com/attributions" target="_blank">CartoDB</a>',
        'subdomains': 'abcd'
    },
]


def RegisterGeometryViewerPreferences(self):
    self.available_background_layers = self.preference.register(
        'geometryviewer', 'available_background_layers',
        gettext("Map background layers"), 'orderedlist', default_layers,
        category_label=gettext('Geometry Viewer'),
        help_str=gettext(
            'Add a new background layer for the map by entering a valid XYZ Tiles Url and a name. Other options relate to Leaflet TileLayer.'
        ),
        fields=fields
    )
