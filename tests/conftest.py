# conftest.py
import os
from xml.dom.minidom import parse


def pytest_sessionfinish(session, exitstatus):  # pylint: disable=unused-argument
    """Beautify the junit.xml file if it exists after the test session finishes."""
    junit_file = "junit.xml"
    if os.path.exists(junit_file):
        dom = parse(junit_file)
        pretty_xml_as_string = dom.toprettyxml()
        with open(junit_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml_as_string)
        print(f"{junit_file} has been beautified.")
    else:
        print(f"{junit_file} does not exist.")
