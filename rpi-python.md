# Python installation, configuration and deployment guide

## Python installation

1. Dependencies installation

```
sudo apt install -y python3 python3-pip python3-venv
```

2. Create and Activate a Virtual Environment

```
python3 -m venv rfid_env
```

3. Enter the Virtual Environment

```
source rfid_env/bin/activate
```

4. Install the venv dependencies

```
pip3 install evdev
```

## Running Python as a Service

1. asd

```
chmod +x /home/youruser/your_project/rfid_reader.py
```

1. Create service at `/etc/systemd/system/MYSERVICE.service`

```
[Unit]
Description=DESCRITPTION
After=network.target

[Service]
WorkingDirectory=/path/to/working/directory
ExecStart=/path/to/virtual_env/bin/python /path/to/your/script
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
