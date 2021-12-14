#!bin/bash
mkdir out
for file in ./tar/*
do
    #echo ${file:0:23}
    dot -Tpng $file -o ./out/${file:15:8}.png
done
