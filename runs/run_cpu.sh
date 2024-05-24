#!/bin/bash
source /opt/intel/inteloneapi/setvars.sh > /dev/null 2>&1
cd ../NPB-CPP/
make sp CLASS=$class_type
echo "hi"
echo $HOSTNAME
if [[ "$is_vtune" -eq "True" ]]; then
  vtune -collect performance-snapshot -collect hotspots ./bin/sp.$class_type
else
  ./bin/sp.$class_type
fi
echo "DONE"