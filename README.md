# sprout
Sprout is a computational photography project. Make your plants bloom.
to run activate a virtual environment
>clone repository
>activate a python virtual environment
>pip install requirements.txt
>python impose_flowers <flower_file_name> <plant_file_name> <max_num_flowers> <optional_clump> <optional_flower_min_size> <optional_flower_max_size>

clump is an alternate imposing where it just puts one clump of flower on the plant. This is turned on by putting 1 in the clump spot and turned off by default or by putting 0. If you explicitly define flower max and min size you must also explicitly set clump. All other args are not optional. Max_num_flowers sets the max amount of flowers that could show up on the plant, but will be less if not enough meet the quality checking criteria. Plant images with white backgrounds are what works best, and the given flower files should be the ones used for the flower parameter.
