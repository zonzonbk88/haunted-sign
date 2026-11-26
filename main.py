"""make.fun entry: Funniest Sign on a Haunted Server Room Door.

Bounty: u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a
Gate: /output/entry.txt must be UTF-8, 1-120 characters, not only whitespace.
Writes exactly one line, with no trailing newline.
"""

LINE = "DO NOT REBOOT RACK 4. THE GHOST LIVES THERE — HE PAYS RENT IN UPTIME."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
