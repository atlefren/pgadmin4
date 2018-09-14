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
        'label': gettext('Layer Name')
    },
    {
        'name': 'tileUrl',
        'type': 'text',
        'label': gettext('Tile Url')
    },
    {
        'name': 'maxZoom',
        'type': 'integer',
        'label': gettext('Max Zoom level')
    },
    {
        'name': 'attribution',
        'type': 'text',
        'label': gettext('Attribution text')
    },
    {
        'name': 'subdomains',
        'type': 'text',
        'label': gettext('subdomains for url')
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
            'Description here'
        ),
        fields=fields
    )
