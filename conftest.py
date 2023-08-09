import pytest
import openpyxl
import os
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Tools\\AppsForTesting\\AddressBook\\AddressBook.exe")

    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_generate_tests(metafunc):
    if "excel_groups" in metafunc.fixturenames:
        testdata = load_from_excel("groups")
        metafunc.parametrize("excel_groups", testdata, ids=[str(x) for x in testdata])


def load_from_excel(file):
    excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", f"{file}.xlsx")
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active
    testdata = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        testdata.append(row[0])

    return testdata
