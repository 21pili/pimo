# test_visualize.py
import pytest
from pimo.visualize import Visualize

@pytest.fixture
def visualize_instance():
    return Visualize()
