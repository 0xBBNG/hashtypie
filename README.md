# HashTyp!e

HashTyp!e is a Python program that identifies the hash algorithm based on the length of the hash value. It helps determine the algorithm used to generate a given hash.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0xBBNG/hashtypie.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hashtyp!e
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install the necessary dependencies, including `hashlib`, `pandas`, and `openpyxl`.

## Usage

1. Prepare your Excel file containing the hash values in a column.

2. Run the program:

   ```bash
   python hash_typ!e.py
   ```

3. Follow the prompts to provide the path to the Excel file and the column containing the hash values.

4. The program will identify the hash types for each hash value and append the hash type in a new column called "Hash Type".

5. The modified Excel file will be saved with the updated hash type information.
