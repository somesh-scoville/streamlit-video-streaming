# Streamlit video streaming
Video streaming using streamlit library

## [Application Demo](https://share.streamlit.io/kalesomeshwar/streamlit-video-streaming/main/app.py)

### Requirements
If docker container is created no need to run following command. <br />
Python 3.9 or later is required

```bash
$ pip install -r requirements.txt
```

#### To run application on remote server

```bash
$  ssh -i /Users/user_name/.ssh/id_rsa user_name@xxx.xxx.xxx.xx -L 8501:localhost:8501
```
```bash
$ bash run_app.sh
``` 

#### To run application locally

```bash
$ bash run_app.sh
``` 

### for docker
```bash
$ docker-compose up -d
```

To see the app in web browser use port 8501, http://localhost:8501/ <br />
one can change the port in [run_app.sh](run_app.sh).
