import requests

def download_csv(url, filename):
    print(f"Downloading data from {url} ...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File saved as {filename}")
    else:
        print(f"Failed to download file: Status code {response.status_code}")

if __name__ == "__main__":
    csv_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    output_file = "owid-covid-data.csv"
    
    download_csv(csv_url, output_file)
