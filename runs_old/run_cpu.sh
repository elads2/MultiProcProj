#!/bin/bash
source /opt/intel/inteloneapi/setvars.sh > /dev/null 2>&1
cd ../NPB-CPP/
make sp CLASS=$class_type
./bin/sp.$class_type
