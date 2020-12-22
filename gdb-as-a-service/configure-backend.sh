#!/bin/sh

kctf-kubectl apply -f backend-config.yaml
kctf-kubectl annotate service/gdb-as-a-service-lb-service 'cloud.google.com/backend-config={"default":"gdb-as-a-service"}' --overwrite
