import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.srx.com.sg/condo"
csv_name = "{home}/Downloads/srx_sg_condo_directory.csv"


def main():
    response = requests.get(url)

    if response.status_code != 200:
        print("failed to get content from SRX")
        return

    top_condo_searches = extract_top_condo_searches(response.text)

    if top_condo_searches:
        save_csv(top_condo_searches, csv_name)


def extract_top_condo_searches(html):
    soup_html = BeautifulSoup(html, 'html.parser')

    soup_content = soup_html.find(id="top-condo-searches-content")

    result = []

    if not soup_content:
        return result

    soup_items = soup_content.find_all('div', attrs={'class': 'top-condo-search'})

    for soup_item in soup_items:
        soup_project = soup_item.find('a', attrs={'class': 'top-condo-search-project'})
        soup_street = soup_item.find('div', attrs={'class': 'top-condo-search-street'})
        soup_views = soup_item.find('div', attrs={'class': 'top-condo-search-views'})

        result.append([soup_project.string.strip(), soup_project.attrs['href'],
                       soup_street.string.strip(), soup_views.string.strip()])

    return result


def save_csv(items, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for item in items:
            writer.writerow(item)


if __name__ == '__main__':
    main()
