![image](logo.svg)

`encode` is a Python package that provides a command-line interface for encoding and decoding strings using various methods such as Base64, URL encoding, and HTML encoding.

## Getting Started

### Prerequisites

Make sure you have Python and `pip` installed on your system.

### Clone the Repository

```bash
git clone https://github.com/devinci-it/encoder-py.git
cd encoder-py
```

### Install Dependencies

```bash
# Optionally, create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux or macOS
# or
.\venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Run the Script

```bash
python encoder/cli.py --interactive
```

### Making It System-Wide

To make the `encoder` script accessible system-wide, create a script in a directory in your system's `PATH`. For example, on Linux:

```bash
echo "python /path/to/encoder-py/encoder/cli.py \"\$@\"" | sudo tee /usr/local/bin/encoder
sudo chmod +x /usr/local/bin/encoder
```

Replace `/path/to/encoder-py/` with the actual path to your `encoder-py` directory.

Now, you can run the `encoder` command system-wide:

```bash
$ encoder --interactive

    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █░▄▄█░▄▄▀█▀▄▀█▀▄▄▀█░▄▀█░▄▄
    █░▄▄█░██░█░█▀█░██░█░█░█░▄▄
    █▄▄▄█▄██▄██▄███▄▄██▄▄██▄▄▄
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Author: devinci-it
(c) 2024
MIT LICENSE 
    
Usage: python cli.py [OPTIONS]

Options:
-e, --encode      Encode input string
-d, --decode      Decode input string
-c, --continuous  Continuous mode for encoding/decoding
-t, --type TEXT   Select encoding type (default: base64)
-i, --interactive Interactive mode for encoding/decoding
-h, --help        Show this message and exit
```

## Contributing

If you'd like to contribute, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
