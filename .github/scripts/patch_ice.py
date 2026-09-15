from pathlib import Path

p = Path("Ice-src/Ice/MenuBar/ControlItem/ControlItem.swift")
s = p.read_text()


def replace_once(old: str, new: str) -> None:
    global s
    count = s.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one anchor, found {count}: {old[:120]!r}")
    s = s.replace(old, new, 1)


replace_once(
    "    /// The control item's underlying status item.\n"
    "    private let statusItem: NSStatusItem\n\n"
    "    /// A horizontal constraint for the control item's content view.\n",
    "    /// The control item's underlying status item.\n"
    "    private let statusItem: NSStatusItem\n\n"
    "    /// Extra invisible status items used on macOS 27 to push hidden\n"
    "    /// sections fully out of the visible status region.\n"
    "    private var spacerItems = [NSStatusItem]()\n\n"
    "    /// A horizontal constraint for the control item's content view.\n",
)

replace_once(
    "    /// Removes the status item without clearing its stored position.\n"
    "    deinit {\n"
    "        // Removing the status item has the unwanted side effect of deleting\n",
    "    /// Removes the status item without clearing its stored position.\n"
    "    deinit {\n"
    "        for item in spacerItems {\n"
    "            NSStatusBar.system.removeStatusItem(item)\n"
    "        }\n\n"
    "        // Removing the status item has the unwanted side effect of deleting\n",
)

replace_once(
    "                    }\n"
    "                    constraint?.isActive = true\n"
    "                } else {\n"
    "                    statusItem.length = 0\n",
    "                    }\n\n"
    "                    let shouldUseSpacers = section.name != .visible && state == .hideItems\n"
    "                    updateSpacerItems(forHiddenState: shouldUseSpacers)\n\n"
    "                    constraint?.isActive = true\n"
    "                } else {\n"
    "                    updateSpacerItems(forHiddenState: false)\n"
    "                    statusItem.length = 0\n",
)

replace_once(
    "        if let appState {\n"
    "            appState.settingsManager.generalSettingsManager.$showIceIcon\n",
    "        NotificationCenter.default\n"
    "            .publisher(for: NSApplication.didChangeScreenParametersNotification)\n"
    "            .receive(on: DispatchQueue.main)\n"
    "            .sink { [weak self] _ in\n"
    "                guard\n"
    "                    let self,\n"
    "                    isSectionDivider,\n"
    "                    isAddedToMenuBar,\n"
    "                    isVisible,\n"
    "                    state == .hideItems\n"
    "                else {\n"
    "                    return\n"
    "                }\n"
    "                statusItem.length = expandedHidingLength()\n"
    "                updateSpacerItems(forHiddenState: true)\n"
    "            }\n"
    "            .store(in: &c)\n\n"
    "        if let appState {\n"
    "            appState.settingsManager.generalSettingsManager.$showIceIcon\n",
)

methods = r'''    /// Adds or removes additional hiding spacers on macOS 27.
    private func updateSpacerItems(forHiddenState isHiddenState: Bool) {
        guard
            #available(macOS 27, *),
            identifier != .iceIcon,
            isHiddenState
        else {
            removeSpacerItems()
            return
        }

        let spacerLength = expandedHidingLength()
        guard spacerLength.isFinite, spacerLength > 0 else {
            removeSpacerItems()
            return
        }

        let needed = requiredSpacerCount(for: spacerLength)

        if spacerItems.count != needed {
            removeSpacerItems()

            spacerItems = (0 ..< needed).map { index in
                // Seed with a tiny non-zero width so AppKit materializes a
                // real status-item window before the final width is applied.
                let item = NSStatusBar.system.statusItem(withLength: 1)
                item.autosaveName = "\(identifier.rawValue).macOS27Spacer.\(index)"

                if let button = item.button {
                    button.title = ""
                    button.image = nil
                    button.isEnabled = false
                    button.appearsDisabled = true
                    button.alphaValue = 0
                }

                return item
            }
        }

        spacerItems.forEach { $0.length = spacerLength }
    }

    /// Removes all additional hiding spacers.
    private func removeSpacerItems() {
        for item in spacerItems {
            NSStatusBar.system.removeStatusItem(item)
        }
        spacerItems.removeAll()
    }

    /// Calculates how many additional macOS 27 spacers are needed.
    private func requiredSpacerCount(for spacerLength: CGFloat) -> Int {
        let maxScreenWidth = NSScreen.screens.map(\.frame.width).max()
            ?? window?.screen?.frame.width
            ?? 0

        guard maxScreenWidth > 0 else {
            return 0
        }

        let desiredWidth = max(maxScreenWidth * 3, spacerLength)
        let remainingWidth = desiredWidth - spacerLength
        guard remainingWidth > 0 else {
            return 0
        }

        return min(32, Int(ceil(remainingWidth / spacerLength)))
    }

'''

replace_once(
    "    /// Performs the control item's action.\n"
    "    @objc private func performAction() {\n",
    methods
    + "    /// Performs the control item's action.\n"
    + "    @objc private func performAction() {\n",
)

p.write_text(s)
print(f"Patched {p}")
