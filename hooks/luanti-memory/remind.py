"""Point Codex at a configured Luanti knowledge checkout on each user turn."""

import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--knowledge-root", required=True, type=Path)
    options = parser.parse_args()
    guide = options.knowledge_root.expanduser().resolve() / "docs" / "agent-memory.md"
    if not guide.is_file():
        parser.error(f"knowledge guide not found: {guide}. Set --knowledge-root to the knowledge checkout.")
    print(
        "For tasks concerning Luanti, Minetest, their mods, A.E.S., MTUI, or related "
        "development and content design, including follow-ups, use the shared knowledge "
        f"repository at {guide.parent.parent}. Before answering or acting, read {guide} "
        "and consult the relevant wiki branches. Before completing the task, follow "
        "its knowledge update, validation, commit and push procedure under the owner's "
        "current authorization. Determine relevance from the conversation and project."
    )
