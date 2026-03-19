# ROADMAP - AI ChatNav

Tracking milestones and planned features for AI ChatNav.
See also: [GitHub Issue #1](https://github.com/djdarcy/aichatnav/issues/1) (canonical, kept up to date)

## v0.1.0 - Core Navigation
- [x] Project scaffolding (RepoKit)
- [x] Manifest V3 extension structure
- [x] Content script with config-driven site selectors
- [x] Floating two-row UI panel (first/up/down/last, mode toggle, counter)
- [x] Keyboard shortcuts (Alt+J/K, Alt+Up/Down, Ctrl+Alt+J/K first/last, Alt+M, Alt+H)
- [x] Three modes: User / AI / Both
- [x] Highlight animation on navigated-to message
- [x] SPA navigation detection (URL polling + debounced MutationObserver)
- [x] Dynamic widget positioning anchored to text input bar
- [x] Per-site positioning config (initialLeft, nudgeX)
- [x] Fade-in on page load (5s stabilization wait)
- [x] Versioning scripts adapted from wtf-restarted
- [x] Playwright layout tests
- [x] Real-world testing on ChatGPT and Claude.ai
- [x] Initial commit

## v0.2.0 - Polish & Settings (current)
- [x] Settings/options page (chrome.storage.local)
- [x] Site-matching color themes (Dark / Light / Auto-detect)
- [x] Options page theme fades smoothly on change
- [x] Auto-expand "show more" on Claude.ai (opt-in, sibling button search)
- [x] Alt+O expand/collapse current, Ctrl+Alt+O toggle auto-expand
- [x] Expand/collapse all button on widget panel
- [x] Overlay/modal detection (widget hides behind image viewers)
- [x] Proper extension icons from designed logo
- [x] Default mode preference setting
- [x] Scroll positioning near top of viewport (8%)
- [x] Faster revisit load (2s vs 5s via sessionStorage)
- [x] README update (match wtf-restarted format)
- [ ] Refine Claude.ai AI message selectors
- [ ] Handle streaming responses gracefully
- [ ] Edge case handling (single message, conversation branches)
- [ ] README screenshots (deferred until light theme is polished)

## v0.3.0 - Platform Expansion
- [ ] Gemini (gemini.google.com) support
- [ ] Relative vs Absolute navigation mode (Ctrl+Alt+M toggle) (#3)
- [ ] Draggable panel position
- [ ] Position persistence across page reloads
- [ ] Keyboard shortcut customization

## v0.4.0 - Responsive UI
- [ ] Progressive widget layouts: Micro / Mini / Compact / Full tiers (#4)
- [ ] Mini tier: customizable 3rd button (mode, expand, close, counter, none)
- [ ] Orientation options: horizontal or vertical (Mini tier)
- [ ] Auto-sizing based on available space (stretch goal)

## v0.5.0 - Cross-Browser
- [ ] Firefox support (browser_specific_settings.gecko.id)
- [ ] Test on Edge, Brave, Opera
- [ ] Firefox Add-ons submission

## v0.5.0 - Store Release
- [ ] Professional icons and screenshots
- [ ] Privacy policy page
- [ ] Chrome Web Store submission ($5 dev fee)
- [ ] Edge Add-ons listing

## v1.0.0 - Stable
- [ ] 3+ supported AI chat platforms
- [ ] Automated E2E tests (Playwright)
- [ ] Stable selectors with fallback chains
- [ ] User-reported bug fixes
