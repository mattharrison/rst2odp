#!/bin/sh

ODP=~/work/pylibs/rst2odp/
PATH=$PATH:${ODP}bin
echo $PATH
#PYTHONPATH=${ODP} rst2odp.py --traceback -r 3 --mono-font "Commodore 64" --template-file templates/whitekids.otp week1.rst week1.odp
PYTHONPATH=${ODP} rst2odp.py --traceback -r 3 --mono-font "Envy Code R" $@
