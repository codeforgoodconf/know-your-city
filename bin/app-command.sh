#!/bin/bash
set -e

make install-dev-requirements
exec ./manage.py runserver_plus "0.0.0.0:${APP_PORT}" --cert /tmp/cert
