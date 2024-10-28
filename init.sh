#!/bin/zsh
source ~/.zshrc

# python env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# https://pulsar.apache.org/docs/4.0.x/getting-started-docker-compose/#step-2-create-a-pulsar-cluster
mkdir -p ./data/zookeeper ./data/bookkeeper
