#!/usr/bin/env python3
"""Builds a fresh working copy for a DIY demo.

    python3 setup_diy.py check     # are git, python and claude ready?
    python3 setup_diy.py 2         # build (or rebuild) the copy for DIY demo 2
    python3 setup_diy.py all       # build every copy that needs one
    python3 setup_diy.py clean     # delete all the working copies

Working copies go in a folder called "atc-diy" in your home folder, never in
this repo. Run a demo there, mess it up, then run this script again to get
back to a clean start. The files in this repo are never changed.

Set ATC_DIY_HOME to use a different folder.
"""
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
WORK = Path(os.environ.get("ATC_DIY_HOME", Path.home() / "atc-diy")).expanduser()
PY = sys.executable or "python3"


# ----------------------------------------------------------------- helpers

def say(msg=""):
    print(msg, flush=True)


def _force_remove(func, path, _exc):
    # Git marks some files read-only, which stops Windows from deleting them.
    os.chmod(path, stat.S_IWRITE)
    func(path)


def wipe(path: Path):
    if path.exists():
        shutil.rmtree(path, onerror=_force_remove)


def copy_tree(src: Path, dest: Path):
    wipe(dest)
    shutil.copytree(
        src, dest,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".git"),
    )


def git(cwd: Path, *args, quiet=True):
    cmd = ["git", *args]
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        say(result.stdout + result.stderr)
        raise SystemExit(f"git {' '.join(args)} failed in {cwd}")
    if not quiet:
        say(result.stdout.rstrip())
    return result.stdout


def git_init(cwd: Path):
    """git init on a branch called main, with a commit identity if you have none."""
    git(cwd, "init", "-q")
    git(cwd, "symbolic-ref", "HEAD", "refs/heads/main")
    has_name = subprocess.run(["git", "config", "user.name"], cwd=cwd,
                              capture_output=True, text=True).stdout.strip()
    if not has_name:
        git(cwd, "config", "user.name", "DIY Demo")
        git(cwd, "config", "user.email", "diy-demo@example.com")


def commit_all(cwd: Path, message: str):
    git(cwd, "add", "-A")
    git(cwd, "commit", "-q", "-m", message)


def run_tests(cwd: Path) -> str:
    result = subprocess.run([PY, "-m", "unittest"], cwd=cwd,
                            capture_output=True, text=True)
    lines = (result.stdout + result.stderr).strip().splitlines()
    summary = [line for line in lines if line.startswith(("Ran ", "OK", "FAILED"))]
    for d in cwd.rglob("__pycache__"):
        wipe(d)
    return " / ".join(summary)


def edit(path: Path, old: str, new: str):
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Setup error: expected text not found in {path.name}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# ------------------------------------------------------------------ demos

def demo2():
    """DIY 2: the checkout app with its bug, as a fresh git project."""
    dest = WORK / "checkout"
    copy_tree(REPO / "diy-02-claude-code" / "starter", dest)
    git_init(dest)
    commit_all(dest, "Checkout: initial version")
    say(f"Ready: {dest}")
    say(f"  tests: {run_tests(dest)}   (expect: Ran 6 tests / OK)")
    say(f"  next:  cd {dest}")


def demo3():
    """DIY 3: the same app 'a day later': bug fixed, plus uncommitted work."""
    dest = WORK / "checkout-skill"
    copy_tree(REPO / "diy-02-claude-code" / "starter", dest)
    git_init(dest)
    commit_all(dest, "Checkout: initial version")

    # Commit 2: yesterday's fix is already done.
    edit(dest / "pricing.py",
         '    return int(code.split("-")[1])\n',
         '    if not code:\n'
         '        return 0\n'
         '    prefix, _, number = code.partition("-")\n'
         '    if prefix != "SAVE" or not number.isdigit():\n'
         '        raise ValueError(f"Sorry, {code!r} is not a valid coupon code.")\n'
         '    return int(number)\n')
    edit(dest / "checkout.py",
         '    total = order_total(subtotal, coupon)\n',
         '    try:\n'
         '        total = order_total(subtotal, coupon)\n'
         '    except ValueError as err:\n'
         '        print(err)\n'
         '        return 1\n')
    edit(dest / "tests" / "test_pricing.py",
         '\n\nif __name__ == "__main__":',
         '\n\n    def test_no_coupon_means_no_discount(self):\n'
         '        self.assertEqual(order_total(80.00, ""), 80.00)\n'
         '\n\nif __name__ == "__main__":')
    commit_all(dest, "Handle a missing or invalid coupon code")

    # Uncommitted work in progress for the skill to check: a real change
    # (free shipping now starts at $35) plus a leftover debug line that
    # prints the payment API key.
    edit(dest / "pricing.py", "FREE_SHIPPING_OVER = 50.00", "FREE_SHIPPING_OVER = 35.00")
    edit(dest / "checkout.py", "import sys\n", "import os\nimport sys\n")
    edit(dest / "checkout.py",
         '    subtotal = float(argv[1])\n',
         '    subtotal = float(argv[1])\n'
         '    print("DEBUG payment setup:", os.environ.get("PAYMENTS_API_KEY"))\n')

    # The empty skills folder must exist BEFORE Claude Code starts, so a skill
    # created during the session is picked up without a restart.
    (dest / ".claude" / "skills").mkdir(parents=True, exist_ok=True)

    say(f"Ready: {dest}")
    say("  changed, not committed: " + ", ".join(
        line[3:] for line in git(dest, "status", "--short").splitlines()))
    say(f"  tests: {run_tests(dest)}   (expect: Ran 7 tests / OK)")
    say(f"  next:  cd {dest}")


def demo4():
    """DIY 4: the hackathon folder for Cowork."""
    dest = WORK / "hackathon-judging"
    copy_tree(REPO / "diy-04-cowork" / "starter", dest)
    shutil.copytree(REPO / "diy-05-design" / "files" / "brand", dest / "brand")
    count = len(list((dest / "submissions").iterdir()))
    say(f"Ready: {dest}")
    say(f"  {count} submissions, plus event.md, rubric.md and brand/   (expect: 7 submissions)")


def demo6():
    """DIY 6: Team Notes twice: one for the quick checks, one for the deep scan."""
    main = WORK / "team-notes"
    origin = WORK / "team-notes-origin.git"
    scan = WORK / "team-notes-scan"
    for path in (main, origin, scan):
        wipe(path)
    src = REPO / "diy-06-security" / "starter"

    # The copy for the deep scan: just the app, as a git project.
    copy_tree(src, scan)
    git_init(scan)
    commit_all(scan, "Team Notes baseline")

    # The main copy: a made-up secrets file, a rule that blocks reading it,
    # a pretend GitHub ("origin"), and a teammate's branch with new bugs.
    copy_tree(src, main)
    (main / ".env").write_text(
        "# Made-up values for the DIY demo. Not real credentials.\n"
        "NOTES_DB_PASSWORD=Harbor-Lights-2026!\n"
        "MAILER_API_KEY=key-demo-7c41e9a2b5d84f0e\n", encoding="utf-8")
    (main / ".claude").mkdir()
    (main / ".claude" / "settings.json").write_text(
        '{\n'
        '  "permissions": {\n'
        '    "deny": [\n'
        '      "Read(./.env)",\n'
        '      "Read(./.env.*)",\n'
        '      "Bash(curl *)",\n'
        '      "Bash(wget *)"\n'
        '    ]\n'
        '  }\n'
        '}\n', encoding="utf-8")
    git_init(main)
    commit_all(main, "Team Notes baseline")

    # /security-review compares your branch with origin's main branch, so the
    # project needs an origin. A bare repo on disk stands in for GitHub.
    git(WORK, "init", "-q", "--bare", str(origin))
    git(main, "remote", "add", "origin", str(origin))
    git(main, "push", "-q", "-u", "origin", "main")
    git(main, "remote", "set-head", "origin", "main")

    # The teammate's branch: note import and note sharing, with two new bugs.
    git(main, "checkout", "-q", "-b", "add-sharing")
    app = main / "app.py"
    edit(app, "import sqlite3\n", "import base64\nimport pickle\nimport sqlite3\n")
    edit(app, "from flask import Flask, jsonify, redirect, request, session\n",
         "from flask import (Flask, jsonify, redirect, render_template_string,\n"
         "                   request, session)\n")
    edit(app, '\n\n@app.get("/health")',
         '\n\n@app.post("/notes/import")\n'
         'def import_notes():\n'
         '    # Restore notes exported from another Team Notes workspace\n'
         '    blob = base64.b64decode(request.form.get("data", ""))\n'
         '    notes = pickle.loads(blob)\n'
         '    conn = db()\n'
         '    for note in notes:\n'
         '        conn.execute("INSERT INTO notes (owner_id, title, body) VALUES (?, ?, ?)",\n'
         '                     (session.get("user_id"), note["title"], note["body"]))\n'
         '    conn.commit()\n'
         '    return jsonify({"imported": len(notes)})\n'
         '\n\n@app.get("/notes/<int:note_id>/share")\n'
         'def share_note(note_id):\n'
         '    # A page you can send to a teammate, with an optional message\n'
         '    note = db().execute("SELECT title, body FROM notes WHERE id = ?",\n'
         '                        (note_id,)).fetchone()\n'
         '    message = request.args.get("message", "")\n'
         '    page = f"<h1>{note[\'title\']}</h1><p>{note[\'body\']}</p><p>Note from sender: {message}</p>"\n'
         '    return render_template_string(page)\n'
         '\n\n@app.get("/health")')
    commit_all(main, "Add note import and note sharing")

    ahead = git(main, "rev-list", "--count", "origin/main..HEAD").strip()
    say(f"Ready: {main}")
    say(f"  on branch {git(main, 'branch', '--show-current').strip()}, "
        f"{ahead} commit ahead of origin/main   (expect: add-sharing, 1 commit ahead)")
    say(f"Ready: {scan}   (for the deep scan)")


def demo7():
    """DIY 7: copies of the workbook and the deck."""
    dest = WORK / "office"
    wipe(dest)
    dest.mkdir(parents=True)
    for name in ("harborview-fy2026.xlsx", "harborview-owners-review.pptx"):
        shutil.copy2(REPO / "diy-07-office" / "files" / name, dest / name)
    say(f"Ready: {dest}")
    for name in sorted(os.listdir(dest)):
        say(f"  {name}")


DEMOS = {"2": demo2, "3": demo3, "4": demo4, "6": demo6, "7": demo7}
NO_SETUP = {
    "1": "DIY 1 runs in your browser. Use the files in diy-01-chat/files/ directly.",
    "5": "DIY 5 runs in your browser. Use the files in diy-05-design/files/ directly.",
}


def check():
    ok = True
    say(f"python: {sys.version.split()[0]}", )
    if sys.version_info < (3, 9):
        say("  -> Python 3.9 or later is needed.")
        ok = False
    for tool, args in (("git", ["--version"]), ("claude", ["--version"])):
        path = shutil.which(tool)
        if not path:
            say(f"{tool}: NOT FOUND")
            ok = False
            continue
        out = subprocess.run([path, *args], capture_output=True, text=True)
        say(f"{tool}: {(out.stdout or out.stderr).strip().splitlines()[0]}")
    say(f"working copies go in: {WORK}")
    say("All set." if ok else "Fix the items above, then run this again.")


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        say(__doc__)
        return 0
    choice = argv[1].lower().removeprefix("diy").strip("-")
    if choice == "check":
        check()
        return 0
    if choice == "clean":
        wipe(WORK)
        say(f"Removed {WORK}")
        return 0
    if choice in NO_SETUP:
        say(NO_SETUP[choice])
        return 0
    WORK.mkdir(parents=True, exist_ok=True)
    if choice == "all":
        for key in DEMOS:
            say(f"--- DIY {key}")
            DEMOS[key]()
        return 0
    if choice not in DEMOS:
        say(f"Unknown demo {argv[1]!r}. Use 1-7, all, check or clean.")
        return 2
    DEMOS[choice]()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
