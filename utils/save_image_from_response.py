def save_image_from_response(image_path, response):
    with open(image_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)