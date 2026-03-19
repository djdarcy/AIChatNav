# Changelog

All notable changes to AI ChatNav will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.3-alpha] - 2026-03-18

### Added
- FUNDING.yml (GitHub Sponsors, Ko-fi, Buy Me a Coffee)
- GitHub templates: dependabot, PR template, release template, stale bot
- Per-site valid path filtering (widget only shows on chat pages)
- Per-site vertical nudge (nudgeY) for fine-tuning widget position
- Chrome Web Store assets (marquee tile, promo tile, screenshots)

### Fixed
- Widget no longer appears on non-chat pages (e.g., claude.ai/downloads)
- SPA navigation hides widget when leaving chat pages, shows when returning

## [0.2.2-alpha] - 2026-03-18

### Added
- Centralized TIMING and LAYOUT constants (eliminated all magic numbers)
- README widget screenshots (light and dark themes)
- ROADMAP v0.4.0: Progressive widget layouts (#4)

### Fixed
- Claude.ai "Both" mode now finds all messages (walks conversation container DOM)
- Claude.ai "AI" mode finds AI responses by excluding user messages from container
- cycleMode updates counter immediately (removed deferred setTimeout)
- Scroll-back to current message after expand/collapse (Alt+O, Ctrl+Alt+O)

## [0.2.1-alpha] - 2026-03-18

### Added
- Chrome Web Store prep: privacy policy, store listing, packaging script
- Release workflow: tag-triggered GitHub Releases with .zip artifact
- CI package validation and artifact upload
- Wrap navigation setting (off by default): Up at first wraps to last and vice versa
- Counter shows closest message position on load (was 0/N)

### Fixed
- Widget no longer rides up when Claude.ai textbox expands (bottom-anchored when docked)
- navigatePrev simplified: uninitialized state handled separately from at-first-message

## [0.2.0-alpha] - 2026-03-18

### Added
- Settings/options page with chrome.storage.local persistence
- CSS variable theming with Dark, Light, and Auto-detect modes
- Options page fades smoothly between themes on change
- Auto-expand truncated messages on Claude.ai (opt-in, sibling button search)
- Alt+O to toggle expand/collapse on current message
- Ctrl+Alt+O to toggle auto-expand setting at runtime
- Expand/collapse all button (vertical ellipsis) on widget panel
- Overlay/modal detection: widget hides when image viewers or dialogs open
- Scroll positioning targets 8% from viewport top for better message visibility
- Faster revisit load (2s vs 5s first-load via sessionStorage tracking)
- Debug logging wrapper with DEBUG constant toggle
- Proper extension icons from designed logo (16/48/128px)
- Branding assets directory (assets/branding/) with full icon set

### Changed
- Scroll behavior: messages now land near top of viewport instead of center
- Keyboard shortcuts: Ctrl+Alt+J/K for first/last (was Alt+Home/End)
- Widget load delay adapts based on first-load vs revisit
- README updated to match wtf-restarted format

### Fixed
- MutationObserver no longer blocks page rendering (debounced, subtree:false)
- Claude "Show more" button found via parent/sibling search (not just within message)
- Widget hides behind ChatGPT image viewer (Radix UI dialog detection)

## [0.1.0-alpha] - 2026-03-17

### Added
- Initial Chrome extension (Manifest V3) for ChatGPT and Claude.ai
- Floating two-row navigation widget anchored to the text input bar
- Three navigation modes: User messages, AI messages, Both
- Up/Down navigation between messages with smooth scrolling
- First/Last jump buttons to reach conversation endpoints
- Keyboard shortcuts: Alt+J/K (Vim), Alt+Up/Down, Ctrl+Alt+J/K (first/last), Alt+M (mode), Alt+H (hide)
- Visual highlight animation on navigated-to messages
- Per-site configuration with fallback selectors
- Dynamic widget positioning relative to each site's input bar
- Site-specific initial positioning (ChatGPT: 20%, Claude: 21.7%)
- Fade-in on page load (5s minimum wait for page stabilization)
- SPA-aware: handles chat switching via URL polling and debounced MutationObserver
- Versioning infrastructure adapted from wtf-restarted (sync-versions.py, git hooks)
- Playwright test for widget layout validation

[Unreleased]: https://github.com/djdarcy/aichatnav/compare/v0.2.3a1...HEAD
[0.2.3-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.2a1...v0.2.3a1
[0.2.2-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.1a1...v0.2.2a1
[0.2.1-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.0a1...v0.2.1a1
[0.2.0-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.1.0a1...v0.2.0a1
[0.1.0-alpha]: https://github.com/djdarcy/aichatnav/releases/tag/v0.1.0a1
