import unittest
import prime_factorization

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(prime_factorization.is_prime(2))
        self.assertTrue(prime_factorization.is_prime(3))
        self.assertTrue(prime_factorization.is_prime(5))
        self.assertTrue(prime_factorization.is_prime(7))
        self.assertTrue(prime_factorization.is_prime(11))
        self.assertTrue(prime_factorization.is_prime(13))
        self.assertTrue(prime_factorization.is_prime(17))
        self.assertTrue(prime_factorization.is_prime(23))
        
    def test_not_prime(self):
        self.assertFalse(prime_factorization.is_prime(-3))
        self.assertFalse(prime_factorization.is_prime(0))
        self.assertFalse(prime_factorization.is_prime(1))
        self.assertFalse(prime_factorization.is_prime(4))
        self.assertFalse(prime_factorization.is_prime(6))
        self.assertFalse(prime_factorization.is_prime(8))
        self.assertFalse(prime_factorization.is_prime(12))
        self.assertFalse(prime_factorization.is_prime(15))
        self.assertFalse(prime_factorization.is_prime(33))
        self.assertFalse(prime_factorization.is_prime(333))


class TestFindPrimeFactors(unittest.TestCase):

    def test_numbers(self):
        self.assertListEqual(prime_factorization.find_prime_factors(-1), [])
        self.assertListEqual(prime_factorization.find_prime_factors(0), [])
        self.assertListEqual(prime_factorization.find_prime_factors(1), [])
        self.assertListEqual(prime_factorization.find_prime_factors(2), [2])
        self.assertListEqual(prime_factorization.find_prime_factors(4), [2, 2])
        self.assertListEqual(prime_factorization.find_prime_factors(10), [2, 5])
        self.assertListEqual(prime_factorization.find_prime_factors(100), [2, 2, 5, 5])

if __name__ == '__main__':
    unittest.main()