# RPI Hailo

this guide is associated with hailo-ai/hailo-rpi5-examples

1. install the dependencies

```
./install.sh
```

2. Initial the venv

```
source setup_env.sh
```

3. install additional dependencies

```
pip3 install meson fastapi uvcorn
```

4. Create init script

```
#!/bin/bash
set -x

cd /opt/exoai/exoai-engine || exit 1

if ! source setup_env.sh; then
  echo "Failed to source setup_env"
  exit 1
fi

echo "Environment activated. Running Python app..."

python basic_pipelines/pose.py --use-frame --input url
```

5. Made the init script executeable

```
chmod +x /opt/exoai/init.sh
```
