name = input("Enter your full name: ")
L = 0
i = 0
while i < len(name):
    if name[i] != " ":
        L = L + 1
    i = i + 1
PLI = L % 3
print("L value:", L)
print("PLI value:", PLI)
data = input("Enter weights: ").split()
weights = []
for x in data:
    weights.append(int(x))
very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []
valid = 0
for w in weights:
    if w < 0:
        invalid_entries.append(w)
    else:
        valid = valid + 1
        if w >= 0 and w <= 5:
            very_light.append(w)
        elif w >= 6 and w <= 25:
            normal_load.append(w)
        elif w >= 26 and w <= 60:
            heavy_load.append(w)
        else:
            overload.append(w)

affected = 0
if PLI == 0:
    print("Applied Rule A")
    index = 0
    while index < len(overload):
        invalid_entries.append(overload[index])
        affected = affected + 1
        index = index + 1
    overload = []
elif PLI == 1:
    print("Applied Rule B")
    affected = len(very_light)
    very_light = []
else:
    print("Applied Rule C")
    affected = len(very_light) + len(overload)
    very_light = []
    overload = []
print("Total Valid:", valid)
print("Affected Items:", affected)

print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
