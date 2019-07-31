# sprout
Sprout is a computational photography project. Make your plants bloom.
to run activate a virtual environment
-clone repository
-activate a python virtual environment
-pip install requirements.txt
-python impose_flowers <flower_file_name> <plant_file_name> <max_num_flowers> <optional_clump> <optional_flower_min_size> <optional_flower_max_size>

clump is an alternate imposing where it just puts one clump of flower on the plant. This is turned on by putting 1 in the clump spot and 
turned off by default or by putting 0. If you explicitly define flower max and min size you must also explicitly set clump. All other 
args are not optional. Max_num_flowers sets the max amount of flowers that could show up on the plant, but will be less if not enough 
meet the quality checking criteria. Plant images with white backgrounds are what works best, and the given flower files should be the ones 
used for the flower parameter. Some example plant pictures that work well are in the repository as well.


Examples with params that give decent results
python impose_flowers.py white-flower-2.jpeg th.jpg 20 0 .1 .3
python impose_flowers.py flower.png vines.jpg 20 0 .04 .1
python impose_flowers.py flower.png vase.jpg 10 0 .08 .15
python impose_flowers.py white-flower-2.jpeg jasmine.jpg 7 0 .15 .25
python impose_flowers.py white-flower-2.jpeg potted.jpg 14 0 .2 .3
python impose_flowers.py flower.png leafy.jpg 7 0 .2 .4
python impose_flowers.py white-flower-2.jpeg th-1.jpg 5 0 .2 .25
python impose_flowers.py flower.png fiddle-fig.jpg 10 0 .07 .18
python impose_flowers.py flower.png amazon-sword.jpg 7 0 .1 .2









