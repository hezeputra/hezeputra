#!/bin/bash
set -x

cd /opt/exoai/exoai-engine || exit 1

if ! source setup_env.sh; then
  echo "Failed to source setup_env"
  exit 1
fi

echo "Environment activated. Running Python app..."

python basic_pipelines/pose.py --use-frame --input url