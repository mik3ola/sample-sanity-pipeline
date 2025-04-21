import subprocess
import sys
import pytest
import allure

@allure.feature("Basic Functionality")
def test_greet_success():
    """Test successful invocation of --greet argument."""
    result = subprocess.run(
        [sys.executable, "../app.py", "--greet"],
        capture_output=True,
        text=True,
        cwd="tests"
    )
    assert result.returncode == 0
    assert "Hello" in result.stdout
    assert result.stderr == ""

@allure.feature("Error Handling")
def test_failing_for_coverage():
    """Simulate a failing test for coverage demonstration."""
    # This test is intentionally designed to fail
    result = subprocess.run(
        [sys.executable, "../app.py", "--non-existent-arg"],
        capture_output=True,
        text=True,
        cwd="tests"
    )
    # Incorrect assertion to simulate failure
    assert "Hello" in result.stdout

@allure.feature("Critical Workflow")
@pytest.mark.critical_workflow
def test_critical_workflow():
    """Test critical workflow functionality with --greet."""
    result = subprocess.run(
        [sys.executable, "../app.py", "--greet"],
        capture_output=True,
        text=True,
        cwd="tests"
    )
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout
    
    # Additional assertions for critical workflow
    assert len(result.stdout.strip()) > 0
    assert "Hello" in result.stdout
