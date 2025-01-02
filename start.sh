#! /bin/bash

uwsgi --ini /code/uwsgi.ini --static-map /static=/static
tail -f /var/log/uwsgi/api.log
