'''Tests for ColumnVariable.'''

from column_variable import ColumnVariable
from scisheets.core import helpers_test as ht
from scisheets.core.column import Column
import os
import unittest

FORMULA_COLUMN_NAME = "Formula_Column"


#############################
# Tests
#############################
# pylint: disable=W0212
# pylint: disable=C0111
# pylint: disable=R0904
class TestColumnVariable(unittest.TestCase):

  def setUp(self):
    self.table = ht.createTable("TEST",
        column_name=[ht.COLUMN1, ht.COLUMN2])
    new_column = Column(FORMULA_COLUMN_NAME)
    new_column.setFormula("np.sin(%s)" % ht.COLUMN1)
    self.table.addColumn(new_column)
    self.table.evaluate()
    columns = self.table.getColumns()
    self.column_variables =  \
        [ColumnVariable(c) for c in columns] 
       #[ColumnVariable(c) for c in columns if c.getName() != 'row'] 

  def testConstructor(self):
    for cv in self.column_variables:
      self.assertEqual(cv._baseline_value, cv._column.getCells())

  def testGetColumnValue(self):
    for cv in self.column_variables:
      self.assertEqual(cv.getColumnValue(), cv._column.getCells())

  def testGetNamespaceValue(self):
    namespace = self.table.getNamespace()
    for cv in self.column_variables:
      self.assertEqual(cv.getNamespaceValue(), 
          namespace[cv._column.getName()])

  def testSetColumnValue(self):
    namespace = self.table.getNamespace()
    for cv in self.column_variables:
      num_rows = cv._column.numCells()
      new_value = [10*n for n in range(num_rows)]
      namespace[cv._column.getName()] = new_value
      cv.setColumnValue()
      self.assertEqual(cv.getColumnValue(), new_value)

  def testIsChangedFromBaselineValue(self):
    namespace = self.table.getNamespace()
    for cv in self.column_variables:
      self.assertFalse(cv.isChangedFromBaselineValue())
      num_rows = cv._column.numCells()
      new_value = [10*n for n in range(num_rows)]
      namespace[cv._column.getName()] = new_value
      cv.setIterationStartValue()
      self.assertTrue(cv.isChangedFromBaselineValue())
      cv.setColumnValue()
      cv._baseline_value = cv.getColumnValue()
      self.assertFalse(cv.isChangedFromBaselineValue())

  def testIsChangedFromIterationStartValue(self):
    namespace = self.table.getNamespace()
    for cv in self.column_variables:
      cv.setIterationStartValue()
      self.assertFalse(cv.isChangedFromIterationStartValue())
      num_rows = cv._column.numCells()
      new_value = [10*n for n in range(num_rows)]
      namespace[cv._column.getName()] = new_value
      self.assertTrue(cv.isChangedFromIterationStartValue())
      cv.setIterationStartValue()
      self.assertFalse(cv.isChangedFromIterationStartValue())
      
    

if  __name__ == '__main__':
  unittest.main()
