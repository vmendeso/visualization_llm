#!/bin/bash

# Script de instalação de dependências do sistema para visualization_llm
# Este script instala todas as dependências necessárias antes de executar pip install -e .

set -e  # Sair em caso de erro

echo "=========================================="
echo "Instalando dependências do sistema..."
echo "=========================================="

# Detectar o sistema operacional
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Sistema Linux detectado"

    # Verificar distribuição
    if command -v apt-get &> /dev/null; then
        echo "Usando apt-get (Debian/Ubuntu)..."
        sudo apt-get update
        sudo apt-get install -y \
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

    elif command -v yum &> /dev/null; then
        echo "Usando yum (RedHat/CentOS)..."
        sudo yum install -y \
            pango-devel \
            pkgconfig \
            python3-devel \
            python3-pip \
            ffmpeg \
            cairo-devel \
            gobject-introspection-devel \
            mesa-libGL \
            mesa-libGL-devel \
            mesa-libEGL \
            mesa-libEGL-devel \
            freeglut-devel \
            texlive

    elif command -v pacman &> /dev/null; then
        echo "Usando pacman (Arch Linux)..."
        sudo pacman -S --noconfirm \
            pango \
            pkg-config \
            python \
            python-pip \
            ffmpeg \
            cairo \
            gobject-introspection \
            mesa \
            glu \
            freeglut \
            texlive-core

    else
        echo "Distribuição Linux não suportada automaticamente."
        echo "Por favor, instale manualmente as dependências listadas em INSTALL.md"
        exit 1
    fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Sistema macOS detectado"

    if ! command -v brew &> /dev/null; then
        echo "Homebrew não encontrado. Instalando Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    echo "Instalando dependências via Homebrew..."
    brew install ffmpeg mactex pango pkg-config cairo

    # Verificar se é processador ARM
    if [[ $(uname -m) == "arm64" ]]; then
        echo "Processador ARM detectado, instalando dependências adicionais..."
        brew install cairo
    fi

else
    echo "Sistema operacional não suportado: $OSTYPE"
    echo "Por favor, consulte INSTALL.md para instruções manuais."
    exit 1
fi

echo ""
echo "=========================================="
echo "Dependências do sistema instaladas com sucesso!"
echo "=========================================="
echo ""
echo "Agora você pode executar:"
echo "  pip install -e ."
echo ""
echo "Para instalar o pacote Python e todas as suas dependências."
