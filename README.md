# Image-Remover
Effortlessly remove backgrounds from images using the Image Remover Python library. Includes Command-Line Interface (CLI) tools and a simple web application built with Streamlit/Flask. Perfect for automation and web services.

## Getting Started
Follow these steps to get the project up and running on your local machine.

### Prerequisites
You need **Python 3.10** or higher installed.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/janakvaghela542/Image-Remover.git
    cd Image-Remover
    ```

2.  **Install dependencies** using `pip`:
    The core library, `rembg`, requires the `Pillow` library, which is included in the `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

    > **Note:** The first time you run the script, `rembg` will automatically download the necessary AI model (U2net or similar), which may take a moment.

---

## Usage (Command Line Interface)

The core functionality is provided by the `simple_cli.py` script.

### Basic Removal

Use the script to remove the background from a single image. **The output file extension must be `.png` to retain the transparent background.**

**Command:**
```bash
python simple_cli.py <INPUT_IMAGE_PATH> <OUTPUT_IMAGE_PATH>
