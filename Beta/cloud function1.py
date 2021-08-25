from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
from google.cloud import storage
from flask import send_file

bucket_name = "templates123"
source_blob_name = "Template.docx"
destination_file_name = "/tmp/template.docx"

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)

def read_request(request):
    # handle the POST request
    if request.method == 'POST':
        Value1 = request.form.get('Name')
        Value2 = request.form.get('Address')
        value3 = request.form.get('Number')
        value4 = request.form.get('addtl')
        value5 = request.form.get('text1')
        value6 = request.form.get('text2')
    else:
        print("error on loading page")

    template = "/tmp/template.docx"

    document = MailMerge(template)

    document.merge(
        Name=Value1,
        Address=Value2,
        Number=Value3,
        addtl=Value4,
        text1=value5,
        text2=value6,
        )

    document.write('/tmp/test-output.docx')

    return send_file("/tmp/test-output.docx")
