# Creating venv
python3 -m venv _env

# Activate
source _env/bin/activate

# Deactivate
deactivate

# Install requirements
pip install -r requirements.txt

# Start our server
uvicorn main:app --reload

