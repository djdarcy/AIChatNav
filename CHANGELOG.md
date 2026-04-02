# Changelog

All notable changes to AI ChatNav will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.3.3-alpha] - 2026-04-02

### Added
- Viewport-relative navigation: Alt+Up/Down navigates from where you're looking (#25)
- Smart detection: re-anchors to viewport when user scrolls away, then navigates
  sequentially from the detected position
- Partial visibility handling: if a message is partially scrolled off, navigates to
  show its top/bottom before moving to prev/next
- Navigation anchor setting in full options page (viewport / fixed)
- Boundary overflow: Alt+Down at N/N scrolls to absolute bottom, Alt+Up at 1/N
  scrolls to absolute top

### Fixed
- Long messages no longer block Alt+Down navigation (viewport detection checked
  element visibility instead of distance from viewport center)
- Viewport re-detection skipped when current element is still visible on screen

### Changed
- Navigation anchor dropdown moved to full options page only (popup was overflowing
  Chrome's 600px height cap)
- Default navigation anchor set to "viewport" for intuitive first-time experience

## [0.3.2-alpha] - 2026-04-01

### Added
- Ctrl+Up/Down arrow navigation (ctrlArrowNav setting, default ON)
- Non-conflicting Ctrl+arrows work alongside Alt+arrows in all keyboard modes
- Checkbox in options page and popup to disable if conflicts with other extensions

### Changed
- Popup footer condensed: "Full Settings" folded into bottom link line, eliminates scrollbar

## [0.3.1-alpha] - 2026-03-23

### Added
- Conversation follow-mode with three tracking policies (#22):
  - Follow (snaps back on new message) -- default
  - Follow (stop when navigating away)
  - Manual only (never auto-advance)
- Previous position memory: Alt+Backspace swaps between current and saved position
- Scroll to current position: Alt+G or click the counter
- Follow indicator: green down-arrow on counter when tracking conversation tail
- Position tracking settings in options page and popup
- Keyboard mode setting: Full (all shortcuts) or Minimal (Alt+Up/Down only)
- Minimal mode grays out unavailable shortcuts in popup with strikethrough
- Position history stack with undo/redo (Alt+Backspace / Ctrl+Alt+Backspace)
- Keyboard shortcuts table in popup uses two-column paired layout

### Fixed
- Follow mode prevCount captured before injectPanel() to detect message count changes
- navigateLast() no longer immediately detaches follow mode (keepFollowing parameter)
- React re-render position preservation: _lastKnownIndex prevents jumping to last message
  when DOM nodes are replaced and follow mode is off

### Changed
- Popup width increased to 340px for two-column shortcut layout
- Follow policy dropdown wording: descriptive labels without first-person pronouns
- Removed "Always follow" policy (redundant, prevented useful navigation)
- Position memory upgraded from single slot to stack with 2s grouping (rapid navigation = one entry)

## [0.3.0-alpha] - 2026-03-22

### Added
- Toolbar popup with settings, keyboard shortcut reference, and links (#13)
- Keyboard only mode: hides widget, all shortcuts still work (Alt+H toggles back)
- Progressive top/bottom navigation: repeated Ctrl+Alt+Up/Down goes deeper (#19)
  - Level 0: first/last of current mode
  - Level 1: true first/last of any type (User/AI modes only)
  - Level 2: absolute page top/bottom
  - Auto-skips redundant levels, works in all modes
- Buy Me a Coffee and scarcityhypothesis.org links in popup and options page
- "Project page" and "Report issues" links in popup footer
- Keyboard only mode setting in popup, options page, and content script

### Fixed
- Initial position defaults to last message (pages load at bottom)
- First navigation scrolls to current position instead of jumping away
- Null guard on compareDocumentPosition for race conditions
- React re-render DOM node replacement handled gracefully
- Options page spacing tightened, footer gap reduced

### Changed
- Default mode changes in popup/settings immediately update active widget
- Store listing rewritten with FAQ, how-to-use, and plain text formatting

## [0.2.4-alpha] - 2026-03-22

### Added
- World-coordinate navigation: tracks DOM elements as source of truth, not indices
- Direction-aware mode switching: Alt+Up finds previous message, Alt+Down finds next
- Approximate position indicator (~N/M) when at a message not in the current mode's set
- Widget hides when no messages exist, truly invisible (pointer-events: none)
- pushState/replaceState interception for instant SPA navigation detection

### Fixed
- Removed unused `activeTab` permission that caused Chrome Web Store rejection
- Mode switch now preserves position continuity in conversation flow (#18)
- Widget no longer flickers when switching between conversations (chat-to-chat stays visible)
- Widget no longer clips behind sidebar (hybrid fixed positioning with input bar tracking)
- Live counter updates every 1s as new messages appear during conversation (#11)
- Widget appears within ~1-2 seconds (was 5-7 seconds) matching competitor extensions (#12)

### Changed
- Permissions reduced to `storage` only (content scripts don't need activeTab)
- Navigation architecture: `state.currentElement` replaces `state.currentIndex` as source of truth
- `run_at` changed from `document_idle` to `document_end` for earlier script execution
- Removed arbitrary 5s/2s load delay -- polls immediately for input bar
- Reposition interval reduced from 3s to 1s for more responsive widget tracking
- Removed old `repositionPanel()` -- replaced by `injectPanel()` with hybrid positioning
- Options page: tighter spacing, Buy Me a Coffee button in footer
- Updated logo and added scripts/resize-icons.py for automated icon generation
- Store listing rewritten with FAQ, how-to-use, and Buy Me a Coffee link
- New main screenshot for Chrome Web Store
- Privacy policy footer: removed "open source" claim

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

[Unreleased]: https://github.com/djdarcy/aichatnav/compare/v0.3.3a1...HEAD
[0.3.3-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.3.2a1...v0.3.3a1
[0.3.2-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.3.1a1...v0.3.2a1
[0.3.1-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.3.0a1...v0.3.1a1
[0.3.0-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.4a1...v0.3.0a1
[0.2.4-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.3a1...v0.2.4a1
[0.2.3-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.2a1...v0.2.3a1
[0.2.2-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.1a1...v0.2.2a1
[0.2.1-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.2.0a1...v0.2.1a1
[0.2.0-alpha]: https://github.com/djdarcy/aichatnav/compare/v0.1.0a1...v0.2.0a1
[0.1.0-alpha]: https://github.com/djdarcy/aichatnav/releases/tag/v0.1.0a1
