def reverse_string(text: str) -> str:
    """Return the reverse of the given string."""
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


def count_vowels(text: str) -> int:
    """Return the number of uppercase and lowercase vowels in the string."""
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    # Question 1: Reverse a String
    print("Question 1: Reverse a String")
    print(reverse_string("hello"))   # Expected: olleh
    print(reverse_string("Python"))  # Expected: nohtyP
    print(reverse_string(""))        # Expected: ""

    # Question 2: Count Vowels
    print("\nQuestion 2: Count Vowels")
    print(count_vowels("Hello World"))  # Expected: 3
    print(count_vowels("PYTHON"))       # Expected: 1
    print(count_vowels("AEIOU"))        # Expected: 5
    print(count_vowels(""))             # Expected: 0
