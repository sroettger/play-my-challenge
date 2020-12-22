#!/bin/sh

kctf-kubectl apply -f backend-config.yaml
kctf-kubectl annotate service/pwngdb-lb-service 'cloud.google.com/backend-config={"default":"pwngdb"}' --overwrite
