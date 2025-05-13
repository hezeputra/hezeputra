# Python installation, configuration and deployment guide

## Python installation

1. Dependencies installation

```
sudo apt install -y python3 python3-pip python3-venv
```

2. Create and Activate a Virtual Environment

```
python3 -m venv parkingsystem_env
```

3. Enter the Virtual Environment

```
source parkingsystem_env/bin/activate
```

4. Install the venv dependencies

```
pip3 install evdev
```

## Running Python as a Service

### Running phyton script

1. asd

```
chmod +x /home/youruser/your_project/rfid_reader.py
```

2. Create service at `/etc/systemd/system/MYSERVICE.service`

```
[Unit]
Description=DESCRITPTION
After=network.target

[Service]
WorkingDirectory=/path/to/working/directory
ExecStart=/path/to/VIRTUAL_ENV/bin/python /path/to/your/script/SCRIPTNAME.py
Restart=always
RestartSec=5
user=root
group=root
StandardOutput=append:/var/log/MYSERVICE.log
StandardError=append:/var/log/MYSERVICE.err

[Install]
WantedBy=multi-user.target
```

2. Reload the service daemon

```
sudo systemctl daemon-reload
sudo systemctl enable MYSERVICE.service
sudo systemctl start MYSERVICE.service
sudo systemctl status MYSERVICE.service
```

> [!IMPORTANT]
>
> 1. Replace `MYSERVICE` with the service name.
> 2. Replace `DESCRITPTION` with the service description.
> 3. Replace `SCRIPTNAME` with the script name.
> 4. Replace `VIRTUAL_ENV` with the virtual env folder name.

### Running phyton bytecode

```
python3 -m py_compile parkingsystem.py
mv __pycache__/parkingsystem.cpython-*.pyc /opt/parkingsystem/parkingsystem.pyc
mv -r parkingsystem_env /opt/parkingsystem/parkingsystem_env
```

2. Create service at `/etc/systemd/system/rfidreader.service`

```
[Unit]
Description=DESCRITPTION
After=network.target

[Service]
WorkingDirectory=/path/to/working/directory
ExecStart=/opt/SCRIPTNAME/VIRTUAL_ENV/bin/python /opt/SCRIPTNAME/SCRIPTNAME.pyc
Restart=always
RestartSec=5
user=root
group=root
StandardOutput=append:/var/log/MYSERVICE.log
StandardError=append:/var/log/MYSERVICE.err

[Install]
WantedBy=multi-user.target

```

> [!IMPORTANT]
>
> 1. Replace `MYSERVICE` with the service name.
> 2. Replace `DESCRITPTION` with the service description.
> 3. Replace `SCRIPTNAME` with the script name.
> 4. Replace `VIRTUAL_ENV` with the virtual env folder name.
