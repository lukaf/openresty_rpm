#!/bin/sh

tag=$1

(cd ngx_openresty && \
    git log --pretty=format:"* %cd %aN <%ae>%n- (%h) %s%n" --date=local ${tag} \
    | sed -r 's/([0-9]+) [0-9]+:[0-9]+:[0-9]+ /\1 /')
