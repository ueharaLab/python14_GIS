import json

with open('tokyo23.json','r', encoding="utf-8_sig") as f:
    d = json.load(f)

features = d['features']
# idリスト
ids = sorted(set([d['properties']['N03_007'] for d in features]))
new_features = []
for id in ids:
    data = [d['geometry']['coordinates'] for d in features if d['properties']['N03_007']==id]
    if len(data) == 1:
        feature = dict(
            type = "Feature",
            geometry = dict(
                type = "MultiPolygon",
                coordinates = data[0],
            ),
            id = id,
        )
    
    else:
        feature = dict(
            type = "Feature",
            geometry = dict(
                type = "MultiPolygon",
                coordinates = data,
            ),
            id = id,
        )
    
    new_features.append(feature)
d['features'] = new_features

with open('new_tokyo23.json', 'w') as f:
    json.dump(d, f)