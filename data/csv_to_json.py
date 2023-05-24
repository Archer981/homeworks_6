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
            if 'location_id' in data:
                data['locations'] = [data['location_id']]
                del data['location_id']
            result.append({'model': model, 'fields': data})
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    csv_to_json('ad.csv', 'ad.json', 'ads.ad')
    csv_to_json('category.csv', 'category.json', 'ads.category')
    csv_to_json('user.csv', 'user.json', 'users.user')
    csv_to_json('location.csv', 'location.json', 'users.location')
