import requests
from bs4 import BeautifulSoup
import csv

def is_valid_wiki_link(link):
    # Function to check if a link is a valid Wikipedia link
    return link.startswith("https://en.wikipedia.org/wiki/")

def scrape_wiki_links(wiki_link, n_cycles):
    # Function to scrape Wikipedia links
    visited_links = set()   # Keep track of visited links to avoid revisiting
    unique_links = []       # Store the unique links found
    links_queue = [(wiki_link, 0)]   # Initialize a queue with the starting Wikipedia link and cycle count

    while links_queue and links_queue[0][1] < n_cycles:
        current_link, current_cycle = links_queue.pop(0)   # Get the current link and cycle count from the front of the queue
        if current_link in visited_links:   # Skip if the current link has been visited
            continue

        visited_links.add(current_link)   # Mark the current link as visited
        response = requests.get(current_link)   # Send an HTTP request to the current link

        if response.status_code == 200:   # If the request is successful
            soup = BeautifulSoup(response.content, "html.parser")   # Parse the HTML content of the page
            for link in soup.find_all("a", href=True):   # Find all anchor tags with href attributes
                if link["href"].startswith("/wiki/") and not link["href"].startswith("/wiki/File:"):
                    # Check if the link is a Wikipedia page link and not a file link
                    wiki_url = f"https://en.wikipedia.org{link['href']}"   # Get the full URL of the Wikipedia link
                    if is_valid_wiki_link(wiki_url) and wiki_url not in visited_links:
                        # Check if the link is valid and not visited before
                        unique_links.append(wiki_url)   # Add the link to the list of unique links
                        links_queue.append((wiki_url, current_cycle + 1))   # Add the link to the queue for the next cycle
            current_cycle += 1   # Increment the cycle count

    return unique_links   # Return the list of unique Wikipedia links

def write_to_csv(filename, links):
    # Function to write the unique links to a CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["S. No.", "Link"])
        for idx, link in enumerate(links, start=1):
            writer.writerow([idx, link])

if __name__ == "__main__":
    wiki_link = input("Enter a Wikipedia link: ")
    n_cycles = int(input("Enter a valid integer between 1 to 3: "))

    if not is_valid_wiki_link(wiki_link) or n_cycles < 1 or n_cycles > 3:
        print("Invalid input. Please provide a valid Wikipedia link and a valid integer between 1 to 3.")
    else:
        print(f"Scraping Wikipedia links for {n_cycles} cycles...")
        unique_links = scrape_wiki_links(wiki_link, n_cycles)

        print("\nFound unique links:")
        for link in unique_links:
            print(link)

        output_filename = "wiki_links.csv"
        write_to_csv(output_filename, unique_links)
        print(f"\nResults written to {output_filename}.")
