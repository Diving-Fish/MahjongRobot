### Install libs
`sudo apt -f -y install`

### Download chrome
```
wget ...
dpkg -i chrome.deb
```

### Pull & Run
```
docker pull richardchien/cqhttp:latest
docker run -ti --rm --name cqhttp-test -v $(pwd)/coolq:/home/user/coolq -p 9000:9000 -p 5700:5700 -e COOLQ_ACCOUNT=1969862413 richardchien/cqhttp:latest
```

### Start coolq and configure
Configure file at `coolq/app/io.github.richardchien.coolqhttpapi/config/<user-id>.json` like
```
{
    "host": "[::]",
    "port": 5700,
    "use_http": true,
    "ws_host": "[::]",
    "ws_port": 6700,
    "use_ws": false,
    "ws_reverse_url": "",
    "ws_reverse_api_url": "ws://172.17.0.1:8080/ws/api/",
    "ws_reverse_event_url": "ws://172.17.0.1:8080/ws/event/",
    "ws_reverse_reconnect_interval": 3000,
    "ws_reverse_reconnect_on_code_1000": true,
    "use_ws_reverse": true,
    "post_url": "",
    "access_token": "",
    "secret": "",
    "post_message_format": "string",
    "serve_data_files": false,
    "update_source": "github",
    "update_channel": "stable",
    "auto_check_update": false,
    "auto_perform_update": false,
    "show_log_console": true,
    "log_level": "info"
}
```

### Rerun
```
docker run -ti --rm --name cqhttp-test -v $(pwd)/coolq:/home/user/coolq -p 9000:9000 -p 5700:5700 -e COOLQ_ACCOUNT=1969862413 richardchien/cqhttp:latest
```
