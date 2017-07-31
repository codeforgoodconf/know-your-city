# Tasks to be run inside app container

LOCAL_IN = requirements/local.in
LOCAL_OUT = requirements/local.txt

pip-compile:
	pip install -q pip-tools
	pip-compile requirements/app.in
	pip-compile requirements/dev.in
	pip-compile requirements/test.in
ifneq (, $(wildcard $(LOCAL_IN)))
	pip-compile $(LOCAL_IN)
else
endif

pip-compile-upgrade:
	pip install -q pip-tools
	pip-compile -U requirements/app.in
	pip-compile -U requirements/dev.in
	pip-compile -U requirements/test.in
ifneq (, $(wildcard $(LOCAL_IN)))
	pip-compile -U $(LOCAL_IN)
endif

install-dev-requirements:
	pip install -q pip-tools
ifneq (, $(wildcard $(LOCAL_OUT)))
	pip-sync $(LOCAL_OUT)
else
	pip-sync requirements/dev.txt
endif
