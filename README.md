# QuickShop
Welcome to QuickShop, a personal shopping agent that emphasizes finding quality clothing from legitimate buyers at a fair price! Check out the output_example.txt to view an example output given the input prompt, and if you want to run this on your own read the following instructions.


Use the LLM API keys provided by ASU Sol RC. Use this link for understanding how to gain access. https://docs.rc.asu.edu/ai/api
The model ID used is gpt-oss-120b, but that should already be fed into the code. If not, paste that model id to the model_id variable. 

Once cloning the repository, make sure to create a .env for your API key and set up the virtual environment. 

python3 -m venv venv && source venv/bin/activate

Then, install all requirements. 

pip install -r requirements.txt

After that, you should be able to run the baseline code and obtain the same output as the output_example.txt.

python3 run.py

The baseline will take an input from a txt file and specific items loaded onto a products.json file, where the name, price, material, seller, seller reputation, rating, and reviews of each product is listed there. Then, the LLM will look through all of the products in the json file and determine the recommended products (around 3) and put that into the output.txt. 

Disclaimer: The baseline model and ideas for an agent for the capstone project were created with generative AI. The ChatGPT link below traces the whole conversation. However, any written portions (ie. README) was written by me. 
