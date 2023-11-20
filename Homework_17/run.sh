#source "$VENV_NAME/bin/activate"
# Activate for windows
hillel_venv/Scripts/activate
python -m pytest -s "$@"

# run from terminal
# cd//./run.sh test_selenium_first_steps.py