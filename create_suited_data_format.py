import numpy as np
import pandas as pd

# If you have three differnt lists or files for the time, probe and data, use the following script.
time = pd.read_csv(f'/your/file/path/filename.csv') # Time delay points. 
probe = pd.read_csv(f'/your/file/path/filename.csv') # The probe axis. Use the calibration file if you have it seperate.
Z1 = pd.read_csv(f'/your/file/path/filename.csv')  # 2D data without the probe and time axis

print("Original Z1 shape:", Z1.shape)
print("Z1 data:\n", Z1)

# Step 1: Create empty result array with correct dimensions
# +1 row for header, +1 column for time values
result = np.empty((len(time) + 1, len(probe) + 1), dtype=object)

# Step 2: Add header row using slicing
# result[0:1, :] means first row, all columns
result[0:1, 0] = 0      # First row, first column = 0
result[0:1, 1:] = probe        # First row, columns 1 to end = probe values

# Step 3: Add time column using slicing
# result[1:, 0:1] means rows 1 to end, first column
result[1:, 0:1] = time[:, np.newaxis]  # Add time values to first column

# Step 4: Add Z1 data using slicing
# result[1:, 1:] means rows 1 to end, columns 1 to end
result[1:, 1:] = Z1

print("\nFinal 2D array:")
print(result)

np.savetxt(r'D:\Python\App_for_pump_probe\HoxCO_data.csv', result, delimiter=',', fmt='%s')