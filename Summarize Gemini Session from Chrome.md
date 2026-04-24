Object: to summarize Q-A insights from Chrome and export it to Obsidian

1. **Open the Inspector Page**: Type `chrome://inspect/#pages` into your Chrome address bar and press **Enter**.
2. **Open Developer Tools**: Press `F12` (or `Ctrl+Shift+I`) to open the Developer Tools panel on this page.
3. **Run the Filter Script**: Click on the **Console** tab at the top of the Developer Tools panel, paste the following code, and press **Enter**:
```javascript
const links = Array.from(document.querySelectorAll('#pages-list .row .url'))
  .map(a => a.innerText)
  .filter(url => url.includes("gemini.google.com"));
copy(links.join('\n'));
console.log("Copied " + links.length + " links to clipboard.");
```

