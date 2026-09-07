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
