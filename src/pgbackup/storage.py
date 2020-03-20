def local(src_file, destination_file):
    destination_file.write(src_file.read())
    destination_file.close()
    src_file.close()


def s3(client, src_file, bucket, name):
    client.upload_fileobj(src_file, bucket, name)
