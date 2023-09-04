from Scraper import Scraper
from EmailService import EmailService
from LinkSaver import LinkSaver

import yaml

if __name__ == "__main__":

    with open("./config.yaml", "r") as file:
        config = yaml.safe_load(file)

    search_queries = config['search_queries']
    sender_email = config['sender_email']
    receiver_email = config['receiver_email']
    sender_email_password = config['sender_email_password']
    images_limit = config['images_limit']

    print(search_queries)
    # Scraping Images
    sc = Scraper(num_threads = 5, show_ui = True)
    email_service = EmailService(
        sender = sender_email,
        receiver = receiver_email,
        sender_password = sender_email_password
    )
    link_saver = LinkSaver()

    for query in search_queries:
        scraped_links = sc.scrape(query = query, count = images_limit)
        link_saver.save_to_csv(links = scraped_links, filename = f"{query}.csv")
        email_service.send_email(message = f"Finished Scraping {query} images")
    

