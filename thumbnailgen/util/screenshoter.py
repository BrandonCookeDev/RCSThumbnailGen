from os.path import isabs, abspath, exists
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver as webdriver
import contextlib

@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()


def get_web_driver():
    return webdriver.Chrome(ChromeDriverManager().install())


def screenshot_webpage(url: str, dest: str):
    with quitting(get_web_driver()) as driver:
        driver.implicitly_wait(10)
        driver.get(url)
        driver.get_screenshot_as_file(dest)


def screenshot_file(filepath: str, dest: str):
    with quitting(get_web_driver()) as driver:
        filepath = filepath if isabs(filepath) else abspath(filepath)
        dest = dest if isabs(dest) else abspath(dest)

        print('writing screenshot of {} to file: {}'.format(filepath, dest))

        driver.implicitly_wait(10)
        driver.set_window_size(width=1920, height=1080)
        driver.get('file://' + filepath)
        driver.get_screenshot_as_file(dest)
        driver.quit()
