#!/bin/bash
# this variables needs to export because of other environment dependencies
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# here --server.port needs to use same port that is forwarded in terminal and while
# running/creating the docker container
# here forwarded port is 8501, in case of local no need to forward any port use default port as 8501
streamlit run app_main.py --server.address=0.0.0.0 --server.port=8501
