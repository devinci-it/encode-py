import base64
import urllib.parse
import html

def encode_base64(data):
    """
    Encode the input string using Base64 encoding.

    Parameters:
    - data (str): The string to be encoded.

    Returns:
    str: The Base64 encoded string.
    """
    try:
        encoded_data = base64.b64encode(data.encode()).decode()
        return encoded_data
    except Exception as e:
        raise ValueError(f"Error encoding with Base64: {e}")

def decode_base64(encoded_data):
    """
    Decode a Base64 encoded string.

    Parameters:
    - encoded_data (str): The Base64 encoded string.

    Returns:
    str: The decoded string.
    """
    try:
        decoded_data = base64.b64decode(encoded_data).decode()
        return decoded_data
    except Exception as e:
        raise ValueError(f"Error decoding with Base64: {e}")

def encode_url(data):
    """
    Encode the input string using URL encoding.

    Parameters:
    - data (str): The string to be encoded.

    Returns:
    str: The URL encoded string.
    """
    try:
        encoded_data = urllib.parse.quote(data)
        return encoded_data
    except Exception as e:
        raise ValueError(f"Error encoding with URL encoding: {e}")

def decode_url(encoded_data):
    """
    Decode a URL encoded string.

    Parameters:
    - encoded_data (str): The URL encoded string.

    Returns:
    str: The decoded string.
    """
    try:
        decoded_data = urllib.parse.unquote(encoded_data)
        return decoded_data
    except Exception as e:
        raise ValueError(f"Error decoding with URL encoding: {e}")

def encode_html(data):
    """
    Encode the input string using HTML encoding.

    Parameters:
    - data (str): The string to be encoded.

    Returns:
    str: The HTML encoded string.
    """
    try:
        encoded_data = html.escape(data)
        return encoded_data
    except Exception as e:
        raise ValueError(f"Error encoding with HTML encoding: {e}")

def decode_html(encoded_data):
    """
    Decode an HTML encoded string.

    Parameters:
    - encoded_data (str): The HTML encoded string.

    Returns:
    str: The decoded string.
    """
    try:
        decoded_data = html.unescape(encoded_data)
        return decoded_data
    except Exception as e:
        raise ValueError(f"Error decoding with HTML encoding: {e}")
