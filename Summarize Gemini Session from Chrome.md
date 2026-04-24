Object: to summarize Q-A insights from Chrome and export it to Obsidian


# Filter out all relavent pages form Chrome
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

# Ask Claude or Chatgpt to summarize
use the following template:
1. copy link one by one
2. customize with the following commands:
	1. 
	a. summarize the link into a markdown file by
		<ol>explain the problem intuitively</ol>
		
		
		explain it rigorously
		1. explain with examples and code