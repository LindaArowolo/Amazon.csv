import csv
import matplotlib.pyplot as plt


def read_data(file_path):
    # Reads data from the spreadsheet
    data = []
    with open(file_path, 'r') as amazon_csv:
        spreadsheet = csv.DictReader(amazon_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def collect_usernames_for_product(data, product_id):
    # Collects names of users who wrote reviews for the given product ID
    usernames = []
    for row in data:
        if row['product_id'] == product_id:
            usernames.append(row['user_name'])  # Ensure the correct column name is used
    return usernames


def visualize_usernames(usernames):
    # Visualize the count of reviews per user
    user_counts = {}
    for username in usernames:
        if username in user_counts:
            user_counts[username] += 1
        else:
            user_counts[username] = 1

    # Sort the users by count for better visualization
    sorted_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)
    users, counts = zip(*sorted_users)

    # Plot the data
    plt.figure(figsize=(9, 5))
    plt.bar(users, counts)
    plt.xlabel('Usernames')
    plt.ylabel('Number of Reviews')
    plt.title(f'Number of Reviews by User for Product ID: {product_id}')
    plt.xticks(rotation=90)  # Rotate usernames for better readability
    plt.show()


if __name__ == "__main__":
    # Read data from the CSV file
    file_path = 'amazon.csv'
    data = read_data(file_path)

    # Collect all usernames who wrote reviews for the product with the unique ID B07JW9H4J1
    product_id = 'B07JW9H4J1'
    user_names = collect_usernames_for_product(data, product_id)

    # Print the collected usernames
    print(user_names)

    # Visualize the usernames
    visualize_usernames(user_names)


