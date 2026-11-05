import collections
import pyscrew

# Same parameters as Paper 2 (West, Trianni & Deuse, CIE51 2024)
data = pyscrew.get_data(
    "s02",                      # scenario s02: surface friction
    handle_duplicates="first",  # remove duplicates
    handle_missings="mean",     # linear interpolation (0.0012 s steps)
    target_length=800,          # every series has length 800
    padding_value=0.0,          # shorter series: fill with zeros
    padding_position="post",    # zeros at the end
    cutoff_position="post",     # longer series: cut at the end
    cache_dir="data",           # downloaded files go into ./data
)

# 1) What does the data contain?
print("Keys:", list(data.keys()))

# 2) Torque only (as in the paper)
torque = data["torque_values"]
labels = data["class_values"]
print("Number of runs:", len(torque))          # expected: 12500
print("Length of one series:", len(torque[0])) # expected: 800

# 3) Runs per class
print("\nRuns per class:")
for cls, n in sorted(collections.Counter(labels).items()):
    print(f"  {cls}: {n}")