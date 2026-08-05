# How to Convert JSON to CSV Using Python (Pandas)

## Prerequisites

Make sure Python is installed on your computer.

Install **pandas** if you haven't already:

``` bash
pip install pandas
```

------------------------------------------------------------------------

## Step 1: Save Your JSON File

Save your API response or JSON data as a file, for example:

    response.json

Example JSON:

``` json
[
    {
        "hostname": "R1",
        "ip": "192.168.1.1",
        "status": "up"
    },
    {
        "hostname": "R2",
        "ip": "192.168.1.2",
        "status": "down"
    }
]
```

------------------------------------------------------------------------

## Step 2: Create a Python Script

Create a new file named:

    json_to_csv.py

Add the following code:

``` python
import json
import pandas as pd

with open("response.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.json_normalize(data)
df.to_csv("response.csv", index=False)

print("CSV file created successfully!")
```

------------------------------------------------------------------------

## Step 3: Run the Script

``` bash
python json_to_csv.py
```

------------------------------------------------------------------------

## Step 4: Verify the Output

A new file named `response.csv` will be created.

  hostname   ip            status
  ---------- ------------- --------
  R1         192.168.1.1   up
  R2         192.168.1.2   down

------------------------------------------------------------------------

## Working with Nested JSON

`pd.json_normalize()` automatically flattens nested JSON.

Example:

``` json
[
    {
        "hostname": "R1",
        "location": {
            "building": "HQ",
            "floor": 3
        }
    }
]
```

Output:

  hostname   location.building   location.floor
  ---------- ------------------- ----------------
  R1         HQ                  3

------------------------------------------------------------------------

## If the JSON Is Inside a Key

``` json
{
    "response": [
        {
            "hostname": "R1",
            "ip": "192.168.1.1"
        },
        {
            "hostname": "R2",
            "ip": "192.168.1.2"
        }
    ]
}
```

Change:

``` python
df = pd.json_normalize(data)
```

to:

``` python
df = pd.json_normalize(data["response"])
```

------------------------------------------------------------------------

## Summary

1.  Install pandas.
2.  Save your JSON data to a file.
3.  Load the JSON with `json.load()`.
4.  Convert it to a DataFrame using `pd.json_normalize()`.
5.  Export the DataFrame to CSV using `df.to_csv()`.

That's it! You can now convert most JSON API responses into CSV files
with just a few lines of Python.
