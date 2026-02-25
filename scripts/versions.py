import csv, requests
response = requests.get('https://endoflife.date/api/v1/products/postgresql/')
data = response.json()
releases = data["result"]["releases"]

with open('docs/data/versions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
        "Major Version",
        "Major Version Released",
        "Supported",
        "Current Minor",
        "Minor Version Released",
        "End of Support"
    ])
    for r in releases:
        writer.writerow([
            r["label"],
            r["releaseDate"],
            "N" if r["isEol"] else "Y",
            r["latest"]["name"],
            r["latest"]["date"],
            r["eolFrom"]
        ])