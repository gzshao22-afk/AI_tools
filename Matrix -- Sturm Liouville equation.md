
### Variation of Parameters Formula
The variation of parameters formula provides a systematic way to find a

**particular solution** ($y_p$) for non-homogeneous linear differential equations. It is more general than other methods because it works for any forcing function 𝑔(𝑥), provided you can perform the required integration. 

**The Standard Formula (Second Order)** 

For a second-order differential equation in **standard form**:  
$$y^{′′}+p(x)y^{′}+q(x)y=g(x)$$
double prime plus p open paren x close paren y prime plus q open paren x close paren y equals g of x

𝑦′′+𝑝(𝑥)𝑦′+𝑞(𝑥)𝑦=𝑔(𝑥)

If

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

y1y sub 1

𝑦1

and

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

y2y sub 2

𝑦2

are linearly independent solutions to the homogeneous equation, the particular solution is given by:  

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

yp(x)=u1(x)y1(x)+u2(x)y2(x)y sub p open paren x close paren equals u sub 1 open paren x close paren y sub 1 open paren x close paren plus u sub 2 open paren x close paren y sub 2 open paren x close paren

𝑦𝑝(𝑥)=𝑢1(𝑥)𝑦1(𝑥)+𝑢2(𝑥)𝑦2(𝑥)

Where the "parameters"

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

u1u sub 1

𝑢1

and

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

u2u sub 2

𝑢2

are calculated as: 

- **
    
    ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    u1(x)=∫−y2⋅g(x)W(y1,y2)dxu sub 1 open paren x close paren equals integral of the fraction with numerator negative y sub 2 center dot g of x and denominator cap W open paren y sub 1 comma y sub 2 close paren end-fraction space d x
    
    𝑢1(𝑥)=−𝑦2⋅𝑔(𝑥)𝑊(𝑦1,𝑦2)𝑑𝑥
    
    **
- **
    
    ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    u2(x)=∫y1⋅g(x)W(y1,y2)dxu sub 2 open paren x close paren equals integral of the fraction with numerator y sub 1 center dot g of x and denominator cap W open paren y sub 1 comma y sub 2 close paren end-fraction space d x
    
    𝑢2(𝑥)=𝑦1⋅𝑔(𝑥)𝑊(𝑦1,𝑦2)𝑑𝑥
    
    **

The term**

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

W(y1,y2)cap W open paren y sub 1 comma y sub 2 close paren

𝑊(𝑦1,𝑦2)

**is the Wronskian, defined as the determinant:  

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

W=y1y2′−y2y1′cap W equals y sub 1 y sub 2 prime minus y sub 2 y sub 1 prime

𝑊=𝑦1𝑦′2−𝑦2𝑦′1

**General Formula for

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

nn

𝑛

-th Order** 

For higher-order equations, the formula generalizes using a system of linear equations. A particular solution for an

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

nn

𝑛

-th order equation is:  

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

yp(x)=∑i=1nui(x)yi(x)y sub p open paren x close paren equals sum from i equals 1 to n of u sub i open paren x close paren y sub i open paren x close paren

𝑦𝑝(𝑥)=𝑛𝑖=1𝑢𝑖(𝑥)𝑦𝑖(𝑥)

The derivatives of these functions,

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

ui′u sub i prime

𝑢′𝑖

, are found by solving the following matrix equation:  

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

[y1y2…yny1′y2′…yn′⋮⋮⋱⋮y1(n−1)y2(n−1)…yn(n−1)][u1′u2′⋮un′]=[00⋮g(x)]the 4 by 4 matrix; Row 1: Column 1: y sub 1, Column 2: y sub 2, Column 3: …, Column 4: y sub n; Row 2: Column 1: y sub 1 prime, Column 2: y sub 2 prime, Column 3: …, Column 4: y sub n prime; Row 3: Column 1: ⋮, Column 2: ⋮, Column 3: ⋱, Column 4: ⋮; Row 4: Column 1: y sub 1 raised to the open paren n minus 1 close paren power, Column 2: y sub 2 raised to the open paren n minus 1 close paren power, Column 3: …, Column 4: y sub n raised to the open paren n minus 1 close paren power end-matrix; the 4 by 1 column matrix; Row 1: u sub 1 prime, Row 2: u sub 2 prime, Row 3: ⋮, Row 4: u sub n prime end-matrix; equals the 4 by 1 column matrix; Row 1: 0, Row 2: 0, Row 3: ⋮, Row 4: g of x end-matrix;

⎣⎢⎢⎢⎡𝑦1𝑦2…𝑦𝑛𝑦′1𝑦′2…𝑦′𝑛⋮⋮⋱⋮𝑦(𝑛−1)1𝑦(𝑛−1)2…𝑦(𝑛−1)𝑛⎦⎥⎥⎥⎤⎣⎢⎢⎢⎡𝑢′1𝑢′2⋮𝑢′𝑛⎦⎥⎥⎥⎤=⎣⎢⎢⎢⎡00⋮𝑔(𝑥)⎦⎥⎥⎥⎤

**Key Requirements** 

- **Standard Form:** You **must** divide the entire equation by the lead coefficient so that
    
    ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    y(n)y raised to the open paren n close paren power
    
    𝑦(𝑛)
    
    has a coefficient of 1 before applying these formulas.
- **Homogeneous Solutions:** You must already know the fundamental set of solutions (
    
    ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    y1,y2,…y sub 1 comma y sub 2 comma …
    
    𝑦1,𝑦2,…
    
    ) for the related homogeneous equation.
- **Integration:** The final step always requires integrating the expressions for
    
    ![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)
    
    ui′u sub i prime
    
    𝑢′𝑖
    
    . If the integrals are non-elementary, you may have to leave the solution in integral form. 

Would you like to walk through a **specific example** like

![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

y′′+y=tan(x)y double prime plus y equals tangent x

𝑦′′+𝑦=tan(𝑥)

to see these formulas in action?