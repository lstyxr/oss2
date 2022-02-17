import oss2

access_key_id = '************************'
access_key_secret = '******************************'


bucket_name = '*******************'
endpoint = '********************'

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

file_name = "../files/test.png"
with open(file_name, "rb") as f:
    data = f.read()

bucket.put_object('python/captcha_num.png', data)
fileurl = bucket.sign_url('GET', 'python/captcha_num.png', 60 * 60 * 24)

print(fileurl)
