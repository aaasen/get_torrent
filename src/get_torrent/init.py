#!/usr/bin/env python2

from get_torrent import GetTorrent

from pprint import pprint

tpb = GetTorrent('../../sources/pirate_bay.json')
torrents = tpb.search('ubuntu', sort='seeders')

pprint(vars(torrents[0]))
