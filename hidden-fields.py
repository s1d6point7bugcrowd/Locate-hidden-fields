import requests
from bs4 import BeautifulSoup, Comment

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def extract_comments(soup):
    return soup.find_all(string=lambda text: isinstance(text, Comment))

def extract_hidden_fields(soup):
    return soup.find_all("input", type="hidden")

def print_and_save_results(comments, hidden_fields):
    print("Comments found:")
    for comment in comments:
        print(comment.strip())
    print("\nHidden fields found:")
    for field in hidden_fields:
        print(field)
    
    with open("hidden_content.txt", "w") as output_file:
        output_file.write("Comments found:\n")
        for comment in comments:
            output_file.write(comment.strip() + "\n")
        output_file.write("\nHidden fields found:\n")
        for field in hidden_fields:
            output_file.write(str(field) + "\n")

# Main script
if __name__ == "__main__":
    # Get the user input URL
    url = input("Enter the target URL: ")

    # Fetch the URL
    html_content = fetch_url(url)

    if html_content:
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract comments and hidden fields
        comments = extract_comments(soup)
        hidden_fields = extract_hidden_fields(soup)

        # Print and save the results
        print_and_save_results(comments, hidden_fields)


