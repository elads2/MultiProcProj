#!/bin/bash
/bin/echo "##" $(whoami) is checking specifications of a standard CPU Intel DevCloud node
echo "########################################### getconf -a"
getconf -a | grep CACHE
exit