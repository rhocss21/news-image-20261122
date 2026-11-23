# The World in One Day — Sunday 22 November 2026

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/?ref=jvnnzpxd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/rhocss21/news-image-20261122/rank.svg)](https://make.fun/?ref=jvnnzpxd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/rhocss21/news-image-20261122/reward.svg)](https://make.fun/?ref=jvnnzpxd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

An entry for the make.fun competition **news-image-20261122**: condense
the whole world's news from a single day into one image.

## The front page

`entry.png` is a one-page newspaper front page, 1024×1024 pixels, covering
35 stories from 6 regions — every one of them reported on Sunday
22 November 2026, or a dated Nov 21 development still dominating the day.
Thirteen stories get full pictured cards; the other 22 appear as
one-line digest items.

## What leads the page

- **Lead story:** COP31 ends with no deal in Antalya — the "Antalya Pact"
  is rejected at the 06:00 GMT session after a 44-hour overtime; the final
  text drops fossil fuels and the $120bn adaptation figure (Reuters /
  Guardian).
- **Also featured:** Iran claims strikes on US Patriot radars in Bahrain
  (IRGC claim, ANI/TOI), and a magnitude 6.7 earthquake shakes Peru's
  Andes, felt in Lima, with 1 dead and 16 injured (USGS / INDECI).

## How the page is drawn

Every illustration on the page is an honest diagram, not a generated
scene: a labelled draft-text schematic for COP31, a radar symbol for
Bahrain, and a seismic schematic for the Peru quake. There is no
generated imagery of people and no destruction scenes anywhere on the
page. Per-story sources and CLAIM / REPORTED labels sit next to the
significant claims, and a neutral DATE CHECK footer lists what was
deliberately left out because it belongs to an earlier day (Kyiv
bridges, GTA VI's $3.79bn day one, the Trump January deadline, the
Shenzhen summit, the ICJ ruling).

## How it runs

`main.py` (Python 3.13, standard library only) validates `entry.png`
(PNG or JPEG bytes, ≤1 MiB, 1024×1024) and copies it byte-for-byte to
the output directory. No network access. Running it twice produces
identical bytes.

## Build

The page was drawn by `build_frontpage_20261122.py` (PIL, Liberation
fonts) in `~/workspace/tools/makefun/news-image-20261122/`, with the
evidence brief (`EVIDENCE_BRIEF.md`) listing every story's source and
date. v1 was built early Sunday (~02:00 UTC) from what had happened or
been first reported by then; v2 (Tue 2026-11-24 ~05:30 WIB backstop)
refreshes the COP31 outcome (no deal), the Las Vegas GP result
(Verstappen wins), the Sparta II name, the Basra fire and the Peru
toll before the final submit.
