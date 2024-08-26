import csv
import json

def process_csv(file_path):
    results = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Strip whitespace from all fields
            processed_row = {key: value.strip() for key, value in row.items()}
            
            if 'sizes' in processed_row:
                processed_row['sizes'] = [keyword.strip() for keyword in processed_row['sizes'].split(',')]
            if 'images' in processed_row:
                processed_row['images'] = [keyword.strip() for keyword in processed_row['images'].split(',')]
            if 'categories' in processed_row:
                processed_row['categories'] = [keyword.strip() for keyword in processed_row['categories'].split(',')]
            
            results.append(processed_row)
    
    return results

def main():
    csv_file_path = 'Rivo frames.csv'
    output_file_path = 'processed_data.json'
    
    data = process_csv(csv_file_path)
    
    with open(output_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

    print(f"Processed data saved to {output_file_path}")

if __name__ == "__main__":
    main()
