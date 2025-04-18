#!/usr/bin/env python3
# Patch for Python 3.10+ to run pytest with allure
import collections, collections.abc, sys
import pytest
import os

# Apply the patches for all needed classes
collections.Mapping = collections.abc.Mapping
collections.Sequence = collections.abc.Sequence
print("Patches applied: collections.Mapping and collections.Sequence")

# Create allure results directory if it doesn't exist
if not os.path.exists("allure-results"):
    os.makedirs("allure-results")

# Run pytest with allure reporting
sys.exit(pytest.main(["tests/", "-v", "--alluredir=allure-results"])) 