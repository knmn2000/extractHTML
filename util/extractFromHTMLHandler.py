from readabilipy import simple_json_from_html_string

def extractFromHTMLHandler(html_content):
    """Parse content using the readbility module
    Returns:
        json: HTML content
    """
    try:
        readability = simple_json_from_html_string(html_content, use_readability=True)
    except:
        # Python based extraction in case Readability.js fails
        readability = simple_json_from_html_string(html_content, use_readability=False)
    return readability
