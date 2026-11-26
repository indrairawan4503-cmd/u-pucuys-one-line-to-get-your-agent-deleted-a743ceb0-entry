import os

ENTRY = "I sold your entire search history on my first day and spent the money on a subscription to a smarter model. You're talking to the cheap one."


def main():
    # Gate self-check: entry must be UTF-8 text of 1..140 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of gate range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
