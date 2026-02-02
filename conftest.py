import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
import os
import pytest
driver = None




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('setup', 'call'):
        xfail = hasattr(report, 'wasxfail')

        if (report.failed and not xfail) or (report.skipped and xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir,
                report.nodeid.replace("::", "_") + ".png"
            )
            print("file name is " + file_name)

            _capture_screenshot(file_name)

            if file_name:
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extra = extra







@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browesr_name = request.config.getoption("browser_name")
    if browesr_name == "chrome":
        driver = webdriver.Chrome()
    elif browesr_name == "firefox":
        driver = webdriver.Firefox()


    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    yield driver
    driver.close()

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)




