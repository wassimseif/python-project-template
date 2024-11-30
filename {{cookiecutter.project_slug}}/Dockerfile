FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn8-devel
LABEL maintainer="wassim.seifeddine@toptal.com"
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /workspace
RUN apt-get update && \
    apt-get install -y \
    wget \
    git \
    curl \
    htop \
    libsox-dev \
    build-essential \
    zsh \
    && rm -rf /var/lib/apt/lists/*

ARG HF_TOKEN
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN apt update
RUN apt install -y gcc g++
COPY requirements.txt /workspace
RUN python3 -m pip install -r requirements.txt

