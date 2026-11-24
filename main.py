#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
fictional city of Port Merrow to /output/entry.txt.

The forecast keeps the rhythm of a real broadcast -- place, weather,
temperature, timing -- and bends it once: the break in the rain is just
long enough for the commuter to regret the jacket left at home.
"""

FORECAST = (
    "Port Merrow: rain steady till noon, 54\xb0, then a break just long "
    "enough to regret the jacket you left on the hook this morning."
)


def main() -> None:
    """Validate the line against the gate, then write it out."""
    text = FORECAST.strip()
    if not text:
        raise SystemExit("forecast is empty")
    if len(text) > 140:
        raise SystemExit(f"forecast is {len(text)} characters, over the 140 limit")
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
