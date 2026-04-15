// 1. Ensure the ROI Manager is open and has boxes in it
count = roiManager("count");
if (count==0) exit("Please add some boxes to the ROI Manager first (press 'T')");

// 2. Measure total area of all boxes
roiManager("Select", Array.getSequence(count)); // Select all
roiManager("Combine");
getStatistics(totalBoxArea);

// 3. Measure whole image area
run("Select All");
getStatistics(imageArea);

// 4. Calculate ratio
totalRatio = (totalBoxArea / imageArea) * 100;

// 5. Output results
print("Number of boxes: " + count);
print("Total Boxes Area: " + totalBoxArea);
print("Full Image Area: " + imageArea);
print("Total Coverage Ratio: " + totalRatio + "%");
