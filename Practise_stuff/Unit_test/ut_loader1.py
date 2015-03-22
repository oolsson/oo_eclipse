# should be run in python mode, not as unit-test run

import unittest
import ut_finc
import ut_finc2


loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(ut_finc)
suite.addTests(loader.loadTestsFromModule(ut_finc2))
# suite.addTests(loader.loadTestsFromModule(test_something3))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)