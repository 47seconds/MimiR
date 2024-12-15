from urllib.parse import urlparse
from src.grabber.sources import readingpia_me, zetrotranslation_com

domain_map = {
    "www.readingpia.me": readingpia_me,
    "zetrotranslation.com": zetrotranslation_com,
}

def get_source(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # print(domain)
    if domain in domain_map:
        return domain_map[domain]