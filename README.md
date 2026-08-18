# wildflower

script for fast video-to-image-sequence for photogrammetry pipelines. used in a variety of projects including video games, assets, etc.

![img](blender_oJzvps2R04.gif)

Mobile phone video -> *wildflower* output -> [Meshroom](https://github.com/alicevision/meshroom)

To be clear: this script just turns video into a folder of images, it does not **do** the photogrammetry. Results may depend on your understanding of what photogrammetry images need to be useful. The script is still more handy than some GUI/webtool options. 3 seconds of terminal and then a few sips of coffee later your output folder is opened for you.

## install and use

Requires `cv2` (`pip install cv2`)

Run: `python wildflower.py <input file> <output folder> <steps>`

---

[See games made by Protoria Studios](https://store.steampowered.com/search/?developer=Protoria%20Studios)

![](https://protoriastudios.com/Skyfear_Screenshot02.png)