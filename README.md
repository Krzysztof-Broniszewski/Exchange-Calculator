# NBP Exchange Rates — Table A

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1oI--Yru8go7zGO3L3JM85eAplq3DEt01?usp=drive_link)

A compact notebook that fetches daily exchange rates from the National Bank of Poland (NBP) **Table A** public API and lists currency names with ISO codes. Minimal by design for quick review and execution.

---

## Run in Colab
1. Click the **Open in Colab** badge above.  
2. Go to **Runtime → Run all**.

> Note: Colab usually ships with `requests`, so no extra setup is needed there.

## Run locally
```bash
# create a clean env (conda/mamba recommended)
mamba create -n nbp -c conda-forge python=3.11
mamba activate nbp

# install dependencies
pip install -r requirements.txt    # contains: requests>=2.32

# or quickly:
# pip install "requests>=2.32"

# open the notebook
jupyter lab
