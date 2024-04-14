#!/usr/bin/env python3

datadbnew = b""
data0new = b""
data1new = b""
data2new = b""
datadbold = b""
data0old = b""
data1old = b""
data2old = b""

# new
with open("fixtures/new/1", "rb") as f:
    data1new = f.read()

with open("fixtures/new/2", "rb") as f:
    data2new = f.read()

with open("fixtures/new/0", "rb") as f:
    data0new = f.read()

with open("fixtures/new/dirf.db", "rb") as f:
    datadbnew = f.read()

# old
with open("fixtures/old/1", "rb") as f:
    data1old = f.read()

with open("fixtures/old/2", "rb") as f:
    data2old = f.read()

with open("fixtures/old/0", "rb") as f:
    data0old = f.read()

with open("fixtures/old/dirf.db", "rb") as f:
    datadbold = f.read()

for i, b in enumerate(datadbold):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data0old):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data1old):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data2old):
    if b == 0:
        print(i)
        break

# as the 0 file starts with zeros it could be interesting where those zeros end
for i, b in enumerate(data0old):
    if b != 0:
        print(i)
        break

for i, b in enumerate(datadbnew):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data0new):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data1new):
    if b == 0:
        print(i)
        break

for i, b in enumerate(data2new):
    if b == 0:
        print(i)
        break

# as the 0 file starts with zeros it could be interesting where those zeros end
for i, b in enumerate(data0new):
    if b != 0:
        print(i)
        break
