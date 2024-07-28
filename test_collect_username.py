import pytest
from collect_username import read_data, collect_usernames_for_product

# Define the path to the CSV file
file_path = 'amazon.csv'

def test_read_data():
    # Call the read_data function
    data = read_data(file_path)

    # Perform basic checks
    assert len(data) > 0  # Check that data is not empty
    assert 'product_id' in data[0]  # Check that 'product_id' is a key in the dictionary
    assert 'user_name' in data[0]  # Check that 'username' is a key in the dictionary

def test_collect_usernames_for_product():
    # Read data from the CSV file
    data = read_data(file_path)
    # Define the product ID to test
    product_id = 'B07JW9H4J1'
    # Call the collect_usernames_for_product function
    usernames = collect_usernames_for_product(data, product_id)

    # Perform basic checks
    assert len(usernames) > 0  # Check that the usernames list is not empty
    assert isinstance(usernames[0], str)  # Check that the first element in the usernames list is a string
if __name__ == "__main__":
    pytest.main()
