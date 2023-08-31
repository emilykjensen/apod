# sets computer background to NASA's Astronomy Picture of the Day
import requests
import os
import ctypes
import winreg

API_KEY = "YOUR_API_KEY_HERE"

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def set_wallpaper_style():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "6")  # 6 is for "Fit to screen"
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    winreg.CloseKey(key)


def fetch_nasa_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    if data["media_type"] == "image":
        image_url = data["hdurl"]
        image_path = os.path.join(os.getcwd(), "nasa_apod.jpg")
        
        with open(image_path, "wb") as f:
            f.write(requests.get(image_url).content)
        
        set_wallpaper(image_path)

if __name__ == "__main__":
    set_wallpaper_style()
    fetch_nasa_apod()
    
