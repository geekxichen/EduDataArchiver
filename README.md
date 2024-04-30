# EduDataArchiver

## Project Overview
EduDataArchiver is an innovative Python-based web scraping tool designed to streamline the process of collecting comprehensive data from publicly available sources. This robust code is capable of delving into specified websites, such as schools.service.gov.uk, extracting key details such as the names and unique identifiers of Harris Federation academics. It's engineered to assist researchers and data analysts in compiling educational data accurately and efficiently, while strictly adhering to the terms of service and data use policies of the sources.

## Project Structure
EduDataArchiver consists of the following key files:
- `edu_data_archiver.py`: The main Python script that performs the web scraping. It contains all the logic for processing the data and saving it to a file.
- `extracted_data.txt`: This text file is the default output where the scraped data is stored. It includes the names and unique identifiers of academics from the Harris Federation as extracted from the website.
Ensure that you have both of these files in the project directory before running the scraper.


## Features
- Automated scraping of academic data from designated web pages.
- Extraction of key details such as academic names and unique identifiers.
- Capability to handle different website structures and layouts.
- Output data in a structured and analysis-ready format.
- User-friendly command-line interface for easy operation.

## Prerequisites
To run EduDataArchiver, you'll need:
- Python 3.x installed on your system.
- The `requests` library for making HTTP requests.
- The `beautifulsoup4` library for parsing HTML content.

Install the required libraries using pip:
```bash
pip install requests
pip install beautifulsoup4
```

## Installation
1. Clone the EduDataArchiver repository to your local machine.
```bash
git clone https://github.com/geekxichen/EduDataArchiver.git
```
2. Navigate to the cloned directory.
```bash
cd EduDataArchiver
```

## Usage
Run the scraper using the following command:
```bash
python edu_data_archiver.py
```
Follow the prompts to enter the target website and start the scraping process.

## How It Works
EduDataArchiver sends HTTP requests to the target URL and retrieves the HTML content. It then uses BeautifulSoup to parse the HTML and extract the required academic data. The data is saved in a CSV file, making it ready for further analysis.

## Customization
You can customize the scraper by editing the `edu_data_archiver.py` file to specify the target elements, attributes, and the output format.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
- BeautifulSoup and Requests libraries for providing the backbone of our scraping capabilities.
- The Python community for continuous support and inspiration.

## Disclaimer
EduDataArchiver is intended for educational and research purposes only. The tool is designed to collect data from publicly available government websites, ensuring access to authoritative and reliable data. Users are responsible for complying with the terms of service of the websites they scrape and for obtaining any necessary permissions for data collection.
