FROM python:3.10-rc-buster
ENV TZ=Europe/Madrid

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone


# apt
RUN apt update && \
    apt install -y -q \
      bash-completion \
      bsdmainutils \
      curl \
      git \
      vim \
      wget && \
    rm -rf /var/lib/apt/lists/*

# pip
RUN python -m pip install --upgrade pip && pip check

# install rshell
RUN pip install rshell


ARG USER_ID=1000
ARG USERNAME="user"
ARG RPI_TTY="/dev/ttyACM0"
WORKDIR /app

RUN if [ "$USER_ID" -eq "1000" ]; then useradd -m --uid $USER_ID $USERNAME; else USERNAME="root"; fi

# .bashrc
RUN echo "alias ll='ls -la'" >> ~/.bashrc && \
    echo "PS1='\u@\h:\w [\e[0;33m\$(git branch 2>/dev/null | grep '^*' | colrm 1 2)\e[m]\$ '" >> ~/.bashrc
    