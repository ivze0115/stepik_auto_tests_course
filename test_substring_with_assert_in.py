def test_substring(full_string , substring):
        assert substring in  full_string, f"expected '{substring}' to be substring of '{full_string}'"

if __name__ == '__main__':
    test_substring('some_text', 'some')
    test_substring('fulltext', 'some_value')
