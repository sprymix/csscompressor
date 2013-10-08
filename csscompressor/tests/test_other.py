##
# Copyright (c) 2013 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from .base import BaseTest


class Tests(BaseTest):
    def test_issue_108(self):
        # https://github.com/yui/yuicompressor/issues/108

        input = '''
            table thead tr td {
                color: #CEDB00;
                padding: 0.5em 0 1.0em 0;
                text-transform: uppercase;
                vertical-align: bottom;
            }
        '''

        output = '''table thead tr td{color:#cedb00;padding:.5em 0 1.0em 0;text-transform:uppercase;vertical-align:bottom}'''

        self._test(input, output)

    def test_issue_59(self):
        # https://github.com/yui/yuicompressor/issues/59

        input = '''
            .issue-59 {
                width:100%;
                width: -webkit-calc(100% + 30px);
                width: -moz-calc(100% + 30px);
                width: calc(100% + 30px);
            }
        '''

        output = '''.issue-59{width:100%;width:-webkit-calc(100% + 30px);width:-moz-calc(100% + 30px);width:calc(100% + 30px)}'''

        self._test(input, output)
