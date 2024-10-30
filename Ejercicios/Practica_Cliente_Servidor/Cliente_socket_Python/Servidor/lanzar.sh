#!/bin/bash

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  
  python3 -m venv venv

fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt -U

# Ejecutar main.py
python main.py

