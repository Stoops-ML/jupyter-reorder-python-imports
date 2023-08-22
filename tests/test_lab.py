"""Tests for jupyter_black running in jupyter lab."""
import typing as t

import pytest
from conftest import source_from_cell


@pytest.mark.xfail(reason="Playwright ^1.37.0 does not support jupyterlab ^4.0.5")
def test_load_ext(lab: t.Callable[..., t.Dict[str, t.Any]]) -> None:
    """Test loading with `%load_ext jupyter_reorder_python_imports`"""
    cells = [
        {
            "source": ["%load_ext jupyter_reorder_python_imports"],
        },
        {
            "id": "imports1",
            "source": ["import re\nimport datetime"],
        },
        {
            "id": "imports2",
            "source": ["import datetime\nimport re"],
        },
    ]
    output = lab(cells)
    cell_imports1 = source_from_cell(output, "imports1")
    assert "".join(cell_imports1) == "import datetime\nimport re"
    cell_imports2 = source_from_cell(output, "imports2")
    assert "".join(cell_imports2) == "import datetime\nimport re"
