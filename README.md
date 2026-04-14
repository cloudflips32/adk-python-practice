# ADK Python practice

Practice workspace for Google’s [Agent Development Kit (ADK) for Python](https://google.github.io/adk-docs/), following the [Python quickstart](https://google.github.io/adk-docs/get-started/python/). The repo includes two sample agents you can run from the CLI or the ADK web UI: a **quickstart** agent with one tool, and a **multi-tool** agent that exercises several tools on the same `Agent`.

## Prerequisites

- Python 3.10 or later (this repo was set up with Python 3.14)
- `pip`

## Setup

1. **Virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   ```

   Activate it:

   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   - **Windows (CMD):** `.venv\Scripts\activate.bat`
   - **macOS / Linux:** `source .venv/bin/activate`

2. **Install ADK**

   ```bash
   pip install google-adk
   ```

   The quickstart uses `pip install google-adk`; a `requirements.txt` can be added later if you want pinned versions.

## Project layout

```text
1-Quickstart/practice_agent/
  agent.py      # Defines root_agent and tools
  __init__.py   # Package entry (imports agent)
  .env          # GOOGLE_API_KEY (local only; not committed)

2-Multi-tool/multi_tool_practice_agent/
  agent.py      # root_agent with multiple tools
  __init__.py
  .env
```

**Quickstart (`1-Quickstart/practice_agent/`)** follows the layout from `adk create` + edits to `agent.py`. The **`root_agent`** is the entry point ADK loads. It uses **Gemini** (`gemini-2.5-flash`) and a single **`get_current_time`** tool that returns the current local time (a stand-in for city-specific time in the quickstart).

**Multi-tool (`2-Multi-tool/multi_tool_practice_agent/`)** uses the same pattern with three tools on one agent: **`get_powershell_commands`**, **`get_bash_commands`**, and **`get_cmd_commands`**. The instructions steer the model to pick the right shell and tool for the user’s task (terminal command learning / practice).

## API key

The agents use the **Gemini API** via a Google AI Studio key.

1. Create a key: [Google AI Studio — API keys](https://aistudio.google.com/app/apikey)
2. Put it in each agent folder you run (same variable in each):

   - `1-Quickstart/practice_agent/.env`
   - `2-Multi-tool/multi_tool_practice_agent/.env`

   ```env
   GOOGLE_API_KEY="YOUR_API_KEY"
   ```

Keep `.env` out of version control (this repo’s `.gitignore` ignores `*.env`).

## Run the agents

Run commands from the **repository root**.

### CLI (`adk run`)

Quickstart (single tool):

```bash
adk run 1-Quickstart/practice_agent
```

Multi-tool:

```bash
adk run 2-Multi-tool/multi_tool_practice_agent
```

You get an interactive session; type `exit` to quit.

### Web UI (`adk web`)

```bash
adk web --port 8000
```

Open [http://localhost:8000](http://localhost:8000), pick the agent in the UI, and chat. The picker lists agents discovered under the current working directory (running from the repo root exposes both packages).

ADK Web is intended for **development and debugging**, not production.

## How this maps to the quickstart

| Quickstart step | Status here |
|-----------------|-------------|
| Install `google-adk` | Done (`pip install google-adk`) |
| `adk create …` | `1-Quickstart/practice_agent` created with Gemini + Google AI backend |
| `root_agent` + a tool in `agent.py` | `get_current_time` + instructions/tools wired on `Agent` |
| `GOOGLE_API_KEY` in `.env` | `1-Quickstart/practice_agent/.env` |
| `adk run` / `adk web` | Run from repo root as above |

The **multi-tool** example builds on the same ideas (Gemini, `root_agent`, tools in `tools=[...]`); see `2-Multi-tool/multi_tool_practice_agent/agent.py` for wiring multiple callables on one agent.

For model and auth options beyond the default Gemini + API key, see: [AI models for ADK agents](https://google.github.io/adk-docs/agents/models/).

## Next steps

Use the ADK **build guides** and the rest of the [ADK documentation](https://google.github.io/adk-docs/) to add workflows, more tools, or deployment patterns. The multi-tool folder is a concrete starting point for agents that must choose among several tools per turn.
