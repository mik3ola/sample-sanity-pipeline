# Python 3.10 Compatibility Notes

## Known Issues

### Allure Reporting

The Allure reporting packages (`pytest-allure-adaptor` and `allure-pytest`) are not compatible with Python 3.10 due to changes in the `collections` module. Specifically, in Python 3.10, the `Mapping` class was moved from `collections` to `collections.abc`.

### Workarounds

1. **Remove Allure Dependencies**: The simplest solution is to run tests without Allure reporting by:
   - Removing allure imports and decorators from test files
   - Removing allure packages from requirements.txt

2. **Use Python 3.9 or Earlier**: If Allure reporting is necessary, consider using Python 3.9 or earlier, which is compatible with these packages.

3. **Advanced Solution**: For advanced users, you can create a patch that modifies the `namedlist.py` file in your virtual environment to use `collections.abc.Mapping` instead of `collections.Mapping`.

## Current Setup

The current setup uses option 1 - running tests without Allure reporting. The tests function correctly, but without the detailed reports that Allure would provide. 