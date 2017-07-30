#!/bin/bash
set -e

make install-dev-requirements
exec ./manage.py runserver "0.0.0.0:${DJANGO_PORT}"
