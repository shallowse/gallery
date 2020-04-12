#!/bin/bash

for file in $(ls img)
do
    echo "Converting ${file}"
    convert -resize 30% img/${file} thumb-img/${file}
done
