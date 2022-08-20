"""_summary_"""
import json
import api
import images

def main():
    """_summary_"""
    card_name = input("Digite el nombre de la carta que desea buscar: ").strip().lower()
    url_request = f'{api.URL}?name={card_name}'

    status, response = api.get_request(url_request)

    if status:

        card_name = card_name.replace(' ', '_')
        card_data = f'card_data/{card_name}.txt'
        response_content = response.content.decode('utf-8')
        data_json = json.loads(response_content)
        data = data_json['data'][0]

        with open(card_data, 'w+', encoding='utf-8') as file:
            file.truncate(0)

        for key in data:
            match key:
                case 'card_sets' | 'card_prices':
                    pass
                case 'card_images':
                    status, response_img = api.get_request(data[key][0]['image_url'])

                    if status:
                        images.save_img(card_name, response_img)
                case _:

                    with open(card_data, 'a', encoding='utf-8') as file:
                        file.write(key + ' : ' + str(data[key]) + '\n')

if __name__ == '__main__':
    main()
