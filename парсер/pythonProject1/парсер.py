import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random

header = {"user-agent": user}
image_number = 0


try:
    for storage_number in range(1, 3):
        link = f'https://zastavok.net/'
        request = requests.get(f"{link}/{storage_number}/", headers=header).text

        soup = BeautifulSoup(request, 'lxml')
        main_block = soup.find('div', class_='block-photo')

        image_all = main_block.find_all('div', class_='short_full')

        for image in image_all:
            image_link = image.find('a').get('href')
            download_storage = requests.get(f'{link}{image_link}').text

            download_soup = BeautifulSoup(download_storage, 'lxml')
            main_data = download_soup.find('div', class_='image_data-func').find('div', class_='block_down')
            result_link = main_data.find('a').get('href')


            image_bytes = requests.get(f'{link}{result_link}').content

            print(type(image_bytes))
            with open(f'C:\\Users\\USER\\Desktop\\image\\{image_number}.jpg', 'wb') as file:
                file.write(image_bytes)

            image_number += 1
            print('Изображение успешно скачано!')

        print('\nпереход к следующей странице\n')

except KeyboardInterrupt as e:
    print('выход')
finally:
    print("Скачивание завершено")