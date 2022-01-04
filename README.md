# Streamlit video streaming
Video streaming using streamlit library

### Requirements

If docker container is created no need to run following command. <br />
Python 3.7 or later is required

```bash
$ pip install -r requirements.txt
```

## Video streaming application

#### To run application

on remote server

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

To see the app in web browser use port 8501, one can change the port in [run_app.sh](run_app.sh)
file

```angular2html
http://localhost:8501/
