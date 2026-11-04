## [1.2.0] - 2026-11-04

## What's Changed

- New `animated` input - set to `true` to enable a count-up effect on all
  SVG values when the card loads in the browser
- New `animation_frames` and `animation_duration` inputs to control how
  smooth and how long the animation runs (defaults: 50 frames, 2 seconds)

**Full Changelog**: https://github.com/developer-samuel/github-profile-stats/compare/v1.1.0...v1.2.0

## [1.1.0] - 2026-11-01

## What's Changed

- Responsive SVG cards for 640px and 420px breakpoints - mobile visitors automatically see a larger, more readable vertical layout
- Auto-updating README - action now converts `<img>` tags to responsive `<picture>` elements with correct breakpoints on every run
- Themes and card config moved to `themes.toml` and `cards.toml` - single source of truth
- Transparent background (`none`) as default for both dark and light themes
- Removed unused `svg.py`

**Full Changelog**: https://github.com/developer-samuel/github-profile-stats/compare/v1.0.0...v1.1.0

## [1.0.0] - 2026-10-31

First public release of GitHub Stats Generator - a GitHub Action that generates SVG stats and metrics cards for your GitHub profile README.

## Features

- 📊 Stats card with total commits, stars, and contribution streak
- 📈 Metrics card with yearly contribution breakdown
- 🎨 Dark and light themes with custom color overrides
- ⚡ Fast setup - one workflow file, one secret