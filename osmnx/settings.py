################################################################################
# Module: settings.py
# Description: Global settings, can be configured by user by passing values to
#              utils.config()
# License: MIT, see full license in LICENSE.txt
# Web: https://github.com/gboeing/osmnx
################################################################################

import logging as lg


# locations to save data, logs, images, and cache
data_folder = 'data'
logs_folder = 'logs'
imgs_folder = 'images'
cache_folder = 'cache'

# cache server responses
use_cache = False

# write log to file and/or to console
log_file = False
log_console = False
log_level = lg.INFO
log_name = 'osmnx'
log_filename = 'osmnx'

# useful osm tags - note that load_graphml expects a consistent set of tag names
# for parsing
useful_tags_node = ['ref', 'highway']
useful_tags_path = ['bridge', 'tunnel', 'oneway', 'lanes', 'ref', 'name',
                    'highway', 'maxspeed', 'service', 'access', 'area',
                    'landuse', 'width', 'est_width', 'junction']

# default filter for OSM "access" key. filtering out "access=no" ways prevents
# including transit-only bridges like tilikum crossing from appearing in drivable
# road network (e.g., '["access"!~"private|no"]'). however, some drivable 
# tollroads have "access=no" plus a "access:conditional" key to clarify when 
# it is accessible, so we can't filter out all "access=no" ways by default.
# best to be permissive here then remove complicated combinations of tags in 
# python after the full graph is downloaded and constructed.
default_access = '["access"!~"private"]'

# default CRS to set when creating graphs
default_crs = {'init':'epsg:4326'}
