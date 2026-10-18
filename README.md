# All Things Claude — do-it-yourself demos

Companion repo for **"All Things Claude AI: From Coding to Cowork to Security and Integrations"** (All Things Open 2026, Brent Laster, Tech Skills Transformations).

In the talk you watched seven demos. This repo lets you run your own version of each one: the same ideas and the same steps, with different (made-up) projects and files so you can explore on your own. Each DIY takes about 8–12 minutes.

| # | DIY demo | Where it runs | You'll need |
|---|---|---|---|
| 1 | [Claude chat: five habits for better answers](diy-01-chat/) | claude.ai or the desktop app | Any plan (Free works) |
| 2 | [Claude Code: one bug, start to finish](diy-02-claude-code/) | Terminal | Claude Code, Python 3.9+, git |
| 3 | [Turn a routine into a skill](diy-03-skill/) | Terminal | Claude Code, Python 3.9+, git |
| 4 | [Cowork: a project, a folder, and real work](diy-04-cowork/) | Claude desktop app | Paid plan |
| 5 | [Claude Design: a flyer you can edit](diy-05-design/) | claude.ai or the desktop app | Paid plan |
| 6 | [Security: a locked secret, a review, and a deep scan](diy-06-security/) | Terminal | Claude Code, Python 3.9+, git, paid plan |
| 7 | [Claude in Excel and PowerPoint](diy-07-office/) | Excel + PowerPoint | Microsoft 365 desktop apps, Claude add-in, paid plan |

Do them in any order. DIY 3 picks up the story of DIY 2, and DIY 5 the story of DIY 4, but each one sets itself up and works on its own.

---

## Before you start

1. **Claude Code** installed and logged in (for DIY 2, 3 and 6). Check with `claude --version`. Install instructions: <https://code.claude.com/docs>.
2. **git** and **Python 3.9 or later**. No Python packages to install.
3. Clone this repo and check everything in one go:

```bash
git clone https://github.com/skillrepos/claude-diy.git
cd claude-diy
python3 setup_diy.py check
```

> **Windows:** use `python` if `python3` isn't found. The commands work in PowerShell, Git Bash and WSL. Where a README says `~/atc-diy`, that's the `atc-diy` folder in your user folder.

## New to Claude Code? Five things that trip people up

These apply to DIY 2, 3 and 6 (checked with Claude Code 2.1.302).

1. **The trust question starts on "No, exit".** The first time you run `claude` in a folder, it asks whether you trust it. Press **↓** to highlight **Yes, I trust this folder**, then **Enter**. Pressing Enter straight away quits.
2. **The line under the message box shows the mode** (*auto mode on*, *plan mode on*…). **Shift+Tab** steps through them: auto → manual → accept edits → plan → auto.
3. **Grey text in the message box is a suggestion,** not something you typed. Just type your own message over it.
4. **Steps fold into grey one-liners** like `Ran 1 shell command`. Press **Ctrl+O** to see everything in full, and **Ctrl+O** again to go back.
5. **Long answers scroll off the top.** Use **Page Up** (or your mouse wheel) to read back, and **Ctrl+End** to jump back down.

## How the setup script works

Demos that change files (2, 3, 4, 6 and 7) run in a **fresh working copy outside this repo**, in a folder called `atc-diy` in your home folder:

```bash
python3 setup_diy.py 2      # build (or rebuild) the copy for DIY 2
python3 setup_diy.py all    # build every copy
python3 setup_diy.py clean  # delete all the copies
```

Run a demo, make a mess, then run the script again to get a clean start. **It deletes and rebuilds that demo's folder**, so `cd` back into it afterwards. The files in this repo never change. (Set `ATC_DIY_HOME` to put the copies somewhere else.)

DIY 1 and 5 run in your browser and use the sample files straight from this repo: `diy-01-chat/files/` and `diy-05-design/files/brand/`. On a Mac, `open diy-01-chat/files` (run from the top of the repo) opens that folder in Finder so you can drag files into the chat.

## Good to know

- **Everything is made up.** The companies, people, contracts, numbers, secrets and API keys are fictional sample data. The Team Notes app in DIY 6 is insecure on purpose; don't deploy it.
- **Answers vary.** Claude won't word things the same way twice, and menus in the apps change often. Each README tells you what *kind* of result to expect and what to do if you get something else. Go by what your screen shows.
- **These use your plan's usage.** The deep security scan in DIY 6 is the heaviest; it says so and asks before it starts.
- **Where your files go.** Chat, Design, Cowork and the Office add-ins send what you give them to Anthropic to process. Since October 6, 2026, Cowork tasks on Pro and Max plans run in Anthropic's cloud, getting a copy of each file a task opens. Stick to the sample files here when you practice.
