#!/bin/bash
source /opt/intel/inteloneapi/setvars.sh > /dev/null 2>&1
cd ../NPB-CPP/
make sp_gpu CLASS=$class_type
echo "hi"
echo $HOSTNAME
vtune -collect performance-snapshot -collect hotspots ./bin/sp.$class_type
# ./bin/sp.$class_type
echo "DONE"