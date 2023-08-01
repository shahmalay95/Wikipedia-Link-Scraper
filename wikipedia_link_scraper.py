import requests
from bs4 import BeautifulSoup
import csv

def is_valid_wiki_link(link):
    return link.startswith("https://en.wikipedia.org/wiki/")

def scrape_wiki_links(wiki_link, n_cycles):
    visited_links = set()
    unique_links = []
    links_queue = [(wiki_link, 0)]

    while links_queue and links_queue[0][1] < n_cycles:
        current_link, current_cycle = links_queue.pop(0)
        if current_link in visited_links:
            continue

        visited_links.add(current_link)
        response = requests.get(current_link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for link in soup.find_all("a", href=True):
                if link["href"].startswith("/wiki/") and not link["href"].startswith("/wiki/File:"):
                    wiki_url = f"https://en.wikipedia.org{link['href']}"
                    if is_valid_wiki_link(wiki_url) and wiki_url not in visited_links:
                        unique_links.append(wiki_url)
                        links_queue.append((wiki_url, current_cycle + 1))
            current_cycle += 1

    return unique_links

def write_to_csv(filename, links):
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

