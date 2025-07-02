# Hailo AI Data Flow Compiler Installation Guide

## Prerequisite

1. Please download the Data Flow Compiler from [Hailo AI Dev Zone SW Download](https://hailo.ai/developer-zone/software-downloads/) and select the suitable operating system, system architecture and python version
2. Please noted that based on the official documentation, the DFC version 3.31.0 only support python 3.8/3.9/3.10 and operating system ubuntu 20.04/22.04

## Installation

1. Update the apt repository

```
apt-get update && apt-get full-upgrade -y
```

2. Install Dependencies

```
apt install -y build-essential graphviz graphviz-dev libgraphviz-dev pkg-config python3-dev python3-distutils python3-tk python3-venv
```

3. Create virtual environment

```
python3 -m venv {env_name}
```

> [!IMPORTANT]
>
> please replace {env_name} with the virtual environment name

4. Activate the virtual environment

```
source {env_name}/bin/activate
```

5. Install the downloaded Hailo Data Flow Compiler

```
pip install {dfc_name}
```

> [!IMPORTANT]
>
> please replace {dfc_name} with the .whl DFC file from official Hailo Dev Zone website
