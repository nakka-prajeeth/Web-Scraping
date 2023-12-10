import requests


class SitemapParser:
    """
    SitemapParser class for fetching and parsing sitemaps from the robots.txt file of a website.

    Attributes:
        baseUrl (str): The base URL of the website.
        sitemapUrls (list): A list to store sitemap URLs extracted from robots.txt.

    Methods:
        fetchRobotsTxt() -> str or None:
            Fetches the content of the robots.txt file for the website.

        parseSitemapUrls(robotsTxtContent: str) -> None:
            Parses the robots.txt content to extract sitemap URLs.

        fetchAndParseSitemaps() -> None:
            Fetches and parses each sitemap URL in the sitemapUrls list.
            Assumes each sitemap contains URLs and displays the results.

    """

    def __init__(self, baseUrl: str):
        """
        Initializes a SitemapParser instance with a base URL.

        Args:
            baseUrl (str): The base URL of the website.
        """
        # Initializing the SitemapParser with a base URL and an empty list for sitemap URLs
        self.baseUrl = baseUrl
        self.sitemapUrls = []

    def fetchRobotsTxt(self) -> str or None:
        """
        Fetches the content of the robots.txt file for the website.

        Returns:
            str or None: The content of the robots.txt file if successful, None if there is an error.
        """
        try:
            # Fetching the robots.txt file for the base URL
            response = requests.get(f"{self.baseUrl}/robots.txt")
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error fetching robots.txt: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching robots.txt: {e}")
            return None

    def parseSitemapUrls(self, robotsTxtContent: str) -> None:
        """
        Parses the robots.txt content to extract sitemap URLs.

        Args:
            robotsTxtContent (str): The content of the robots.txt file.
        """
        try:
            # Parsing the robots.txt content to extract sitemap URLs
            lines = robotsTxtContent.split("\n")
            sitemaps = [
                line.split(": ")[-1] for line in lines if line.startswith("Sitemap:")
            ]
            self.sitemapUrls = sitemaps
        except Exception as e:
            print(f"Error parsing sitemap URLs: {e}")

    def fetchAndParseSitemaps(self) -> None:
        """
        Fetches and parses each sitemap URL in the sitemapUrls list.
        Assumes each sitemap contains URLs and displays the results.
        """
        for sitemapUrl in self.sitemapUrls:
            try:
                # Fetching each sitemap URL
                response = requests.get(sitemapUrl)
                if response.status_code == 200:
                    # Parsing the sitemap content using an XML parser
                    soup = BeautifulSoup(response.text, "xml")

                    # Assuming the sitemap contains URLs, create a DataFrame
                    urls = [url.text for url in soup.find_all("url")]
                    df = pd.DataFrame(urls, columns=["url"])

                    # Displaying the sitemap URL and the first few rows of the DataFrame
                    print(f"Sitemap: {sitemapUrl}")
                    print(df.head())
                else:
                    print(
                        f"Error fetching sitemap data ({sitemapUrl}): {response.status_code}"
                    )
            except Exception as e:
                print(f"Error parsing sitemap ({sitemapUrl}): {e}")
