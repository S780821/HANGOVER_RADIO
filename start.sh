echo "Cloning Repo...."
git clone https://github.com/780821/HANGOVER_RADIO.git /HANGOVER_RADIO
cd /HANGOVER_RADIO
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
