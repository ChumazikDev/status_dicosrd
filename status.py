from pypresence import Presence
import time as TIME
BTNS = [
    {
        "label": "TG",
        "url": "https://t.me/chumazik_dev/"
    }
         
]
RPC = Presence("YOUR_Application_ID")
RPC.connect()
print('Starting...')
timer = 199
print('Connecting...')
RPC.update(
    state="state",
    details="details",
    start=timer,
    party_id='game',
    party_size=[9999, 1],
    buttons=BTNS,
    large_image="YOUR_PHOTO_NAME",
    small_image='YOUR_PHOTO_NAME',
    small_text='text photo',
    large_text="text photo",
    instance=True)

print('Discord status working...')
timer += 1
TIME.sleep(999999)