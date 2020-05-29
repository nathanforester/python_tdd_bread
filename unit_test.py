import unittest
from bread_factory import make_dough
from bread_factory import bake_bread
from bread_factory import wholewheat
from bread_factory import wholewheat_sell


class Tests(unittest.TestCase):

    def test(self):
        self.assertTrue(make_dough('water', 'flour') == 'dough')
        self.assertTrue(make_dough('flour', 'water') == 'dough')
        self.assertTrue(make_dough('bread', 'bread') == 'not dough')
        self.assertTrue(make_dough('water', 'water') == 'not dough')
        self.assertTrue(make_dough('bread', 'paraffin') == 'not dough')
        self.assertTrue(make_dough('paraffin', 'water') == 'not dough')
        self.assertTrue(make_dough('paraffin', 'paraffin') == 'not dough')
        self.assertTrue(make_dough('paraffin', 'paraffin') == 'not dough')
        self.assertTrue(make_dough('water', 'flour') == 'dough')
        self.assertTrue(bake_bread('baked') == 'bread baked')
        self.assertTrue(bake_bread('not baked') == 'bread not baked')
        self.assertTrue(wholewheat('water', 'flour') == 'factory downtime more effective and new markets')
        self.assertTrue(wholewheat('flour', 'water') == 'factory downtime more effective and new markets')
        self.assertTrue(wholewheat('water', 'water') == 'factory downtime not more effective and no new markets')
        self.assertTrue(wholewheat('flour', 'flour') == 'factory downtime not more effective and no new markets')
        self.assertTrue(wholewheat('flour', 'paraffin') == 'factory downtime not more effective and no new markets')
        self.assertTrue(wholewheat('paraffin', 'water') == 'factory downtime not more effective and no new markets')
        self.assertTrue(wholewheat('paraffin', 'paraffin') == 'factory downtime not more effective and no new markets')
        self.assertTrue(wholewheat_sell('baked') == 'sell to niche clients')
        self.assertTrue(wholewheat_sell('not baked') == 'cannot sell to niche clients')

        if __name__ == '__main__':
            unittest.main()
