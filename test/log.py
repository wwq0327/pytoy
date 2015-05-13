#!/usr/bin/env python

import logging

logging.basicConfig(
	filename = "app.log",
	format = "%(levelname)-10s %(asctime)s %(message)s",
	level = logging.INFO
	)

logging.debug('hello, world!')