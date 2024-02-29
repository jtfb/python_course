from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open('mask.png')
# words.show()
# mask.show()

print(f'word size: {words.size}')
print(f'mask size: {mask.size}')

mask_resized = mask.resize((1015,559))
print(f'mask resized: {mask_resized.size}')

mask_resized_alpha = mask_resized.putalpha(128)

words.paste(mask_resized_alpha,(0,0), mask)

words.save("result.png")