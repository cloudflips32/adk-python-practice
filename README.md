# ADK Python practice

Practice workspace for Google’s [Agent Development Kit (ADK) for Python](https://google.github.io/adk-docs/), following the [Python quickstart](https://google.github.io/adk-docs/get-started/python/). The project contains a small LLM agent with a custom tool, runnable from the CLI or the ADK web UI.

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

This matches the structure described in the quickstart (`adk create` + edits to `agent.py`):

```text
practice_agent/
  agent.py      # Defines root_agent and tools
  __init__.py   # Package entry (imports agent)
  .env          # GOOGLE_API_KEY (local only; not committed)
```

The **`root_agent`** in `practice_agent/agent.py` is the required entry point ADK loads. The agent uses **Gemini** (`gemini-2.5-flash` as chosen during `adk create`) and a **`get_current_time`** tool that returns the current local time (a stand-in for city-specific time in the quickstart).

## API key

The agent uses the **Gemini API** via a Google AI Studio key.

1. Create a key: [Google AI Studio — API keys](https://aistudio.google.com/app/apikey)
2. Put it in `practice_agent/.env`:

   ```env
   GOOGLE_API_KEY="YOUR_API_KEY"
   ```

Keep `.env` out of version control (this repo’s `.gitignore` ignores `*.env`).

## Run the agent

Run commands from the **repository root** (the directory that contains the `practice_agent/` folder).

### CLI (`adk run`)

```bash
adk run practice_agent
```

You get an interactive session; type `exit` to quit.

### Web UI (`adk web`)

```bash
adk web --port 8000
```

Open [http://localhost:8000](http://localhost:8000), pick the agent in the UI, and chat.

ADK Web is intended for **development and debugging**, not production.

## How this maps to the quickstart

| Quickstart step | Status here |
|-----------------|-------------|
| Install `google-adk` | Done (`pip install google-adk`) |
| `adk create …` | `practice_agent` created with Gemini + Google AI backend |
| `root_agent` + a tool in `agent.py` | `get_current_time` + instructions/tools wired on `Agent` |
| `GOOGLE_API_KEY` in `.env` | `practice_agent/.env` |
| `adk run` / `adk web` | Run from repo root as above |

For model and auth options beyond the default Gemini + API key, see: [AI models for ADK agents](https://google.github.io/adk-docs/agents/models/).

## Next steps

After the quickstart, use the ADK **build guides** and the rest of the [ADK documentation](https://google.github.io/adk-docs/) to add workflows, more tools, or deployment patterns.
