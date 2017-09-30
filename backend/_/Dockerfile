FROM python:3.6

ARG HOSTUID=1000
ARG HOSTGID=1000

# create mount directories
RUN mkdir /backend
RUN chown $HOSTUID:$HOSTGID /backend
VOLUME /backend

# add host user
RUN addgroup --gid $HOSTGID backend
RUN adduser --uid $HOSTUID --gid $HOSTGID  --gecos "" --disabled-password --quiet backend

EXPOSE 5000

WORKDIR /backend

# install dependencies and start
CMD /backend/_/startup_development.sh
