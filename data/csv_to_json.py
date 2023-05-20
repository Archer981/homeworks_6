import csv
import json


def csv_to_json(csv_file, json_file, model):
    with open(csv_file, encoding='utf-8') as f:
        result = []
        for data in csv.DictReader(f):
            if 'is_published' in data:
                if data['is_published'] == 'TRUE':
                    data['is_published'] = True
                else:
                    data['is_published'] = False
            result.append({'model': model, 'fields': data})
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    csv_to_json('ads.csv', 'ads.json', 'ads.ad')
    csv_to_json('categories.csv', 'categories.json', 'ads.category')
