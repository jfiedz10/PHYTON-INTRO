# test_app.py
import unittest
from app import validate_email, calculate_circle_area, sort_list_descending, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        """Przygotowanie środowiska testowego - wspólne dane dla testów."""
        self.valid_email = "test@example.com"
        self.invalid_email = "invalid-email"
        self.radius = 5.0
        self.data_list = [3, 1, 4, 1, 5]
        self.date_str = "2023-10-05"
        self.palindrome_text = "A man a plan a canal Panama"

    def test_validate_email_typical(self):
        """Test typowy: poprawny email."""
        self.assertTrue(validate_email(self.valid_email))

    def test_validate_email_edge_case(self):
        """Przypadek brzegowy: email z kropką i plusem."""
        self.assertTrue(validate_email("user.name+tag@example.co.uk"))

    def test_validate_email_edge_case_long(self):
        """Przypadek brzegowy: bardzo długi email (maksymalna długość)."""
        long_email = "a" * 64 + "@" + "b" * 63 + ".com"  # Bliski limitom RFC
        self.assertTrue(validate_email(long_email))

    def test_validate_email_invalid(self):
        """Błędne dane: nieprawidłowy email."""
        self.assertFalse(validate_email(self.invalid_email))

    def test_validate_email_assert_not_equal(self):
        """Dodatkowy test z assertNotEqual: sprawdź, że nieprawidłowy email nie jest równy True."""
        self.assertNotEqual(validate_email(self.invalid_email), True)

    def test_calculate_circle_area_typical(self):
        """Test typowy: obliczenie pola dla promienia 5."""
        expected = 78.53981633974483  # math.pi * 5**2
        self.assertAlmostEqual(calculate_circle_area(self.radius), expected)

    def test_calculate_circle_area_edge_case(self):
        """Przypadek brzegowy: promień 0 (powinien rzucić wyjątek)."""
        with self.assertRaises(ValueError):
            calculate_circle_area(0)

    def test_calculate_circle_area_edge_case_large(self):
        """Przypadek brzegowy: bardzo duży promień (np. 1e6)."""
        result = calculate_circle_area(1e6)
        self.assertGreater(result, 0)  # Sprawdź, że wynik jest dodatni

    def test_calculate_circle_area_invalid(self):
        """Błędne dane: ujemny promień."""
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)

    def test_sort_list_descending_typical(self):
        """Test typowy: sortowanie listy."""
        result = sort_list_descending(self.data_list)
        self.assertEqual(result, [5, 4, 3, 1, 1])

    def test_sort_list_descending_edge_case(self):
        """Przypadek brzegowy: pusta lista."""
        result = sort_list_descending([])
        self.assertEqual(result, [])

    def test_sort_list_descending_edge_case_duplicates(self):
        """Przypadek brzegowy: lista z duplikatami."""
        result = sort_list_descending([2, 2, 1, 3])
        self.assertEqual(result, [3, 2, 2, 1])

    def test_sort_list_descending_edge_case_floats(self):
        """Przypadek brzegowy: lista z floatami."""
        result = sort_list_descending([3.5, 1.2, 4.0])
        self.assertEqual(result, [4.0, 3.5, 1.2])

    def test_sort_list_descending_invalid(self):
        """Błędne dane: lista z tekstem."""
        with self.assertRaises(TypeError):
            sort_list_descending([1, "a", 3])

    def test_convert_date_format_typical(self):
        """Test typowy: konwersja daty."""
        result = convert_date_format(self.date_str)
        self.assertEqual(result, "05/10/2023")

    def test_convert_date_format_edge_case(self):
        """Przypadek brzegowy: data z dniem 31 grudnia."""
        result = convert_date_format("2023-12-31")
        self.assertEqual(result, "31/12/2023")

    def test_convert_date_format_edge_case_different_format(self):
        """Przypadek brzegowy: konwersja z innego formatu (np. MM/DD/YYYY do DD/MM/YYYY)."""
        result = convert_date_format("10/05/2023", from_format="%m/%d/%Y", to_format="%d/%m/%Y")
        self.assertEqual(result, "05/10/2023")

    def test_convert_date_format_invalid(self):
        """Błędne dane: nieprawidłowa data."""
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")

    def test_is_palindrome_typical(self):
        """Test typowy: tekst jest palindromem."""
        self.assertTrue(is_palindrome(self.palindrome_text))

    def test_is_palindrome_edge_case(self):
        """Przypadek brzegowy: pusty tekst (traktowany jako palindrom)."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_edge_case_numbers(self):
        """Przypadek brzegowy: tekst z liczbami (np. '12321')."""
        self.assertTrue(is_palindrome("12321"))

    def test_is_palindrome_edge_case_accents(self):
        """Przypadek brzegowy: tekst z akcentami (ignoruje akcenty, ale sprawdź bez nich)."""
        self.assertTrue(is_palindrome("radar"))  # Prosty przykład bez akcentów

    def test_is_palindrome_invalid(self):
        """Błędne dane: tekst nie będący palindromem."""
        self.assertFalse(is_palindrome("hello world"))

    def test_is_palindrome_assert_not_equal(self):
            """Dodatkowy test z assertNotEqual: sprawdź, że nie-palindrom nie jest równy True."""
            self.assertNotEqual(is_palindrome("not a palindrome"), True)

        # Testy parametryzowane (rozszerzone dla validate_email i nowe dla is_palindrome)
        def test_validate_email_parametrized(self):
            """Testy parametryzowane dla validate_email."""
            test_cases = [
                ("test@example.com", True),
                ("invalid", False),
                ("user@domain.co", True),
                ("a@b.c", True),  # Krótki email
                ("very.long.email.address@subdomain.example.org", True),  # Długi email
            ]
            for email, expected in test_cases:
                with self.subTest(email=email):
                    self.assertEqual(validate_email(email), expected)

        def test_is_palindrome_parametrized(self):
            """Testy parametryzowane dla is_palindrome."""
            test_cases = [
                ("radar", True),
                ("hello", False),
                ("A man a plan a canal Panama", True),
                ("12321", True),
                ("not palindrome", False),
            ]
            for text, expected in test_cases:
                with self.subTest(text=text):
                    self.assertEqual(is_palindrome(text), expected)

    if __name__ == '__main__':
        unittest.main()
