# Daily Scripture Scraper

A script that scrapes daily scriptures from the JW website (wol.jw.org) for a specified year and saves them as text files.

## Description

The `daily-scripture-scraper` repository contains a Python script, `daily scripture scraper.py`, which scrapes daily scriptures from the JW website for a specified year and saves each day's scripture as a text file. The script uses `aiohttp` for asynchronous HTTP requests and `BeautifulSoup` for parsing HTML content.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/trustosas/daily-scripture-scraper.git
    ```
2. Navigate to the repository directory:
    ```sh
    cd daily-scripture-scraper
    ```
3. Install the required dependencies:
    ```sh
    pip install aiohttp BeautifulSoup4 unidecode
    ```

## Usage

1. Open the `daily scripture scraper.py` file in a text editor.
2. Run the script and enter the desired year when prompted:
    ```sh
    python daily\ scripture\ scraper.py
    ```
3. The script will scrape the daily scriptures for the specified year and save each day's scripture as a text file in the specified directory.

## Example Output
```
Enter year: 2025
Downloaded 365 sites in 123.45 seconds
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- GitHub: [trustosas](https://github.com/trustosas)

Feel free to contribute to this project by submitting issues or pull requests. Enjoy scraping daily scriptures!
