import unittest

from jinja2 import Template

from simplecover.llm.generic import load_template


class llm_generic(unittest.TestCase):

    def test_load_template(self):
        template = load_template("./simplecover/coverletter.pmpt.j2")
        self.assertEqual(type(template), Template)
