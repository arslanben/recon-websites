#!/bin/bash

CURRENT_PYTHON=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

REQUIRED_VERSION="3.6"

version_gt() { test "$(printf '%s\n' "$@" | sort -V | head -n 1)" != "$1"; }

if version_gt $REQUIRED_VERSION $CURRENT_PYTHON; then
    echo "Python sürümünüz $CURRENT_PYTHON. Updating..."
    sudo apt update
    sudo apt install -y python3 python3-pip
    NEW_PYTHON=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    echo "Python updated. Current version: $NEW_PYTHON"
else
    echo "Your Python version is current.: $CURRENT_PYTHON"
fi
