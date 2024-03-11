"""
py2exe allow python scripts run in windows that does not have python installed.

run the command to build the app/script:
    python 10_py2exe.py py2exe
"""
from distutils.core import setup

from py2exe import freeze


freeze(
        console=[{'script' : '10_demo_py2exe.py'}],
        options = {
            'py2exe': {'bundle_files' : 1, 'compressed' : True}
            },
        zipfile = None
        )
