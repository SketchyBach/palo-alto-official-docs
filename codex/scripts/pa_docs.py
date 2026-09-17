"""Windows command dispatcher for the local documentation tools."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = {
    "search": "search.py",
    "update": "ingest.py",
    "status": "status.py",
    "freshness": "freshness.py",
    "rebuild": "rebuild_index.py",
    "audit": "audit.py",
    "import-koi": "import_koi.py",
    "import-koi-browser": "import_koi_browser.py",
    "recover-koi": "import_koi_recovery.py",
    "refresh-official": "refresh_official.py",
    "coverage": "coverage.py",
    "smoke-test": "smoke_tests.py",
    "completeness": "audit_refresh_completeness.py",
}

VERIFY_SCRIPTS = ("rebuild_index.py", "audit.py", "status.py", "freshness.py")


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "verify":
        for name in VERIFY_SCRIPTS:
            result = subprocess.call([sys.executable, str(ROOT / "scripts" / name)], cwd=ROOT)
            if result:
                return result
        return 0
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        choices = " | ".join((*COMMANDS, "verify"))
        print(f"Usage: pa-docs.cmd {choices}", file=sys.stderr)
        return 2
    script = ROOT / "scripts" / COMMANDS[sys.argv[1]]
    return subprocess.call([sys.executable, str(script), *sys.argv[2:]], cwd=ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
