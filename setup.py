#! python
# $Id: setup.py 110 2005-07-22 10:24:48Z xiphux $
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'optimize': 2}},
    windows = [{'script': "soulforge.py"}],
)
