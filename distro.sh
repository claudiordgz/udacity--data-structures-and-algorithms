#!/bin/bash -ex

function build_p0 {
  mkdir -p ./P0/dist
  rm -rf ./P0/dist/submit.zip
  zip ./P0/dist/submit.zip P0/*.py P0/Analysis.txt
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

