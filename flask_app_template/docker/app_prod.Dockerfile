FROM python:3.9-buster

# We don't want to run our application as root if it is not strictly necessary, even in a container.
# Create a user and a group called 'app' to run the processes.
# A system user is sufficient and we do not need a home.
# We provide specific UID and GID, and make sure that they are ok to use on the host system.
# The GID is gsd_ma group on Ocean
# The UID is domantas on Ocean, maybe we need a generic UID for our stuff?
ARG UNAME=app
ARG UID=1205
ARG GID=1207
RUN groupadd -g $GID -o $UNAME
RUN useradd --system --no-create-home -u $UID -g $GID -s /bin/bash $UNAME

# workdir is /app/back because backend code is in this folder so it will be the context
WORKDIR /app

# note, we're copying the requirements.txt in the /back/ folder to correspond to modules needed  for the backend ;)
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy the backend folder with all the code & co
COPY . /app

# Install from the requirements.txt we copied above
RUN chown -R app:app /app

# Subsequent commands, either in this Dockerfile or in a
# docker-compose.yml, will run as user 'app'
USER $UNAME

# We are done with setting up the image.
# As this image is used for different
# purposes and processes no CMD or ENTRYPOINT is specified here,
# this is done in docker-compose.yml.

