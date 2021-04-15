FROM ubuntu:20.04 as builder

LABEL maintainer="Jorge Camarero Vera"
LABEL maintainer_mail="jorge.camarero@nexplore.com"

# Set build path
ENV BUILDPATH /build
ENV DEBIAN_FRONTEND=noninteractive

RUN set -ex; \
  apt-get update && apt-get install -y \
    build-essential g++ \
    wget; \
  apt-get clean;

# Set the working directory
WORKDIR $BUILDPATH

# Muscle
RUN set -ex; \
  wget https://www.drive5.com/muscle/muscle_src_3.8.1551.tar.gz; \
  mkdir muscle; \
  tar -zxvf muscle_src_3.8.1551.tar.gz --directory ./muscle/; \
  cd muscle; \
  make -j`nproc`;

# Development Docker
FROM ubuntu:20.04

LABEL maintainer="Jorge Camarero Vera"
LABEL maintainer_mail="jorge.camarero@nexplore.com"

ENV DEBIAN_FRONTEND=noninteractive
ENV USER="bio"

COPY --from=builder /build/muscle/muscle /usr/local/bin/muscle

RUN set -ex; \
  apt-get update && apt-get install -y \
    python3 python3-pip \
    rename \
    gnumeric; \
  apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY ./requirements.txt /build

RUN set -ex; \
  python3 -m pip install -r /build/requirements.txt; \
  rm -rf /build

# Create user develop and give permissions
RUN set -ex; \
  useradd -ms /bin/bash $USER;

USER $USER
VOLUME "/home/$USER/project"
WORKDIR /home/$USER/project
