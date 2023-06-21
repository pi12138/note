from concurrent import futures

from flags import save_photo, get_photo, main, Photos


MAX_WORKERS = 20


def download_one(photo):
    image = get_photo(photo)
    save_photo(image, photo)
    

def download_many(photo_list):
    workers = min(MAX_WORKERS, len(photo_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(photo_list))
    
    return len(list(res))


if __name__ == "__main__":
    main(download_many)