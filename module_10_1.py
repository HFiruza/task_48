import time
import threading
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as f:
        for i in range(1, word_count + 1):
            text = f"Какое-то слово № {i}\n"
            time.sleep(0.1)
            f.write(text)
    print(f"Завершилась запись в файл {file_name}")

start_time = datetime.now()
word_count = 10
file_name = "example1.txt"
wite_words(word_count, file_name)

word_count = 30
file_name = "example2.txt"
wite_words(word_count, file_name)

word_count = 200
file_name = "example3.txt"
wite_words(word_count, file_name)

word_count = 100
file_name = "example4.txt"
wite_words(word_count, file_name)

end_time = datetime.now()
time_duration = end_time - start_time
print(f"Общее время выполнения функций: {time_duration} секунд")

start_time_threads = datetime.now()
threads = [
    threading.Thread(target=wite_words, args=(10, "example5.txt")),
    threading.Thread(target=wite_words, args=(30, "example6.txt")),
    threading.Thread(target=wite_words, args=(200, "example7.txt")),
    threading.Thread(target=wite_words, args=(100, "example8.txt"))
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end_time_threads = datetime.now()
time_duration_threads = end_time_threads - start_time_threads
print(f"Общее время выполнения потоков: {time_duration_threads} секунд")