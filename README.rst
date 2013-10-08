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


Compatibility
=============

Tested under Python 2.6, 2.7 and 3.3


Development
===========

Use py.test to run unittests


License
=======

Published under the original Yahoo License for YUI Compressor -- BSD.
