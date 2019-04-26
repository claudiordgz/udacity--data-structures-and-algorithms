#!/bin/bash -ex

function build_p0 {
  rm -rf P0.zip
  zip P0.zip P0/*.py P0/Analysis.txt
}

if [ -z $1 ]
then
  PROJECT="*** Unknown Project ***"
elif [ -n $1 ]
then
  PROJECT=$1
fi

case "$PROJECT" in 
  P0)
    build_p0
    ;;
  *) 
    echo "$PROJECT"
    ;;
esac

