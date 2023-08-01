# Wikipedia Link Scraper

The "Wikipedia Link Scraper" is a Python script that allows users to extract and analyze Wikipedia page links in a given number of cycles. This script utilizes web scraping techniques to retrieve the first 10 unique Wikipedia page links embedded within the provided Wikipedia link.

## Getting Started

These instructions will guide you on how to use the "Wikipedia Link Scraper" script and explore Wikipedia page links.

### Prerequisites

To run the script, you need to have the following installed:

- Python 3.x
- requests library
- BeautifulSoup library

You can install the required libraries using the following command:

```
pip install requests beautifulsoup4
```

### Usage

1. Clone the repository or download the `wikipedia_link_scraper.py` file to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the `wikipedia_link_scraper.py` file.

3. Run the script using the following command:

```
python wikipedia_link_scraper.py
```

4. You will be prompted to enter a valid Wikipedia link. Please ensure that the link starts with "https://en.wikipedia.org/wiki/" for successful scraping.

5. Next, input a valid integer between 1 and 3 to specify the number of cycles for link extraction.

6. The script will perform the link scraping process and display the first 10 unique Wikipedia page links found in the specified number of cycles.

7. The script will offer to write the results to a CSV file named `wiki_links.csv`, which includes all unique links along with their counts.

