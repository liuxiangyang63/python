# coding=utf-8

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

def cos_upload(image_obj, file_name):
	"""
	:param image_obj: 上传图片对象
	:param file_name: 上传图片名字
	:return:
	"""
	secret_id = 'AKIDOZYR7YmjU3Scf6qYP3e4GLHyLSL1sxxx'  # 替换为用户的secret_id
	secret_key = 'QpJhDe2TpfUVeieUD3Ri6GKE8nKG6xxx'  # 替换为用户的secret_key
	region = 'ap-beijing'  # 替换为用户的region
	token = None  # 使用临时密钥需要传入Token，默认为空,可不填
	config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
	client = CosS3Client(config)

	response = client.upload_file_from_buffer(
		Bucket='auction-1301082770',
		Body=image_obj,
		Key=file_name,
		PartSize=1,
		MAXThread=10,
		EnableMD5=False
	)
	print(response['ETag'])