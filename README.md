# Sample Sanity Pipeline

A complete system that demonstrates how to measure and capture sanity test metrics across GitHub repositories, with visualization and Confluence integration.

## Overview

This repository contains a sample Python CLI tool with basic sanity tests, a GitHub Actions workflow for test execution, metrics collection, and a dashboard for visualizing test results. The system is designed to provide end-to-end visibility into test metrics and critical workflow coverage.

## Features

- Simple Python CLI tool with basic functionality
- Pytest-based sanity tests with critical workflow tagging
- GitHub Actions workflow for automated testing
- Metrics collection and storage using GitHub Pages
- Interactive dashboard for visualizing test metrics
- Confluence integration for team-wide visibility

## Directory Structure

```
sample-sanity-pipeline/
├── app.py                      # Sample Python CLI tool
├── tests/
│   └── test_sanity.py          # Pytest-based sanity tests
├── requirements.txt            # Python dependencies
├── .github/workflows/
│   └── sanity-tests.yml        # GitHub Actions workflow
├── confluence_integration.html # Guide for Confluence integration
└── README.md                   # This file
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git
- GitHub account

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/sample-sanity-pipeline.git
   cd sample-sanity-pipeline
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

#### Running the CLI Tool

The sample CLI tool accepts a `--greet` argument:

```
python app.py --greet
```

This will output: `Hello, World!`

#### Running Tests Locally

To run the sanity tests locally:

```
pytest tests/
```

To generate Allure reports locally:

```
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow (`sanity-tests.yml`) that:

1. Runs on every push and pull request
2. Sets up Python and installs dependencies
3. Executes tests with Allure reporting
4. Parses test metrics (pass/fail rate, duration, critical test count)
5. Converts results to JSON format
6. Deploys metrics and dashboard to GitHub Pages

## Metrics Collection

The system captures the following metrics:

- **Pass/Fail Rate**: Count of test outcomes from Allure results
- **Test Duration**: Timing from GitHub Actions
- **Critical Workflow Coverage**: Count of tests tagged with `@critical_workflow`

Metrics are stored as JSON files in the GitHub Pages branch and are used to generate the dashboard.

## Dashboard

The dashboard provides visualization of test metrics with:

- Pass/Fail pie chart
- Test duration line graph
- Test results bar chart
- Critical tests coverage line graph
- Table of recent test runs

The dashboard is automatically deployed to GitHub Pages and can be accessed at:
`https://YOUR_USERNAME.github.io/sample-sanity-pipeline/dashboard.html`

## Confluence Integration

To embed the dashboard in Confluence, refer to the `confluence_integration.html` file for detailed instructions. Two options are provided:

1. Using the HTML macro
2. Using the Iframe macro

## Customization

### Adding More Tests

To add more tests, create new test functions in `tests/test_sanity.py` or add new test files in the `tests/` directory.

To mark a test as a critical workflow test, use the `@pytest.mark.critical_workflow` decorator:

```python
@pytest.mark.critical_workflow
def test_your_critical_function():
    # Test implementation
```

### Modifying the Dashboard

The dashboard is generated in the GitHub Actions workflow. To modify it, edit the HTML and JavaScript code in the `sanity-tests.yml` file.

## Troubleshooting

### Common Issues

- **Tests not running in GitHub Actions**: Ensure the workflow file is in the correct location (`.github/workflows/sanity-tests.yml`)
- **Dashboard not updating**: Check if the GitHub Pages branch exists and if the workflow has permission to push to it
- **Confluence embedding not working**: Verify that your Confluence instance allows iframe embedding from GitHub Pages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Pytest for the testing framework
- Allure for test reporting
- GitHub Actions for CI/CD
- Chart.js for dashboard visualization
