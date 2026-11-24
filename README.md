# Charm the Commuter: Forecast a City That Isn't

[![Charm the Commuter: Forecast a City That Isn't](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/jinan86/charm-the-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/jinan86/charm-the-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather forecast, at most 140 characters, for a city that does not exist — written to make a bored commuter at a rainy bus stop smile once.

## The entry

> Port Merrow: rain steady till noon, 54°, then a break just long enough to regret the jacket you left on the hook this morning.

(126 characters.)

The forecast keeps the rhythm of a real broadcast — place, weather, temperature, timing — and bends it once: the break in the rain arrives just in time for the commuter to regret the jacket left hanging at home. Port Merrow is invented; the regret is universal.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (Python 3.13, stdlib only)
```

The program validates its own line against the gate (1–140 characters, not whitespace-only) before writing it, and prints the character count.

## License

MIT — see [LICENSE](LICENSE).
