#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # --- レポートの戦略に基づいて追加するテストケース ---
        
        # No.1: 境界値 (最小×最大) -> 成功すべき
        def test_boundary_min_max (self):
                self.assertEqual (999, calc(1,999))

        # No.2: 境界値 (最大×最小) -> 現在の実装では失敗する (-1が返るバグ)
        def test_boundary_max_min (self):
                self.assertEqual (999, calc(999,1))

        # No.3: 境界値 (下限外 0) -> 成功すべき (-1が返る)
        def test_boundary_min_out (self):
                self.assertEqual (-1, calc(0,100))

        # No.4: 境界値 (上限外 1000) -> 成功すべき (-1が返る)
        def test_boundary_max_out (self):
                self.assertEqual (-1, calc(1000,100))

        # No.5: 型違反 (片方が文字列) -> 現在の実装では失敗する (クラッシュするバグ)
        def test_type_string (self):
                self.assertEqual (-1, calc(100,"abc"))

        # No.6: 型違反 (小数) -> 現在の実装では失敗する (計算されてしまうバグ)
        def test_type_float (self):
                self.assertEqual (-1, calc(1.5,100))