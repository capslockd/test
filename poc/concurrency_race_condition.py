import concurrent.futures
import threading


thread_local = threading.local()
counter = 0


def increment_counter(fake_value):
    if not hasattr(thread_local, "counter"):
        for _ in range(100):
            thread_local.counter = 0
    thread_local.counter += 1
    print(thread_local.counter)
    print (vars(thread_local))


if __name__ == "__main__":
    fake_data = [x for x in range(100)]
    print(fake_data)
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(increment_counter, fake_data)
