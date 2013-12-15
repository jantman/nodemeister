#!/bin/bash -x

NAME=`date +%Y-%m-%d_%H-%M-%S`
python ../../manage.py dumpdata  enc > ${NAME}.json
pg_dump -U nodemeister --clean nodemeister > ${NAME}.sql
wget -O ${NAME}.yaml http://localhost:8000/enc/puppet/testnode
