// Step A: clean the image

// 1. Convert to Grayscale
run("8-bit");

// 2. Subtract Background to even out lighting
run("Subtract Background...", "rolling=50");
