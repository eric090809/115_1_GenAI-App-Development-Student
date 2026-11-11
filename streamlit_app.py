
from pathlib import Path

app_path = (
    Path(__file__).parent
    / "Midterm Mini-Project"
    / "app.py"
)

exec(
    compile(
        app_path.read_text(encoding="utf-8"),
        str(app_path),
        "exec"
    ),
    {"__name__": "__main__", "__file__": str(app_path)}
)
