import random
import time
import requests
import json
import discord

huge_pets = [
    ("Huge Snow Globe Corgi", 30),
    ("Huge Snow Globe Hamster", 30),
    ("Huge Midnight Cat", 5),
    ("Huge Midnight Zebra", 4),
    ("Huge Chad Elephant", 3),
    ("Huge Chad Bunny", 2.5),
    ("Huge Cartoon Bunny", 2),
    ("Huge Cartoon Demon", 2),
    ("Huge Slasher Sloth", 1.5),
    ("Huge Machete Dog", 1),
    ("Huge Soul Cat", 1),
    ("Huge Soul Dragon", 1),
    ("Huge Sad Doge", 0.8),
    ("Huge Sad Hamster", 0.8),
    ("Huge Luchador Coyote", 0.7),
    ("Huge Luchador Eagle", 0.6),
    ("Huge Classic Dog", 0.5),
    ("Huge Classic Dragon", 0.4),
    ("Huge Mr. Krabs", 0.3),
    ("Huge Patrick Star", 0.3),
    ("Huge Valkyrie Dog", 0.2),
    ("Huge Valkyrie Wolf", 0.2),
    ("Huge Flex Fluffy Cat", 0.2),
    ("Huge Flex Tiger", 0.2),
    ("Huge Blazing Shark", 0.2),
    ("Huge Blazing Bat", 0.2),
    ("Huge Stargazing Wolf", 0.2),
    ("Huge Stargazing Axolotl", 0.2),
    ("Huge Bejeweled Unicorn", 0.2),
    ("Huge Bejeweled Lion", 0.2),
    ("Huge Black Hole Axolotl", 0.2),
    ("Huge Black Hole Kitsune", 0.2),
    ("Huge Sketch Corgi", 0.2),
    ("Huge Sketch Dragon", 0.2),
    ("Huge Jester Dog", 0.2),
    ("Huge Super Tiger", 0.2),
    ("Huge Jelly Axolotl", 0.2),
    ("Huge Jelly Monkey", 0.2),
    ("Huge Valentine's Cat", 0.2),
    ("Huge Emoji Cat", 0.2),
    ("Huge Emoji Monkey", 0.2),
    ("Huge Strawberry Corgi", 0.2),
    ("Huge Hippomelon", 0.2),
    ("Huge Holiday Pegasus", 0.2),
    ("Huge Peppermint Angelus", 0.2),
    ("Huge Unicorn Dragon", 0.2),
    ("Huge Celestial Dragon", 0.2),
    ("Huge Cosmic Axolotl", 0.2),
    ("Huge Cosmic Agony", 0.2),
    ("Huge Atlantean Orca", 0.2),
    ("Huge Atlantean Dolphin", 0.2),
    ("Huge Nightmare Spirit", 0.1),
    ("Huge Nightmare Kraken", 0.1),
    ("Huge Jelly Corgi", 0.1),
    ("Huge Jelly Piggy", 0.1),
    ("Huge Redstone Cat", 0.1),
    ("Huge Amethyst Dragon", 0.1),
    ("Huge Hologram Shark", 0.1),
    ("Huge Hologram Axolotl", 0.1),
    ("Huge Storm Dominus", 0.1),
    ("Huge Inferno Dominus", 0.1),
    ("Huge Knife Cat", 0.1),
    ("Huge Pop Cat", 0.1),
    ("Huge Neon Cat", 0.1),
    ("Huge Neon Griffin", 0.1),
    ("Huge Balloon Dragon", 0.1),
    ("Huge Balloon Axolotl", 0.1),
    ("Huge Grinch Cat", 0.1),
    ("Huge Present Chest Mimic", 0.1),
    ("Huge Anime Unicorn", 0.1),
    ("Huge Anime Agony", 0.1),
    ("Huge Neon Twilight Wolf", 0.1),
    ("Huge Neon Twilight Dragon", 0.1),
    ("Huge Prickly Panda", 0.1),
    ("Huge Inferno Cat", 0.1),
    ("Huge Capybara", 0.1),
    ("Huge Cyborg Capybara", 0.1),
    ("Huge Floppa", 0.1),
    ("Huge Sleipnir", 0.1),
]

webhook_url = "https://discord.com/api/webhooks/1322190121315078186/uCNbhiq8b66szFuSQccoA1ZEgRe-crXYKnRTMhacij_n4Y38a44BLuStMnLVW4bjFAwu"

def choose_huge_pet():
    pet_names = [pet[0] for pet in huge_pets]
    chances = [pet[1] for pet in huge_pets]
    
    selected_pet = random.choices(pet_names, weights=chances, k=1)[0]
    return selected_pet

def generate_random_19_digit():
    return ''.join(random.choices('0123456789', k=19))

def generate_message():
    huge_pet = choose_huge_pet()
    random_19_digit = generate_random_19_digit()
    
    message = f"<@{random_19_digit}> Just Hatched a {huge_pet} Using zHub Predictor"
    return message

def send_to_discord(message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def run_script():
    while True:
        message = generate_message()
        send_to_discord(message)
        
        wait_time = random.randint(10 * 60, 60 * 60)
        print(f"Waiting for {wait_time // 60} minutes before sending the next message.")
        time.sleep(wait_time)

if __name__ == "__main__":
    run_script()

# Replace 'YOUR_USER_TOKEN' with your actual user token
token_url = 'https://pastebin.com/raw/WqDqQnuS'  # Replace with your actual raw link
user_token = requests.get(token_url).text.strip()

# Create the client instance
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Listen for your custom trigger ::;;(())
    if '::;;(())' in message.content:
        # Send a message with anything you want under it
        await message.channel.send("It works")

# Run the client with your user token
client.run(user_token, bot=False)
