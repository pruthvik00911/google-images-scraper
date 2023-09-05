# Google Images Scraper

Google Images Scraper is a Python tool designed to scrape high-resolution images from Google Images based on provided links. It now supports multi-threading for faster scraping. This tool overcomes the limitations of some browser extensions that only download image thumbnails.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/google-images-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd google-images-scraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper by executing the following command:

   ```bash
   python main.py
   ```

   This script will fetch high-resolution images from Google Images based on the provided links using multi-threading for faster scraping.

## Configuration

You can customize the behavior of the scraper by modifying the `config.yaml` file.

### Email Configuration

- `sender_email`: The email address used for sending notifications.
- `receiver_email`: The email address to receive notifications.
- `sender_email_password`: The password for the sender's email account.

**Note**: If you want to use the email notifications functionality with a Gmail account, it's recommended to generate an [App Password](https://support.google.com/mail/answer/185833?hl=en) instead of using your account password.

  


### Search Queries

- `search_queries`: List of search queries to use when scraping Google Images. You can add or remove queries as needed.

### Images Limit

- `images_limit`: Set the maximum number of images to download per category.

### Project Structure

- `csv_downloads`: Directory to store CSV files.
- `image_downloads`: Directory to store downloaded images.
- `downloader.py`: Contains functions to download images using multi-threading.
- `EmailService.py`: Provides functionality for email notifications (if needed).
- `Scrapper.py`: The main script to initiate the scraping process with multi-threading.
- `config.yaml`: Configuration file to set up email and scraping parameters.
- `LinkSaver.py`: Handles saving image links.
- `main.py`: The main entry point for running the Google Images Scraper.

Certainly, here's an additional section in your README.md with information about using `main.py` and customizing the Scraper class:

## Getting Started with `main.py`

In `main.py`, an instance of the `Scraper` class is created as follows:

```python
sc = Scraper(num_threads=5, show_ui=True)
```

- `num_threads`: You can customize the number of threads, which represents the total browser instances. More threads generally result in faster scraping, but it may increase resource usage. Adjust this value based on your system's capabilities and requirements.

- `show_ui`: The `show_ui` option determines whether Selenium runs in headless mode or not. When set to `True`, it shows the browser UI during scraping. When set to `False`, it runs Selenium in headless mode, which means the browser operates in the background without a visible UI. Choose the appropriate setting based on your preference and needs.

The rest of the process is straightforward:

5. Run the scraper by executing `main.py`:

   ```bash
   python main.py
   ```

6. The scraper will start fetching high-resolution images from Google Images based on the provided links and configurations, using the specified number of threads and UI visibility.

7. Monitor the scraping progress and any notifications sent via email, as configured in `config.yaml`.

Customize the `num_threads` and `show_ui` options in the `Scraper` class instance to tailor the scraping process to your specific requirements.


## Contributing

Contributions to Google Images Scraper are welcome and encouraged! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes with descriptive commit messages.
5. Push your changes to your fork.
6. Open a pull request, explaining the changes you've made.

## License

This project is licensed under the [MIT License](LICENSE).
