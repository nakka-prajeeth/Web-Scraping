import requests
from bs4 import BeautifulSoup


class KatzStaffScraper:
    """
    A class for scraping staff information from the Yeshiva University Katz School of Science and Health website.
    """

    def __init__(self, url):
        """
        Initializes the KatzStaffScraper with the provided URL.

        Parameters:
        - url (str): The URL of the website containing staff information.
        """
        self.url = url

    def fetchData(self):
        """
        Fetches and parses staff information from the specified website.

        Returns:
        - list: A list of dictionaries containing staff information (name, title, and contactInfo).
        """
        try:
            # Sending a GET request to the specified URL
            response = requests.get(self.url)

            # Checking if the request was successful (status code 200)
            if response.status_code == 200:
                # Parsing the HTML content of the page
                soup = BeautifulSoup(response.text, "html.parser")

                data = []  # List to store staff information

                # Extracting staff information
                staff_div = soup.find("div", class_="text-only")
                if staff_div:
                    staff_members = staff_div.find_all("p")
                    for member in staff_members:
                        # Spliting name and title using a comma
                        name_and_title = member.text.strip().split(",")
                        if len(name_and_title) == 2:
                            name, title = name_and_title
                            contact_info = member.find_next("p").text.strip()
                            data.append(
                                {
                                    "name": name.strip(),
                                    "title": title.strip(),
                                    "contactInfo": contact_info,
                                }
                            )

                    return data
                else:
                    print("No staff members found on the page.")
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to fetch or parse data. Error: {e}")
