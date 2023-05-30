Usage
=====

To extract only the parts that you will need, use:

.. code-block:: python3

	from reddit_photo_aggregator import SubReddit, ImageURLValidator, SortBy


Alternatively, import just the package:

.. code-block:: python3

	import reddit_photo_aggregator


Set the image host whitelist using :func:`.set_image_host_whitelist() <reddit_photo_aggregator.ImageURLValidator.set_image_host_whitelist>`

.. code-block:: python3

	ImageURLValidator.set_image_host_whitelist([
		'i.redd.it',
		'i.imgur.com',
	])


Set the file extension whitelist using :func:`.set_image_extension_whitelist() <reddit_photo_aggregator.ImageURLValidator.set_image_extension_whitelist>`

.. code-block:: python3

	ImageURLValidator.set_image_extension_whitelist([
		'png',
		'jpeg',
		'jpg'
	])


Create a :class:`SubReddit <reddit_photo_aggregator.SubReddit>` object with the sub-reddit name that you want to aggregate images from

.. code-block:: python3

	sub = SubReddit('r/LandscapePhotography')


You can then discover images, this can be sorted using the :class:`SortBy <reddit_photo_aggregator.SortBy>` class, this will also give you the amount of images found and the ``sub.loaded_images`` becomes filled out

.. code-block:: python3

	amount = sub.discover_images(SortBy.hot)
	print(amount)
	print(sub.loaded_images)


Save the images to an ``/images`` directory.

.. code-block:: python3

	for image in sub.loaded_images:
		print(f'Saving to {image.filename}')
		image.save(to='./images')


Full Example
------------

.. code-block:: python3

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
	amount = sub.discover_images(SortBy.hot)
	print(amount)

	for image in sub.loaded_images:
		print(f'Saving to {image.filename}')
		image.save(to='./images')
