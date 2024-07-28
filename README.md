# Amazon Reviews Analysis

This project provides a Python script to read Amazon product reviews from a CSV file, collect usernames for a specific product ID, and visualize the data using Matplotlib.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Visualization](#visualization)
- [Testing](#testing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/amazon-reviews-analysis.git
    cd amazon-reviews-analysis
    ```

2. Install the required Python packages:
    ```bash
    pip install matplotlib pandas pytest
    ```

## Usage

1. Ensure you have the `amazon.csv` file in the same directory as the script. The CSV file should contain the following columns:
    - `product_id`
    - `username`
    - Other relevant columns

2. Run the script to read data from the CSV file, collect usernames, and visualize the data:
    ```bash
    python collect_usernames.py
    ```

### Script Details

- `read_data(file_path)`: Reads data from the CSV file.
- `collect_usernames_for_product(data, product_id)`: Collects usernames for the specified product ID.
- `visualize_usernames(usernames, product_id)`: Visualizes the count of reviews per user for the specified product ID.
