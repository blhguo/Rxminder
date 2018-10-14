'''
Created on Oct 13, 2018

@author: brandon guo
'''
def detect_handwritten_ocr_uri(uri):
    """Detects handwritten characters in the file located in Google Cloud
    Storage.

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """
    from google.cloud import vision_v1p3beta1 as vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(image=image,
                                              image_context=image_context)

    print('Full Text: {}'.format(response.full_text_annotation.text))

    ret = []
    flag = False
    flag1 = False
    flag2 = True
    flag3 = False



    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            #print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                #print('Paragraph confidence: {}'.format(paragraph.confidence))

                for word in paragraph.words:

                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    if flag1 and flag2:
                        #print(word_text)
                        ret.append(word_text)
                        flag2 = False
                    if flag:
                        flag1 = True
                    #print('Word text: {} (confidence: {})'.format(
                        #word_text, word.confidence))

                    if word_text == "Qty" or word_text == "Quantiy" or word_text == "amount":
                        flag = True
                    if flag3:
                        if word_text.isdigit:
                            #print("occur")
                            ret.append(word_text)
                            flag3 = False
                    elif (word_text == "TAKE" or word_text == "Take" or word_text == "take"):
                        flag3 = True
                    

    #print (ret)
    return ret