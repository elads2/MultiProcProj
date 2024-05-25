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
if [ $is_vtune -eq 1 ]
then
    echo "use vtune"
    vtune -collect hotspots -collect gpu-offload ./bin/sp.$class_type
else
    ./bin/sp.$class_type
fi
echo "DONE"