#!/usr/bin/env python

# $Id: setup.py,v 1.1 2002/06/21 18:10:49 jgoerzen Exp $

# IMAP synchronization
# Module: installer
# COPYRIGHT #
# Copyright (C) 2002 - 2018 John Goerzen & contributors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

from setuptools import setup, Command


class TestCommand(Command):
    """runs the OLI testsuite"""
    description = """Runs the test suite. In order to execute only a single
        test, you could also issue e.g. 'python -m unittest
        test.tests.test_01_basic.TestBasicFunctions.test_01_olistartup' on the
        command line."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test.OLItest import TextTestRunner, TestLoader, OLITestLib
        import logging
        import os.path
        import sys
        logging.basicConfig(format='%(message)s')
        here = os.path.dirname(os.path.abspath(__file__))
        # set credentials and OfflineImap command to be executed:
        OLITestLib(cred_file=here + '/test/credentials.conf',
                   cmd=[sys.executable, '%s/offlineimap.py' % here])
        suite = TestLoader().discover('./test/tests')
        # TODO: failfast does not seem to exist in python2.6?
        TextTestRunner(verbosity=2).run(suite)


setup(name="offlineimap",
      version='7.3.3+py3',
      description='',
      long_description='',
      author='',
      author_email='',
      url='',
      packages=['offlineimap', 'offlineimap.folder',
                  'offlineimap.repository', 'offlineimap.ui',
                  'offlineimap.utils'],
      # scripts=['bin/offlineimap'],
      install_requires=[
          'setuptools',
          'six',
          'rfc6555'
      ],
      license='',
      cmdclass={'test': TestCommand},
)

