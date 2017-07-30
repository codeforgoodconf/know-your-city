#!/bin/bash
set -e

make install-dev-requirements
exec ./manage.py runserver_plus "0.0.0.0:${PORT}" --cert /tmp/cert
