import unittest
from culc import Culc

class CalculatorTestCase(unittest.TestCase):
    #SUM
    def test_culc_sum_normal(self):
        self.assertEqual(Culc().sum(1, 2), 3)

    def test_culc_sum_float_num(self):
        self.assertNotEqual(Culc().sum(0.1, 0.2), 0.3)

    def test_culc_sum_float_str(self):
        self.assertEqual(Culc().sum('0.1', '0.2'), 0.3)

    def test_culc_sum_exp(self):
        self.assertEqual(Culc().sum(1e3, 2e3), 3000)

    def test_culc_sum_exp_and_normal(self):
        self.assertEqual(Culc().sum(123e2, 1000), 13300)

    def test_culc_sum_eq_zero(self):
        self.assertEqual(Culc().sum(0.1, -0.1), 0)

    def test_culc_sum_string(self):
        self.assertEqual(Culc().sum("lol", 2), "No, don't use strings")

    #DIF
    def test_culc_dif_normal(self):
        self.assertEqual(Culc().dif(4, 2), 2)

    def test_culc_dif_float_num(self):
        self.assertNotEqual(Culc().dif(.3, .1), .2)

    def test_culc_dif_float_str(self):
        self.assertEqual(Culc().dif('.3', '.1'), .2)

    def test_cucl_dif_exp(self):
        self.assertEqual(Culc().dif(1e3, 1e2), 900)

    def test_culc_dif_exp_and_normal(self):
        self.assertEqual(Culc().dif(1e3, 100), 900)

    def test_culc_dif_near_zero(self):
        self.assertNotEqual(Culc().dif(0.0000000000001, 0.000000000001), 0)

    def test_culc_dif_zero(self):
        self.assertEqual(Culc().dif(0.00000001, 0.00000001), 0)

    def test_culc_dif_string(self):
        self.assertEqual(Culc().dif("lolo", 1), "No, don't use strings")

    #MUL
    def test_culc_mul_normal(self):
        self.assertEqual(Culc().mul(4, 2), 8)

    def test_culc_mul_float_num(self):
        self.assertEqual(Culc().mul(49.0, .1), 4.9)

    def test_culc_mul_float_str(self):
        self.assertEqual(Culc().mul('.3', '.1'), .03)

    def test_cucl_mul_exp(self):
        self.assertEqual(Culc().mul(1e3, 1e2), 100000)

    def test_culc_mul_exp_and_normal(self):
        self.assertEqual(Culc().mul(1e3, 100), 100000)

    def test_culc_mul_near_zero(self):
        self.assertNotEqual(Culc().mul(0.0000000000001, 0.000000000001), 0)

    def test_culc_mul_zero(self):
        self.assertEqual(Culc().mul(0.00000001, 0.00000001), 1.0000000000000001e-16)

    def test_culc_mul_string(self):
        self.assertEqual(Culc().mul(1, "lolo"), "No, don't use strings")


    #DIV
    def test_culc_div_normal(self):
        self.assertEqual(Culc().div(4, 2), 2)

    def test_culc_div_float_num(self):
        self.assertEqual(Culc().div(49.0, .1), 490)

    def test_culc_div_float_str(self):
        self.assertEqual(Culc().div('.3', '.1'), 3)

    def test_cucl_div_exp(self):
        self.assertEqual(Culc().div(1e3, 1e2), 10)

    def test_culc_div_exp_and_normal(self):
        self.assertEqual(Culc().div(1e3, 100), 10)

    def test_culc_div_near_zero(self):
        self.assertEqual(Culc().div(0.000000000001, 0.000000000001), 1)

    def test_culc_div_string(self):
        self.assertEqual(Culc().div("lolo", 1), "No, don't use strings")

    def test_culc_div_by_zero(self):
        self.assertEqual(Culc().div(123, 0), "/0, really?")

    #POW
    def test_culc_pow_normal(self):
        self.assertEqual(Culc().pow(4, 2), 16)

    def test_culc_pow_float_num(self):
        self.assertEqual(Culc().pow(49.0, 1./2.), 7)

    def test_culc_pow_float_str(self):
        self.assertEqual(Culc().pow(2, 0), 1)

    def test_cucl_pow_exp(self):
        self.assertEqual(Culc().pow(1e3, 2e0), 1000000)

    def test_culc_pow_exp_and_normal(self):
        self.assertEqual(Culc().pow(1e3, 3), 1000000000)

    def test_culc_pow_string(self):
        self.assertEqual(Culc().pow("lolo", 1), "No, don't use strings")

if __name__ == '__main__':
    unittest.main()
