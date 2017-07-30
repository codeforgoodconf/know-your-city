FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install --no-install-recommends -y \
  bash-completion \
  && rm -rf /var/lib/apt/lists/*
RUN echo 'source /usr/share/bash-completion/bash_completion' >> /etc/bash.bashrc

ADD https://rawgit.com/django/django/stable/1.11.x/extras/django_bash_completion /etc/bash_completion.d/
RUN echo 'export HISTFILE=$HOME/.bash_history/history' >> $HOME/.bashrc

WORKDIR /app
COPY requirements/dev.txt requirements/dev.txt
RUN pip install -r requirements/dev.txt && rm -rf /root/.cache

ARG TINI_VERSION
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]
