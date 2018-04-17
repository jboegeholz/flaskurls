import unittest


class ModuleImportTest(unittest.TestCase):

    def test_module_import(self):
        import importlib
        mod = importlib.import_module("a.b")
        assert mod.my_member == "Hello B"




