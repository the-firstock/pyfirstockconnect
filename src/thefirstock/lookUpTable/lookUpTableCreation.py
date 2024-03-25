from thefirstock.commonImports.importers import *
from thefirstock.lookUpTable.private_enums import *
from thefirstock.lookUpTable.lookUpVariables import *


def process_exchange_file(exchange_file):
    with open(exchange_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Token = row['Token']
            TradingSymbol = row['TradingSymbol']
            Exchange = row['Exchange']
            lookup_table[TradingSymbol] = {"Token": Token, "Exchange": Exchange}
    return lookup_table


def create_lookup_table():
    lookUpTableList = [NSE_FILE_CSV, NFO_FILE_CSV, BFO_FILE_CSV, BSE_FILE_CSV]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_exchange_file, exchange_file) for exchange_file in lookUpTableList]

        for future in concurrent.futures.as_completed(futures):
            local_lookup_table = future.result()
            lookup_table.update(local_lookup_table)

    return lookup_table


def download_file(url, download_dir):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.basename(url)
        file_path = os.path.join(download_dir, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        return None


def extract_and_delete(file_path, extract_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    os.remove(file_path)


def delete_folder_if_exists(folder_path):
    if os.path.exists(folder_path):
        try:
            os.rmdir(folder_path)
        except OSError as e:
            print("Error deleting folder:", e)


def main():
    file_urls = [NSE_FILE, NFO_FILE, BSE_FILE, BFO_FILE]

    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)

    extract_dir = 'downloads'
    os.makedirs(extract_dir, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        downloaded_files = list(executor.map(download_file, file_urls, [download_dir] * len(file_urls)))

        for file_path in downloaded_files:
            if file_path:
                executor.submit(extract_and_delete, file_path, extract_dir)

    lookup_table = create_lookup_table()
    shutil.rmtree('downloads')

    return lookup_table
