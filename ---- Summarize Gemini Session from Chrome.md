Object: to summarize Q-A insights from Chrome and export it to Obsidian


# Filter out all relevant pages form Chrome
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
	1. summarize the link into a markdown file by:
		1. Explaining the question intuitively
		2. Explaining it rigorously
		3. Explaining with examples and code
		4. using a "Question template"



## Question templates:
### Example template 1:

[https://gemini.google.com/app/041217ccc47acadc](https://gemini.google.com/app/041217ccc47acadc) Summarize this link in a markdown file: start from explaining refractive index, real part and imaginary part and their meaning, then explain how reflectivity and the phase shift can be used with the Fresnel equations to solve for refractive index; then introduce Kramers-Kronig analysis and how it is used to obtain refractive index and how is Cauchy's Integral Theorem is used



### Example template 2:

[https://www.google.com/search?q=does+FTIR+measure+reflectivity+over+different+wavelength&rlz=1C1HKFL_enUS1197US1197&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRiPAtIBCTEzMDMyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3u6MWRtAr31GIrXLfiKhJJ8rW39M0T_N8wn3kINg3nQk-dwTV6GiRqsz_UCAHf8NRTFqbzB1rE_rNy-EgYhhPtVeLTImvKNA9ZTBb3msotXE1Nv_O_ZT2gvG7Axu4TJaZa2_RUXzCsVYaOgh9vaXo94uGCjbSjTCGdSX6W9lXfVsxOGx5w&ved=2ahUKEwjzjqjZpoSUAxX-HzQIHeQZAAgQ0NsOegQIAxAB&aep=10&ntc=1&mstk=AUtExfBMEHnlvEqHSH1gmiDqqBqldkWrRh5CWGekmE9B8m_I0LOJXjyclJlgt5CKH7I5AP6jFrT1nWa4sPqNfgWfwV14gVo8TtNY2sPJ66E-jqEQghZfXUlVb_HG3LwXA5tndCO-wJISRzIkaiEZugKo7Y2EcZoMhFRyCdrLvlr0ffkX3TM_UEEbPj-hY2RZ-v-ASV4Hz7HgXTwMh5e6QuKT5PxX0VXimFqGlZQpLc-B67Vxytx-yLHWNZel2RAD8j60_4AfFrOjViVV5Q&csuir=1&mtid=po_qaZTnAfmk0PEPh5HbkAc&udm=50](https://www.google.com/search?q=does+FTIR+measure+reflectivity+over+different+wavelength&rlz=1C1HKFL_enUS1197US1197&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRiPAtIBCTEzMDMyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3u6MWRtAr31GIrXLfiKhJJ8rW39M0T_N8wn3kINg3nQk-dwTV6GiRqsz_UCAHf8NRTFqbzB1rE_rNy-EgYhhPtVeLTImvKNA9ZTBb3msotXE1Nv_O_ZT2gvG7Axu4TJaZa2_RUXzCsVYaOgh9vaXo94uGCjbSjTCGdSX6W9lXfVsxOGx5w&ved=2ahUKEwjzjqjZpoSUAxX-HzQIHeQZAAgQ0NsOegQIAxAB&aep=10&ntc=1&mstk=AUtExfBMEHnlvEqHSH1gmiDqqBqldkWrRh5CWGekmE9B8m_I0LOJXjyclJlgt5CKH7I5AP6jFrT1nWa4sPqNfgWfwV14gVo8TtNY2sPJ66E-jqEQghZfXUlVb_HG3LwXA5tndCO-wJISRzIkaiEZugKo7Y2EcZoMhFRyCdrLvlr0ffkX3TM_UEEbPj-hY2RZ-v-ASV4Hz7HgXTwMh5e6QuKT5PxX0VXimFqGlZQpLc-B67Vxytx-yLHWNZel2RAD8j60_4AfFrOjViVV5Q&csuir=1&mtid=po_qaZTnAfmk0PEPh5HbkAc&udm=50)

Summarize the link in a markdown file. First, explain what are the methods to obtain refractive index, include Becke line method (how it works) and K-K method, in the K-K method, what are the requirements on the sample, does it need to be smooth or not; then explain Goodness of Fit method, what is each row and column of the matrix, what is the x vector, how the calculated scattering patterns is used to obtain residual error and how the residual error is used to update refractive index, then how the updated refractive index is used to update the matrix using Mie theory


### Example template 3:

[https://www.google.com/search?q=Cauchy%E2%80%99s+Integral+Theorem+explain&rlz=1C1HKFL_enUS1197US1197&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMgcIAxAAGO8FMgcIBBAAGO8F0gEIMzI5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpmAsnXCN5UBx17opt8eaTX5ijYCyJdSZFM4mewRGuivaHuHursf-soOk0JbfkgzOIi1ZPsNSh18l54qW-c2NyuZMG8y16go9KUfTULPqJXVMTxktxMC8Z9TCTzz6aCPq5dwX-SehOfBM0TrbQyNJAW9CHlgcb_CYJG4Dq23HuLy7BrhI3zs_AY7GIzFa_-B-jzhTi3g&ved=2ahUKEwjrh93ajoSUAxWEle4BHakUGpUQ0NsOegQIAxAB&aep=10&ntc=1&mstk=AUtExfCmE_xk8yFyRl2pLdUvL0rRAVRtgRWSoIuu-oLlJNisPEeqcDiFk6aA74fwtw9KyqrNejto4aZWI-Vv7ZyOifxa7qrxaolc9T8R2U9KFB2Q3DELiiHFDap2xeKA_bQ0TDjw4LU2NdrlYZFoIZjQKeMOvcLO8wirr4h5FiajPS4C_QeVQcm-1G71UC_95jT8IMhRrMgce3T0Rvg3NoMGdGQXhQsuQNXY4c3OjTT53gXpvk-xsbISsj11-vb7b9eZx92DwnIbUogsL4ZTV0aaejWjgMMjikMI7Q7UNCmZB5gN9o5Qus85SY4jhMRRBO9QfzJJ7KwLE0tS_Wfh5yHBqpkEbMJgMVZ3WHFzOx23gQXU2ZRnSC2XnGM&csuir=1&mtid=gCPqabjqJ6KNur8Pq56S2As&udm=50](https://www.google.com/search?q=Cauchy%E2%80%99s+Integral+Theorem+explain&rlz=1C1HKFL_enUS1197US1197&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMgcIAxAAGO8FMgcIBBAAGO8F0gEIMzI5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpmAsnXCN5UBx17opt8eaTX5ijYCyJdSZFM4mewRGuivaHuHursf-soOk0JbfkgzOIi1ZPsNSh18l54qW-c2NyuZMG8y16go9KUfTULPqJXVMTxktxMC8Z9TCTzz6aCPq5dwX-SehOfBM0TrbQyNJAW9CHlgcb_CYJG4Dq23HuLy7BrhI3zs_AY7GIzFa_-B-jzhTi3g&ved=2ahUKEwjrh93ajoSUAxWEle4BHakUGpUQ0NsOegQIAxAB&aep=10&ntc=1&mstk=AUtExfCmE_xk8yFyRl2pLdUvL0rRAVRtgRWSoIuu-oLlJNisPEeqcDiFk6aA74fwtw9KyqrNejto4aZWI-Vv7ZyOifxa7qrxaolc9T8R2U9KFB2Q3DELiiHFDap2xeKA_bQ0TDjw4LU2NdrlYZFoIZjQKeMOvcLO8wirr4h5FiajPS4C_QeVQcm-1G71UC_95jT8IMhRrMgce3T0Rvg3NoMGdGQXhQsuQNXY4c3OjTT53gXpvk-xsbISsj11-vb7b9eZx92DwnIbUogsL4ZTV0aaejWjgMMjikMI7Q7UNCmZB5gN9o5Qus85SY4jhMRRBO9QfzJJ7KwLE0tS_Wfh5yHBqpkEbMJgMVZ3WHFzOx23gQXU2ZRnSC2XnGM&csuir=1&mtid=gCPqabjqJ6KNur8Pq56S2As&udm=50)

summarize this link in a markdown file: start from Green's theorem, explaining the intuitively, then rigorous deduction, end with examples calculating area and vector field applying Green's theorem; then derive cauchy's Integral Theorem from green's theorem

### Example template 4:

[https://www.google.com/search?q=elisa+data+fitting+example&sca_esv=58faf45c7c4dd337&rlz=1C1HKFL_enUS1197US1197&sxsrf=ANbL-n5RlKJZ_WSillIPgg7M1RgUb5ncOw%3A1776963318387&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3p-ML-906rRL_m6h4jR-tdCH-vUIlZq9RzugLEcfjf51b4dfDKizXS4hTwRCZW2TydVcnv1RUVx0SX0axPgL6aA1y5lH4oIQTHc9n3as9K40uq1ucVlSq7hphXixGrVbAHaxl4xbaQRNq-TBoJwkyHSzWgD1m8zRB8KZ0lvZ8gcgw8mFAQ&aep=1&ntc=1&sa=X&ved=2ahUKEwig_vuauISUAxXRyOYEHXWABMAQ2J8OegQIDRAI&biw=1404&bih=674&dpr=1.37&mstk=AUtExfA5WHj4QIdfTNa50cqKVdvSbmPR4PVw1dSrmmyx7-GZpqDlWkD0LoJP52H5fFpfr51UDB74RAVjnBPTASrLP0Q2r9_sXiLEpiYytbbN2Ox4JyjJG6F1oBa4ZuPQKbFZLBJAHN7HsoIcK6bxh6kRl3X6SOXcOicXWE7c_zyj1y9OBYAPakizKjBGaCnTlfkQ9N56AvHnPpgtVAxp1OC7669vkLVP7zG6XklWdqLX3EXeO6RIqz6QK5RBQbsW7HVV0gO-zrK-NVTdSYQB1RBCUwNLdhl2-hbX_t7xPwgwyNu5riv8zc2FcFfe9EzTGMMhHZOUXQDQ0snOtwnQkgKx7yCGt4sHOUvriQ&csuir=1&mtid=-U7qab3jL-Hw0PEPmaWysAw&udm=50](https://www.google.com/search?q=elisa+data+fitting+example&sca_esv=58faf45c7c4dd337&rlz=1C1HKFL_enUS1197US1197&sxsrf=ANbL-n5RlKJZ_WSillIPgg7M1RgUb5ncOw%3A1776963318387&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3p-ML-906rRL_m6h4jR-tdCH-vUIlZq9RzugLEcfjf51b4dfDKizXS4hTwRCZW2TydVcnv1RUVx0SX0axPgL6aA1y5lH4oIQTHc9n3as9K40uq1ucVlSq7hphXixGrVbAHaxl4xbaQRNq-TBoJwkyHSzWgD1m8zRB8KZ0lvZ8gcgw8mFAQ&aep=1&ntc=1&sa=X&ved=2ahUKEwig_vuauISUAxXRyOYEHXWABMAQ2J8OegQIDRAI&biw=1404&bih=674&dpr=1.37&mstk=AUtExfA5WHj4QIdfTNa50cqKVdvSbmPR4PVw1dSrmmyx7-GZpqDlWkD0LoJP52H5fFpfr51UDB74RAVjnBPTASrLP0Q2r9_sXiLEpiYytbbN2Ox4JyjJG6F1oBa4ZuPQKbFZLBJAHN7HsoIcK6bxh6kRl3X6SOXcOicXWE7c_zyj1y9OBYAPakizKjBGaCnTlfkQ9N56AvHnPpgtVAxp1OC7669vkLVP7zG6XklWdqLX3EXeO6RIqz6QK5RBQbsW7HVV0gO-zrK-NVTdSYQB1RBCUwNLdhl2-hbX_t7xPwgwyNu5riv8zc2FcFfe9EzTGMMhHZOUXQDQ0snOtwnQkgKx7yCGt4sHOUvriQ&csuir=1&mtid=-U7qab3jL-Hw0PEPmaWysAw&udm=50)

write a markdown document explaining the curve fitting process based on contents in this link, emphasize on the reason for choosing 4PL, how it is implemented to ease the computation; then summarize key parameters like R^2 value, CV, and LLoQ; finally, include an example R code for tutorial