#!/bin/bash -ex

function build {
  local project_dir=$1
  mkdir -p ./$project_dir/dist
  rm -rf ./$project_dir/dist/submit.zip
  zip ./$project_dir/dist/submit.zip $project_dir/*.py $project_dir/Analysis.txt
}

function build_md {
  local project_dir=$1
  mkdir -p ./$project_dir/dist
  rm -rf ./$project_dir/dist/submit.zip
  zip ./$project_dir/dist/submit.zip $project_dir/*.py $project_dir/*.md
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
    build P0
    ;;
  P1)
    build_md P1
    ;;
  P2)
    build_md P2
    ;;
  *) 
    echo "$PROJECT"
    ;;
esac

