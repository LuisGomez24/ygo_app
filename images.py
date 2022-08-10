import pywhatkit as kt

SRC_DIR  = 'card_img/'
DEST_DIR = 'card_ascii/' 

def save_img(card_name, response_img):
    
    card_path = f'{SRC_DIR}{card_name}.jpg'
    
    with open(card_path, 'wb') as file:
        for chunk in response_img.iter_content(1024):
            file.write(chunk)
            
def save_ascii_img(card_name):
    
    src_path  = f'{SRC_DIR}{card_name}.jpg'
    dest_path = f'{DEST_DIR}{card_name}'
    
    kt.image_to_ascii_art(src_path, dest_path)

