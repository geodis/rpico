#!/bin/bash
echo "+-------------------+"
echo "| -- rpico - rshell |"
echo "+-------------------+"
echo

FILE=$1
FILE_NAME=$(echo $FILE | cut -d '.' -f1) # without extension

echo "-- rpico - rshell: Building ..."
docker build -t rshell \
    --build-arg USER_ID=$(id -u) \
    --build-arg USERNAME=$(whoami) \
    -f Dockerfile . 2>1 > /dev/null

RPI_PORT=$(ls /dev/ttyACM* |head -n1)
echo $RPI_PORT
if [ "$RPI_PORT" !=  "" ]
then
  echo "-- rpico - rshell: Running ..."
  docker run -ti \
      --name rshell \
      --ulimit memlock=-1 \
      --rm \
      -v $(pwd)/:/data \
      -w /data/ \
      --privileged -v $RPI_PORT:$RPI_PORT \
      rshell \
      rshell cp /data/$FILE /pyboard/ && \
      timeout 1 rshell  repl \~ import $FILE_NAME \~ ${FILE_NAME}\.start\(\) \~
fi