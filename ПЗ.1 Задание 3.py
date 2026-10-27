import json

with open("file1.json", "w", encoding="utf-8") as f:
    json.dump({
        "name": "Alice",
        "age": "25",
        "city": "Moscow"
    }, f, ensure_ascii=False)

with open("file1.json", "r", encoding="utf-8") as f:
    data1 = json.load(f)


with open("file2.json", "w", encoding="utf-8") as f:
    json.dump({
        "name": "Bob",
        "gender": "man",
    }, f, ensure_ascii=False)

with open("file2.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)


with open("target.json", "w", encoding="utf-8") as f:
    merged = data1.copy()
    merged.update(data2)

    json.dump(merged, f, ensure_ascii=False)

with open("target.json", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)