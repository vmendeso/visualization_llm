# Instruções de Instalação

Este guia ajudará você a instalar todas as dependências necessárias para o repositório visualization_llm.

## Dependências do Sistema

Antes de executar `pip install -e .`, você precisa instalar algumas dependências do sistema:

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install -y \
    libpango1.0-dev \
    pkg-config \
    python3-dev \
    ffmpeg \
    libcairo2-dev \
    libgirepository1.0-dev \
    python3-cairo \
    texlive-full
```

### macOS

```bash
brew install ffmpeg mactex pango pkg-config cairo

# Para processadores ARM (M1/M2/M3)
brew install cairo
```

### Windows

1. **FFmpeg**: Baixe de https://ffmpeg.org/download.html e adicione ao PATH
2. **LaTeX**: Instale MiKTeX de https://miktex.org/download
3. **Compilador C++**: Instale Visual Studio Build Tools

## Instalação do Pacote

Depois de instalar as dependências do sistema, execute:

```bash
pip install -e .
```

Este comando irá:
- Instalar o manimgl (biblioteca de animação)
- Instalar todas as dependências Python necessárias
- Configurar o repositório em modo editável (development mode)

## Verificação da Instalação

Para verificar se tudo foi instalado corretamente, tente executar:

```bash
manimgl --version
```

Ou teste com uma cena simples:

```bash
manimgl playground.py TestScene -p
```

## Configuração Adicional

O arquivo `custom_config.yml` contém configurações personalizadas para o manim. Você pode ajustar:
- Resolução da câmera
- Diretórios de saída
- Configurações de texto e LaTeX
- FPS e qualidade de renderização

## Solução de Problemas

### Erro: "pangocairo >= 1.30.0 is required"
Instale as dependências de desenvolvimento do Pango:
```bash
sudo apt-get install libpango1.0-dev pkg-config
```

### Erro: "FFmpeg not found"
Certifique-se de que o FFmpeg está instalado e no PATH do sistema.

### Erro com LaTeX
Instale uma distribuição completa do LaTeX:
- Linux: `sudo apt-get install texlive-full`
- macOS: `brew install mactex`
- Windows: MiKTeX

## Recursos

- Documentação do ManimGL: https://3b1b.github.io/manim/
- Repositório do ManimGL: https://github.com/3b1b/manim
- Canal 3Blue1Brown: https://www.youtube.com/c/3blue1brown
