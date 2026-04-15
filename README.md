# CopilotLoop — Project Context

You are editing `loop.py`, a single-file Python tool called **CopilotLoop**.

## What It Does

CopilotLoop is a wrapper that lets users have an unlimited conversation with GitHub Copilot Agent Mode using only ONE prompt. Instead of typing multiple messages in Copilot Chat (each costing a request), the user communicates through a text file called `btw.txt`.

## How It Works

1. User runs `python loop.py` — this creates `btw.txt` containing a master prompt (the loop instructions for Copilot)
2. User opens VS Code → Copilot Chat → Agent Mode → types: "Read btw.txt and follow the instructions in it"
3. Copilot reads btw.txt, gets the loop protocol, and starts looping:
   - Does a task
   - Runs `echo "--- LOOP CHECKPOINT ---"` (terminal command)
   - Agent Mode asks user for terminal approval — THIS IS THE PAUSE POINT
   - While approval dialog is open, the user types their next instruction in `loop.py` terminal
   - `loop.py` writes that instruction to `btw.txt`
   - User clicks "Allow" in VS Code
   - Copilot reads btw.txt (now has the new instruction) → does the task → loops
4. User types `stop` in the wrapper → writes "STOP" to btw.txt → Copilot ends the loop

## The Key Trick

The `echo` terminal command is the mechanism that creates a pause. GitHub Copilot Agent Mode requires user approval before executing terminal commands. That approval dialog is the window where the user updates `btw.txt` with the next instruction. This turns a single Copilot session into an infinite back-and-forth without sending new chat messages.

## File Structure

There is only ONE file: `loop.py`. It handles everything:
- **Setup**: Creates `btw.txt` with the master prompt baked in, adds btw.txt to `.gitignore`
- **Wrapper**: Interactive terminal UI where user types instructions that get written to `btw.txt`
- **Commands**: `stop`, `wait`, `status`, `clear`, `help`, `quit`
- **Help**: Built-in usage docs via `python loop.py --help`

## btw.txt States

| Content | Meaning |
|---|---|
| Master prompt (contains "LOOP MODE") | Initial state — Copilot reads this to learn the loop protocol |
| Any instruction text | Copilot treats this as the next task to execute |
| "WAIT" or empty | Copilot pauses — runs echo again and re-reads btw.txt |
| "STOP" | Copilot ends the loop and prints a summary |

## The Master Prompt (stored in PROMPT variable)

The prompt tells Copilot to:
1. Run `echo "--- LOOP CHECKPOINT ---"` after every task
2. Read `btw.txt` fresh every loop
3. If btw.txt has a task → do it → go back to step 1
4. If btw.txt says WAIT → run echo again → re-read
5. If btw.txt says STOP → print summary and end

## Technical Details

- Python 3.6+ (no external dependencies)
- Uses ANSI color codes for terminal UI
- Works on Windows (cls) and Unix (clear)
- Accepts optional project directory argument: `python loop.py /path/to/project`
- btw.txt is always written with a trailing newline
- The `.gitignore` is only modified if btw.txt is not already listed

## When Making Edits

- Keep it as a single file — no splitting into modules
- No external dependencies — stdlib only
- The PROMPT variable is critical — changes to it affect how Copilot behaves in the loop
- The echo command wording matters — Copilot looks for it as the checkpoint signal
- Keep the wrapper simple — it's a terminal tool, not a GUI
