import os
import json
import requests

from PIL import Image
from dotenv import load_dotenv

import pandas as pd
from openai import AzureOpenAI
from typing import Any, Dict


def setup_client() -> AzureOpenAI:
    """
    Initialises and returns an AzureOpenAI client using environment variables.

    Returns:
        AzureOpenAI: An instance of the AzureOpenAI class.
    """
    load_dotenv()
    api_version = os.environ.get('API_VERSION')
    api_key = os.environ.get('API_KEY')
    azure_endpoint = os.environ.get('ENDPOINT')

    client = AzureOpenAI(
        api_version=api_version,
        api_key=api_key,
        azure_endpoint=azure_endpoint
    )
    return client


def generate_image_response(client: AzureOpenAI) -> Dict[str, Any]:
    """
    Generates an image based on a prompt using AzureOpenAI's image generation API.

    Args:
        client (AzureOpenAI): The AzureOpenAI client to use for image generation.

    Returns:
        Dict[str, Any]: A JSON-decoded dictionary containing the image generation response.
    """
    result = client.images.generate(
        prompt='A dog surfing a wave',
        model='dall-e-3',
        n=1,
        quality='hd',
        size="1024x1024",
        response_format='url',
        style='vivid'
    )

    # Convert the response to JSON
    model_dump_json = result.model_dump_json()
    json_response = json.loads(model_dump_json)

    return json_response


def set_directory(directory_name: str) -> None:
    """
    Creates the specified directory if it does not already exist.

    Args:
        directory_name (str): The name of the directory to create.
    """
    image_dir = os.path.join(os.curdir, directory_name)
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)


def create_safety_report(json_response: Dict[str, Any], filter_result_type: str) -> None:
    """
    Creates a safety report (CSV) from the specified filter results in the JSON response.

    Args:
        json_response (Dict[str, Any]): The JSON response containing filter results.
        filter_result_type (str): The key in the JSON response to extract filter results from.
    """
    content_filter_results = json_response["data"][0][filter_result_type]
    df = pd.DataFrame.from_dict(content_filter_results, orient='index').reset_index()
    df.rename(columns={'index': 'category'}, inplace=True)
    df.to_csv(f'./datasets/{filter_result_type}_report.csv', index=False)


def show_and_save_image(json_response: Dict[str, Any], image_directory: str) -> None:
    """
    Downloads an image from the provided JSON response, saves it locally, and displays it.

    Args:
        json_response (Dict[str, Any]): The JSON response containing the image URL.
        image_directory (str): The directory where the image should be saved.
    """
    image_path = os.path.join(image_directory, 'generated_image.png')

    # Retrieve the generated image
    image_url = json_response["data"][0]["url"]
    generated_image = requests.get(image_url).content
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image
    image = Image.open(image_path)
    image.show()


def main() -> None:
    """
    Main execution function that orchestrates:
      1. Creating the AzureOpenAI client.
      2. Generating an image response.
      3. Creating the necessary directories.
      4. Creating safety reports.
      5. Showing and saving the generated image.
    """
    client = setup_client()
    json_response = generate_image_response(client=client)

    for directory_name in ['images', 'datasets']:
        set_directory(directory_name=directory_name)
    
    for filter_result_type in ['prompt_filter_results', 'content_filter_results']:
        create_safety_report(json_response=json_response, filter_result_type=filter_result_type)
    
    show_and_save_image(json_response=json_response, image_directory='images')


if __name__ == '__main__':
    main()
