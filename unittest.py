import unittest


class MyTestCase(unittest.TestCase):
  def test_split(self):
      s = 'Hello  world'
      self.assertEqual(s.split(), ['Hello', 'world'])


if __name__ == '__main__':
    unittest.main()
