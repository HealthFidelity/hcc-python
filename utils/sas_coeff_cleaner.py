
fname_in = "/Users/rituraj_tiwari/Documents/Development/hcc-python/utils/V22_17_Coefficient.csv"
fname_out = "/Users/rituraj_tiwari/Documents/Development/hcc-python/utils/V22_17_Coefficient_cleaned.csv"

with open(fname_in, "rt") as infile:
    row1 = infile.readline()
    row2 = infile.readline()
    names = [x.strip() for x in row1.split(",")]
    values = [x.strip() for x in row2.split(",")]
    pairs = zip(names, values)

    with open(fname_out, "wt") as outfile:
        for pair in pairs:
            outfile.write(pair[0] + "," + pair[1] + "\n")

