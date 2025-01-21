# Azure OpenAI Image Generation with Python
This repository demonstrates how to generate images using the AzureOpenAI service in Python. It uses a script to generate an image (saved in an `images` directory) and safety reports (saved in a `datasets` directory) based on a prompt. 

For example, a user can enter a prompt in the script such as "A dog riding a surfboard". From there, an image will be generated based on this prompt and saved to an `images` directory. Two safety report around aspects such as hate speech, violence etc. will also be generated, and placed in a directory called `datasets`.

Example business benefits:
* Reduced Design Costs: Automating the process of creating images can reduce dependence on external designers, lowering ongoing costs.
* Fast Prototyping: Quickly generating multiple image variants allows marketing and product teams to experiment and iterate at a faster speed, saving time (and resources).
* API-driven: Since the service is API-driven, it can be called automatically at any time from various applications or internal tools.
* Uniqueness: Stock photos are often used by many organisations, leading to repetitive or clichéd visuals. AI-generated images can be fresh and original.
* Showcasing AI Expertise: Demonstrating sophisticated uses of AI can bolster a firm’s reputation, attracting both customers and top-tier talent.

## Prerequisites
1. You must set up and deploy Azure OpenAI resource and retrieve the resource API version, API key and endpoint, which can be found in the Azure AI Foundry Portal after deploying the resource.
2. The following imports are needed
   ```python
   import os
   import json
   import requests
   
   from PIL import Image
   from dotenv import load_dotenv
   
   import pandas as pd
   from openai import AzureOpenAI
   from typing import Any, Dict
   ```

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
* [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
* [Detailed breakdown of what to pass to `client.images.generate`](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#request-body-5)
* [Response after calling `images.generate()`](https://learn.microsoft.com/en-us/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Cresponse&pivots=programming-language-python#imagesgenerate)
* [Where/why to use the `model_dump_json` method](https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json)
