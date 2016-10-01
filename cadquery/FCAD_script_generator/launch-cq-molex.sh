#!/bin/sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
FreeCAD export_conn_molex.py 0271
#FreeCAD export_conn_molex.py all
