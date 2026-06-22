# test_zeroblock.py
"""
Tests for ZeroBlock module.
"""

import unittest
from zeroblock import ZeroBlock

class TestZeroBlock(unittest.TestCase):
    """Test cases for ZeroBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroBlock()
        self.assertIsInstance(instance, ZeroBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
