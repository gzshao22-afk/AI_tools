![](file-20260212113624473.png)
Manual for pgfplots
https://www.iro.umontreal.ca/~simardr/pgfplots.pdf

```tex
% Preamble: \pgfplotsset{width=7cm,compat=1.3} 
\begin{tikzpicture} 
\begin{axis}[view={60}{30}] 
\addplot3+[domain=0:5*pi,samples=60,samples y=0] ({sin(deg(x))}, {cos(deg(x))}, {2*x/(5*pi)}); 
\end{axis} 
\end{tikzpicture}
```
