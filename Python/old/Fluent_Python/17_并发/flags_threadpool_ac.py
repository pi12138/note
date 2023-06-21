from concurrent import futures

from flags import save_photo, get_photo, main, Photos


MAX_WORKERS = 20


def download_one(photo):
    image = get_photo(photo)
    save_photo(image, photo)
    

def download_many(photo_list):
    photo_list = photo_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for photo in sorted(photo_list):
            future = executor.submit(download_one, photo)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(photo, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == "__main__":
    main(download_many)