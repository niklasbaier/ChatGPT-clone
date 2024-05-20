#!/usr/bin/env bash

set -eux

python3 -m pip install --user pipx
python3 -m pipx ensurepath

POETRY_VERSION=$(bash scripts/cicd/setup/read_poetry_version.sh)

echo "Installing Poetry $POETRY_VERSION"
pipx install poetry==$POETRY_VERSION
