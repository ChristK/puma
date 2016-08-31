#! /usr/bin/env python

import os.path
import config.config as config


###########################################################
# Make sure the directory structure is set up first.
# Everything in the cache is grabbed from elsewhere, or built on the fly,
# so it should all be considerd ready to be deleted at any point!
def build_file_tree(root_dir):
    # = Cache directory =
    if not os.path.exists(config.cache_dir):
        os.mkdir(config.cache_dir)

    if not os.path.exists(config.cache_dir + '/geodata'):
        os.mkdir(config.cache_dir + '/geodata')

    # = Data directory =
    if not os.path.exists(root_dir + '/data'):
        os.mkdir(root_dir + '/data')

    # = Log directory =
    if not os.path.exists(root_dir + '/logs'):
        os.mkdir(root_dir + '/logs')

    # = Output html directory =
    # Html dir
    if not os.path.exists(root_dir + "/html"):
        os.mkdir(root_dir + "/html")

    # Study html dir. This one is inside the previous one.
    if not os.path.exists(config.html_dir):
        os.mkdir(config.html_dir)

    html_directories = {"/mesh", "/css", "/papers", "/all_keywords", "/major_keywords", "/map", "/country", "/city", "/metrics", "/wordcloud", "/abstractwordcloud", "/authornetwork", "/errorlog", "/help"}

    for direct in html_directories:
        if not os.path.exists(config.html_dir + direct):
            os.mkdir(config.html_dir + direct)
