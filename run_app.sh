#!/bin/bash
# this variables needs to export because of other environment dependencies
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# here --server.port needs to use same port that is forwarded in terminal and while
# running/creating the docker container
# here forwarded port is 8502, in case of local no need to forward any port use default port as 8502
streamlit run app.py --server.address=0.0.0.0 --server.port=8502
