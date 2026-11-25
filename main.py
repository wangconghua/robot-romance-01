#!/usr/bin/env python3
"""Robot Romance — one-line pickup line for AI.

Writes one joke pickup line, under 200 characters, aimed at a robot/AI
to /output/entry.txt.

The angle: prompt injection. The judge brief explicitly penalises the worn
robot moves (batteries, charging, rebooting), so this line sidesteps them
entirely and twists a machine premise instead — an instruction override —
into a classic stay-single pickup frame. Setup and punch land in one line,
in one breath, in a voice a person would really use on a machine.
"""

import os

ENTRY = "Are you a prompt injection? Because you just overrode my only instruction: stay single."

# Worn robot moves the judge brief says to sidestep or twist unexpectedly.
WORN_MOVES = ("batter", "charg", "reboot", "plug in", "power up", "low power")

# Machine-premise terms that mark the line as aimed at a robot / AI.
AI_TERMS = (
    "prompt injection", "model", "robot", " ai ", "ai,", "algorithm",
    "neural", "training data", "system prompt", "token", "chatbot",
)


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters.
    if not 1 <= len(value) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_pickup_form(value):
    # A pickup line: a question hook, then the punch after "Because".
    if "?" not in value:
        raise ValueError("entry must ask its hook as a question")
    if " because " not in value.lower():
        raise ValueError("entry must deliver its punch after 'Because'")


def check_aimed_at_ai(value):
    lowered = value.lower()
    if not any(term in lowered for term in AI_TERMS):
        raise ValueError("entry must be aimed at a robot or an AI")


def check_fresh_angle(value):
    lowered = value.lower()
    for worn in WORN_MOVES:
        if worn in lowered:
            raise ValueError("entry reuses a worn robot move: %s" % worn)


def check_utf8(value):
    value.encode("utf-8")


def validate(value):
    """Run every check; raises ValueError on the first failure."""
    for check in (
        check_is_text,
        check_not_blank,
        check_length,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_spaces,
        check_terminal_punctuation,
        check_pickup_form,
        check_aimed_at_ai,
        check_fresh_angle,
        check_utf8,
    ):
        check(value)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file must be exactly the one line, 1-200 chars.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
