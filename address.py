def main():
    address_books = [
        {'name': '東京タワー',
         'location': '東京都港区芝公園４丁目２−８',
         'zipcode': '1050011'},

        {'name': 'スカイツリー',
         'location': '東京都墨田区押上１丁目１−２',
         'zipcode': '1310045'},

        {'name': '通天閣タワー',
         'location': '大阪府大阪市浪速区恵美須東１丁目１８−６',
         'zipcode': '5560002'},
    ]

    for book in address_books:
        print(f"{book['name']} 〒{book['zipcode']} {book['location']}")


if __name__ == '__main__':
    main()
