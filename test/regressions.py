import unittest
from StringIO import StringIO

from docutils.readers import standalone
from docutils.core import Publisher, default_description, \
    default_usage

from types import ModuleType
rst2odp = ModuleType('rst2odp')
exec open('../bin/rst2odp') in rst2odp.__dict__

from odplib import preso, zipwrap

class TestRegressions(unittest.TestCase):

    def _to_odp_content(self, rst, xml_filename):
        reader = standalone.Reader()
        reader_name = 'standalone'
        writer = rst2odp.Writer()
        writer_name = 'pseudoxml'
        parser = None
        parser_name = 'restructuredtext'
        settings = None
        settings_spec = None
        settings_overrides = None
        config_section = None
        enable_exit_status = 1
        usage = default_usage
        publisher = Publisher(reader, parser, writer,# source=StringIO(rst),
                              settings=settings,
                              destination_class=rst2odp.BinaryFileOutput)
        publisher.set_components(reader_name, parser_name, writer_name)
        description = ('Generates OpenDocument/OpenOffice/ODF slides from '
                       'standalone reStructuredText sources.  ' + default_description)

        fin = open('/tmp/in.rst', 'w')
        fin.write(rst)
        fin.close()
        argv = ['--traceback', '/tmp/in.rst', '/tmp/out']
        output = publisher.publish(argv, usage, description, settings_spec, settings_overrides, config_section=config_section, enable_exit_status=enable_exit_status)
        # pull content.xml out of /tmp/out
        z = zipwrap.ZipWrap('/tmp/out')
        fout = open(xml_filename, 'w')
        content = preso.pretty_xml(z.cat('content.xml'))
        fout.write(content)
        fout.close()
        return content

    def check_output(self, rst, desired, filename='/tmp/foo.xml'):
        content = self._to_odp_content(rst, filename)
        self.assert_(_contains_lines(content, desired), "%s should have %s" %(content, desired))
        
    def test_basic(self):
        rst = """
Title
-----

hello world
"""
        desired = """<text:p text:style-name="P1">
              hello world
            </text:p>"""
        self.check_output(rst, desired)

    def test_2_paragraphs(self):
        rst = """
2 para
-------

Hello

World
"""
        desired = """<text:p text:style-name="P1">
              Hello
            </text:p>
            <text:p text:style-name="P1">
              World
            </text:p>"""
        self.check_output(rst, desired, '/tmp/2para.xml')

    def t2est_mono_block(self):
        rst = """
From script
------------

Make file ``hello.py`` with ::

  print "hello world"

Run with::

  python hello.py
"""
        desired='bad'
        self.check_output(rst, desired, '/tmp/monoblock.xml')

    def tes2t_code_block(self):
        rst = """
``id``
--------

.. code-block:: pycon

  >>> a = 4
  >>> id(a)
"""
        desired='bad'
        self.check_output(rst, desired, '/tmp/code.xml')

    def te2st_code_block_with_space(self):
        rst = """
``id``
--------

.. code-block:: pycon

  >>> a = 4

  >>> id(a)
"""
        desired='bad'
        self.check_output(rst, desired, '/tmp/code.xml')

    def test_normal_sized_styled_before_code(self):
        rst ="""
txt before code
----------------

.. class:: normal

  foo

.. class:: normal

  .. code-block:: python

    a = 3
"""
        desired='bad'
        self.check_output(rst, desired, '/tmp/code.xml')

    def te2st_styled_before_code(self):
        rst ="""
txt before code
----------------

.. class:: large

  foo

.. class:: large

  .. code-block:: python

    a = 3
"""
        desired='''<text:p text:style-name="P1">
              foo
            </text:p>
            <text:p text:style-name="P1">
              <text:span text:style-name="T0">
                a
                <text:s/>
              </text:span>
              <text:span text:style-name="T1">
                =
              </text:span>
              <text:span text:style-name="T0">
                <text:s/>
              </text:span>
              <text:span text:style-name="T1">
                3
              </text:span>
              <text:span text:style-name="T0">
                <text:line-break/>
              </text:span>
            </text:p>
'''
        self.check_output(rst, desired, '/tmp/code2.xml')

def _contains_lines(haystack, needle, ignore_whitespace=True):
    """
    >>> _contains_lines(range(4), range(1,2))
    True
    >>> _contains_lines(range(4), range(1,5))
    False
    """
    if ignore_whitespace:
        haystack = [str(x).strip() for x in haystack]
        needle = [str(x).strip() for x in needle]
    for i, line in enumerate(haystack):
        if needle[0] == line and haystack[i:i+len(needle)] == needle:
            return True
    return False

if __name__ == '__main__':
    unittest.main()
    # import doctest
    # doctest.testmod()
