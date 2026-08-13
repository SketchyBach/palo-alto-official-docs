<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/uninstall-koi.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/uninstall-koi.md).

# Uninstall Koi

Removing Koi from an endpoint is straightforward. The exact steps depend on how it was originally deployed, so start by picking the path that matches your deployment.

### Agentless

The agentless script is downloaded from the deployment portal when "Agentless" is selected as the installation method.

<figure><img src="/files/nrKbGZAvbUjwCRgxUYlf" alt=""><figcaption></figcaption></figure>

The steps are the same on every operating system:

1. Open the original script you downloaded from Koi.
2. Add `--rollback` to the end of the script.
3. Run the script once.

This removes the Koi footprint and settings from the endpoint.

### Installed

The installed package is downloaded from the deployment portal when "Installed" is selected as the installation method.

<figure><img src="/files/IRSMjtDmLgBPURiwnupe" alt=""><figcaption></figcaption></figure>

Follow the steps for your operating system.

#### Windows (Service, .msi)

Uninstall through Add/Remove Programs, or run `msiexec /x` against the installer. The MSI handles the rest.

#### macOS (LaunchDaemon, .pkg)

Run the dedicated uninstall script below. It unloads the daemon, clears any launchd overrides, removes the plist and helper files, forgets the package receipts, and verifies that no Koi components are still registered.

```bash
#!/usr/bin/env bash


LABEL="koi.security.mdm"
PLIST="/Library/LaunchDaemons/${LABEL}.plist"

echo "== Stopping & unregistering =="
sudo launchctl bootout system/koi.security.mdm.plist 2>/dev/null || true
sudo launchctl bootout koi.security.mdm 2>/dev/null || true

sudo launchctl remove koi.security.mdm.plist 2>/dev/null || true
sudo launchctl remove koi.security.mdm 2> /dev/null || true

echo "== Clearing launchd disabled overrides =="
# Remove both label- and path-based override keys if present
DB="/var/db/com.apple.xpc.launchd/disabled.plist"
[ -r "$DB" ] || { echo "override DB not readable ($DB) — nothing to do"; return 0 2>/dev/null || exit 0; }

changed=0
for KEY in \
  "$LABEL" \
  "${LABEL}.plist" \
  "/Library/LaunchDaemons/${LABEL}.plist"
do
  if /usr/libexec/PlistBuddy -c "Print :$KEY" "$DB" >/dev/null 2>&1; then
    echo "Removing override: $KEY"
    sudo /usr/libexec/PlistBuddy -c "Delete :$KEY" "$DB"
    changed=1
  else
    echo "No override for: $KEY"
  fi
done

# Summary
if [ "$changed" -eq 1 ]; then
  echo "Overrides updated. Current koi entries:"
  /usr/bin/plutil -p "$DB" 2>/dev/null | /usr/bin/grep -i 'koi' || echo "none"
else
  echo "No koi overrides were present."
fi

echo "== Deleting files =="
sudo rm -f $PLIST
sudo rm -f "/Library/PrivilegedHelperTools/${LABEL}" 2>/dev/null || true
sudo rm -f /usr/local/bin/koi.security.mdm.sh
sudo rm -f /var/log/koi.security.mdm.out 
sudo rm -f /var/log/koi.security.mdm.err

echo "== Forgetting receipts (if any) =="
for id in $(/usr/sbin/pkgutil --pkgs | /usr/bin/grep -iE '(^koi\.security\.mdm$|KoiMdmManaged)'); do
  echo "  -> forgetting $id"
  /usr/sbin/pkgutil --forget "$id" >/dev/null 2>&1 || true
  /bin/rm -f "/var/db/receipts/${id}.plist" "/var/db/receipts/${id}.bom" 2>/dev/null || true
done

echo "== Verification =="
/bin/launchctl print-disabled system | /usr/bin/plutil -p - | /usr/bin/grep -i 'koi' || echo "✅ no koi overrides"
/bin/launchctl print system/"$LABEL" >/dev/null 2>&1 && echo "⚠️ still registered" || echo "✅ not registered"
/bin/test -e "$PLIST" && echo "⚠️ plist still present" || echo "🗑️ plist removed"
koi_lines="$(/bin/launchctl list 2>/dev/null | /usr/bin/grep -i 'koi' || true)"
if [ -n "$koi_lines" ]; then
  echo "$koi_lines"
  pid="$(printf '%s\n' "$koi_lines" | /usr/bin/awk 'NR==1{print $1}')"
  last="$(printf '%s\n' "$koi_lines" | /usr/bin/awk 'NR==1{print $2}')"
  if [[ "$pid" =~ ^[0-9]+$ ]]; then
    echo "⚠️ still running (pid=$pid, last_exit=$last)"
  else
    echo "⚠️ still loaded (no current pid, last_exit=$last)"
  fi
else
  echo "✅ not listed in launchctl"
fi
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/uninstall-koi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
