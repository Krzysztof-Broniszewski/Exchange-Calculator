# NBP Exchange Rates — Table A

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<USER>/<REPO>/blob/main/notebooks/01_main.ipynb)
&nbsp;|&nbsp; [Polska wersja](./README.pl.md)

A compact notebook that fetches daily exchange rates from the National Bank of Poland (NBP) **Table A** API and prints currency codes and names. Minimal by design for quick review and execution.

---

## Run in Colab
1. Click the **Open in Colab** badge above.  
2. **Runtime → Run all**.  
> Note: Colab already includes `requests`, so no extra setup is needed there.

## Run locally
```bash
# create a clean env (conda/mamba)
mamba create -n nbp -c conda-forge python=3.11
mamba activate nbp

# install deps
pip install -r requirements.txt

# start Jupyter
jupyter lab

# Kursy walut NBP — Tabela A

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<USER>/<REPO>/blob/main/notebooks/01_main.ipynb)
&nbsp;|&nbsp; [English version](./README.md)

Zwięzły notatnik pobierający dzienne kursy z publicznego API NBP (**Tabela A**) oraz wypisujący kody i nazwy walut. Minimalny, aby łatwo go przejrzeć i uruchomić.

---

## Uruchom w Colabie
1. Kliknij badge **Open in Colab** powyżej.  
2. **Runtime → Run all**.  
> Uwaga: w Colabie `requests` jest zazwyczaj już dostępne, więc nie trzeba nic instalować.

## Uruchom lokalnie
```bash
# czyste środowisko (conda/mamba)
mamba create -n nbp -c conda-forge python=3.11
mamba activate nbp

# zależności
pip install -r requirements.txt

# start Jupytera
jupyter lab
