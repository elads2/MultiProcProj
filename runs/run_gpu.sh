#!/bin/bash
source /opt/intel/inteloneapi/setvars.sh > /dev/null 2>&1
echo "hi"
echo $HOSTNAME
cd ../NPB-CPP/
if [ $is_make -eq 1 ]
then
    echo "make"
    make sp_gpu CLASS=$class_type
fi
./bin/sp.$class_type
echo "DONE"