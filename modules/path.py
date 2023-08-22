import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
modelfile_path = os.path.abspath(os.path.join(base_dir, 'Models', 'Checkpoints'))
lorafile_path = os.path.abspath(os.path.join(base_dir, 'Models', 'Loras'))
