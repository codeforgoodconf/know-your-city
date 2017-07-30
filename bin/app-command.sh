#!/bin/bash
set -e

make install-dev-requirements
npm i
exec ./manage.py runserver_plus "0.0.0.0:${PORT}" --cert /tmp/cert
