#!/usr/bin/env python3
"""
🔁 CopilotLoop v1.0 — One prompt. Infinite iterations.

Usage:
    python loop.py              Run in current directory
    python loop.py /path        Run in specific project
    python loop.py --help       Show how it works
"""

import os
import sys

BTW = "btw.txt"

PROMPT = """You are now in LOOP MODE. Follow this protocol exactly:

1. Run this terminal command: echo "--- LOOP CHECKPOINT ---"
2. Read the file `btw.txt` in the project root
3. If btw.txt says "STOP" — end the loop, print a summary of everything you did
4. If btw.txt says "WAIT" or is empty — run `echo "--- WAITING ---"` then read btw.txt again
5. If btw.txt has any other text — that is your task. Do it. Then go back to step 1.

RULES:
- Always run the echo command BEFORE reading btw.txt (this gives me time to update it)
- Always read btw.txt FRESH every loop — never use cached content
- After finishing each task, briefly say what you did before running the echo
- Keep going until you see STOP
"""

C = "\033[96m"
G = "\033[92m"
Y = "\033[93m"
R = "\033[91m"
D = "\033[2m"
B = "\033[1m"
X = "\033[0m"


def write(text, d):
    with open(os.path.join(d, BTW), "w") as f:
        f.write(text + "\n")


def read(d):
    p = os.path.join(d, BTW)
    return open(p).read().strip() if os.path.exists(p) else ""


def setup(d):
    write(PROMPT, d)
    gi = os.path.join(d, ".gitignore")
    existing = open(gi).read() if os.path.exists(gi) else ""
    if BTW not in existing:
        with open(gi, "a") as f:
            f.write(f"\n# CopilotLoop\n{BTW}\n")


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(f"""
{B}HOW IT WORKS:{X}

  1. Run: {C}python loop.py{X}
  2. In VS Code → Copilot Chat → Agent Mode → type:
     {C}Read btw.txt and follow the instructions in it{X}
  3. Copilot reads the loop prompt from btw.txt
  4. Copilot runs echo → approval dialog pops up
  5. Type your instruction here → click Allow in VS Code
  6. Copilot reads btw.txt → does task → echo → repeat
  7. Type {C}stop{X} when done
""")
        return

    d = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else os.getcwd()

    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
{C}{B}  🔁 CopilotLoop v1.0{X}
{D}  One prompt. Infinite iterations.{X}

  Project: {C}{d}{X}
""")

    setup(d)

    print(f"""{Y}{B}  → Open Copilot Agent Mode and type:{X}
  {C}  Read btw.txt and follow the instructions in it{X}

{D}  Then come back here. Type 'help' for commands.{X}
""")

    n = 0
    while True:
        cur = read(d)
        is_prompt = "LOOP MODE" in cur
        tag = "READY" if is_prompt else ("WAITING" if cur in ("WAIT", "") else "SENT")
        color = C if is_prompt else (Y if tag == "WAITING" else G)

        print(f"{D}────────────────────────────────{X}")
        print(f"  {color}{tag}{X}  │  #{C}{n}{X}")

        try:
            inp = input(f"\n{B}→ {X}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{D}Bye.{X}")
            break

        if not inp:
            continue

        cmd = inp.lower()

        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "stop":
            write("STOP", d)
            print(f"{R}⏹ STOP sent.{X}")
            break
        elif cmd == "wait":
            write("WAIT", d)
            print(f"{Y}⏸ Paused.{X}")
        elif cmd == "status":
            c = read(d)
            print(f"  {C}{c[:120] + '...' if len(c) > 120 else c or '(empty)'}{X}")
        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif cmd == "help":
            print(f"""
  {B}(text){X}    Send instruction to Copilot
  {B}stop{X}      End the loop
  {B}wait{X}      Pause the loop
  {B}status{X}    Show btw.txt content
  {B}clear{X}     Clear screen
  {B}quit{X}      Exit wrapper
""")
        else:
            write(inp, d)
            n += 1
            print(f"{G}✅ Sent. Approve the echo in VS Code.{X}")


if __name__ == "__main__":
    main()
