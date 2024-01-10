from easydict import EasyDict as edict


config = edict()
config.margin_list = (1.0, 0.5, 0.0)
config.network = "r50"
config.resume = False
config.output = '/content/output'
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 5e-4
config.batch_size = 128
config.lr = 0.02
config.verbose = 2000
config.dali = False

config.rec = "/content/arcface_torch/database"
config.num_classes = 2
config.num_image = 1000
config.num_epoch = 100
config.warmup_epoch = 0
config.val_targets = []
