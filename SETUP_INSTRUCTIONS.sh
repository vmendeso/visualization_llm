#!/bin/bash

# Este é um guia de instalação passo a passo para o repositório visualization_llm
# Execute estes comandos no seu terminal

echo "=========================================="
echo "Instalação do visualization_llm"
echo "=========================================="
echo ""
echo "IMPORTANTE: Execute os comandos abaixo na ordem mostrada"
echo ""

echo "Passo 1: Instalar dependências do sistema"
echo "Execute este comando:"
echo ""
cat << 'EOF'
sudo apt-get update && sudo apt-get install -y \
    libpango1.0-dev \
    pkg-config \
    python3-dev \
    python3-pip \
    ffmpeg \
    libcairo2-dev \
    libgirepository1.0-dev \
    python3-cairo \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libegl1-mesa \
    libegl1-mesa-dev \
    libgles2-mesa-dev \
    freeglut3-dev \
    texlive \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-science
EOF

echo ""
echo "=========================================="
echo ""
echo "Passo 2: Navegar para o diretório do projeto"
echo "Execute:"
echo ""
echo "cd /home/sakod/Documentos/Visualization_LLM/visualization_llm"
echo ""
echo "=========================================="
echo ""
echo "Passo 3: Instalar o pacote Python"
echo "Execute:"
echo ""
echo "pip install -e ."
echo ""
echo "=========================================="
echo ""
echo "Passo 4: Testar a instalação"
echo "Execute:"
echo ""
echo "manimgl _2024/manim_demo/lorenz.py LorenzAttractor -p"
echo ""
echo "=========================================="
echo ""
echo "Se você encontrar erros, consulte INSTALL.md para soluções."
