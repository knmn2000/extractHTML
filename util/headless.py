from os.path import abspath, dirname, join

from envs import env
from readabilipy import simple_json_from_html_string
from selenium import webdriver

PATH_DIR = dirname(abspath(__file__))
GECKODRIVER_PATH = abspath(join(PATH_DIR, "./../geckodriver.exe"))
# Get firefox.exe path from environment variables
FIREFOX_BINARY = env('firefoxbinary')

class HeadlessBrowser():
    """
    The HeadlessBrowser object initializes a firefox instance.
    
    args:
        url : str -> the URL to be loaded on the instance.
        wait_time : int -> time(in seconds) to wait for the URL to load.
    """
    def __init__(self, url="" , wait_time=30):
        self.url = url
        self.wait_time = wait_time
        options = webdriver.FirefoxOptions()
        # TODO: replace path with environment variable path
        options.binary_location = FIREFOX_BINARY
        self.driver = webdriver.Firefox(executable_path = GECKODRIVER_PATH, options=options)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print traceback if an exception was encountered
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, traceback)
        self.driver.quit()

    def fetchContent(self):
        """Load URL on browser instance and fetch text content.
           Parse text content with readability.

        Returns:
            json: HTML content
        """
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.wait_time)
        text = self.driver.find_element_by_xpath('/html').text
        try:
            readability  = simple_json_from_html_string(text, use_readability=True)
        except:
            # Python based extraction in case Readability.js fails
            readability  = simple_json_from_html_string(text, use_readability=False)
        return readability
