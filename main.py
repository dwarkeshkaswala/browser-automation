from utils import create_chrome_browser
import threading

def get_data():
    # for x in range(0, 10):
    browser = create_chrome_browser(headless=False, preserve_browser=True)
    url = "https://nft.dcuniverse.com/api/v1/public/catalog?catalogObjectType=TOKEN&page=1&size=30&filter=forSale=true&filter=asset.id=7c19fb16-8cf3-49b1-9e37-754d3a9e9734&sort=sale.price.amount,asc"
    browser.get(url)
    # print(browser.title)
    # browser.quit()

def makeThreads():
    all_threads = []
    
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))
    all_threads.append(threading.Thread(target=get_data))


    return all_threads

def executeThreading(all_threads):
    for thread in all_threads:
        thread.start()

    for thread in all_threads:
        thread.join()


if __name__ == "__main__":
    all_threads = makeThreads()
    executeThreading(all_threads)

    print("Done")