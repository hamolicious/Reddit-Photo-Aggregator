import os
from src import SubReddit, ImageURLValidator, SortBy

ImageURLValidator.set_image_host_whitelist([
	'i.redd.it',
	'i.imgur.com',
])
ImageURLValidator.set_image_extension_whitelist([
	'png',
	'jpeg',
	'jpg'
])

sub = SubReddit('r/LandscapePhotography')
sub = SubReddit('r/SonyAlpha')
amount = sub.discover_images(SortBy.hot)
print(amount)

for image in sub.loaded_images:
	print(f'Saving to {image.filename}')
	image.save(to='./images')

