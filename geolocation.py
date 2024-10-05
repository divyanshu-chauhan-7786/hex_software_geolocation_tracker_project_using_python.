import phonenumbers
from opencage.geocoder import OpenCageGeocode
import folium
import tkinter as tk
from tkinter import messagebox
from phonenumbers import geocoder, carrier

def find_location():
    try:
        number = entry_number.get()
        ipkey = entry_key.get()

    
        pepnumbers = phonenumbers.parse(number)
        location = geocoder.description_for_number(pepnumbers, "en")

        service = phonenumbers.parse(number)
        carrier_name = carrier.name_for_number(service, "en")

        geocoder_instance = OpenCageGeocode(ipkey)
        query = str(location)
        result = geocoder_instance.geocode(query)

        if result and len(result):
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']

        
            messagebox.showinfo("Location Info", f"Location: {location}\nCarrier: {carrier_name}\nLatitude: {lat}\nLongitude: {lng}")

    
            myloc = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(myloc)
            myloc.save('location.html')


            messagebox.showinfo("Success", "Location map saved as 'location.html'")
        else:
            messagebox.showerror("Error", "Location not found. Check your API key or phone number.")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Phone Number Location Finder")

label_number = tk.Label(root, text="Enter Phone Number:")
label_number.pack(pady=10)
entry_number = tk.Entry(root, width=60)
entry_number.pack(pady=10)

label_key = tk.Label(root, text="Enter API Key:")
label_key.pack(pady=10)
entry_key = tk.Entry(root, width=60)
entry_key.pack(pady=10)

btn_find = tk.Button(root, text="Find Location", command=find_location)
btn_find.pack(pady=15)

root.mainloop()
