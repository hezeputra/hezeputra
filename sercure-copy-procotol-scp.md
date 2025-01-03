# Transfer file into and from remote server using Secure Copy Protocol (SCP) [^1]

Replace `username` using your ssh username and `ipaddress` using your server ip address. Please specify the `port` if you use port other than default port 22 for ssh connection.

## Download from remote to local

```
scp -P port username@ipaddress:/remote/path/to/file/filename.format filename.format
```

## Upload from local to remote

```
scp -P port filename.format username@ipaddress:/remote/path/to/file/filename.format
```

[^1]: This instruction is tested in windows 10 and 11
