from PIL import Image

# Load image
image_path = r"C:\Users\b_cer\Documents\GitWebpage\mattchoo2.github.io\assets\images\MattLifeTech.png"
output_path = r"C:\Users\b_cer\Documents\GitWebpage\mattchoo2.github.io\assets\images\MattLifeTech_transparent.png"

image = Image.open(image_path).convert("RGBA")

# Process pixels
datas = image.getdata()
new_data = [
    (r, g, b, 0) if (r > 200 and g > 200 and b > 200) else (r, g, b, a)
    for (r, g, b, a) in datas
]

# Apply changes
image.putdata(new_data)
image.save(output_path)

print(f"Transparent image saved as: {output_path}")
