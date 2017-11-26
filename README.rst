.. image:: https://travis-ci.org/sprymix/csscompressor.svg?branch=master
    :target: https://travis-ci.org/sprymix/csscompressor


Almost exact port of YUI CSS Compressor.
Passes all original unittests.


Usage
=====

.. code:: pycon

    >>> from csscompressor import compress
    >>> compress('''
    ...    your css {
    ...        content: "!";
    ...    }
    ... ''')
    'your css{content:"!"}'

Or, if you want to use it from command line:

.. code::

    $ python3 -m csscompressor --help


Compatibility
=============

Tested under Python 2.7 and 3.3+


Installation
============

Use ``pip`` or ``easy_install``:

.. code::

    $ pip install csscompressor


Development
===========

Use py.test to run unittests


License
=======

Published under the original Yahoo License for YUI Compressor -- BSD.
