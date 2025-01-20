# Azure OpenAI Image Generation with Python
This repository demonstrates how to generate images using the AzureOpenAI service in Python. It uses a simple script to generate an image (saved in an `images` directory) and safety reports (saved in a `datasets` directory) based on a prompt. 



## Environment Variables
Make sure to place the values for each environment variable (in the `.env` file) as defined in your Azure OpenAI resource. This requires an `API_VERSION`, `API_KEY` and `ENDPOINT`

## How to Run
Once the environment variables have been correctly set up, run the script as follows

```python
python3 image_generation.py`
```

This will do the following:

1. Setup Client: The script initialises an AzureOpenAI client with your credentials.

2. Generate Image Response: Prompts the AzureOpenAI service to generate an image (e.g. a dog surfing a wave).

3. Create Directories: The images and datasets directories are created if they do not already exist.

4. Safety Reports: Two CSV files `prompt_filter_results_report.csv` and `content_filter_results_report.csv` are saved in the datasets directory.

5. Show and Save Image: The generated image is saved to the `images` directory and displayed in the default image viewer.

## Useful resources
* [Response after calling `images.generate()`](https://learn.microsoft.com/en-us/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Cresponse&pivots=programming-language-python#imagesgenerate)
