# Instalação e Configuração - visualization_llm

Este repositório agora está configurado para instalação fácil com `pip install -e .`

## 🚀 Instalação Rápida (3 Passos)

### 1️⃣ Instalar Dependências do Sistema

No seu terminal, execute:

```bash
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
```

> **Nota**: Isso instalará ~1-2GB de dependências (principalmente LaTeX)

### 2️⃣ Navegar para o Diretório do Projeto

```bash
cd /home/sakod/Documentos/Visualization_LLM/visualization_llm
```

### 3️⃣ Instalar o Pacote Python

```bash
pip install -e .
```

Isso instalará:
- ✅ manimgl (biblioteca de animação 3Blue1Brown)
- ✅ Todas as dependências Python (numpy, scipy, etc.)
- ✅ O repositório em modo editável (alterações refletem imediatamente)

## ✅ Verificar Instalação

Teste se tudo funcionou:

```bash
manimgl --version
```

Você deve ver algo como: `ManimGL v1.7.2`

## 🎬 Executar sua Primeira Animação

```bash
manimgl _2024/manim_demo/lorenz.py LorenzAttractor -p
```

Isso abrirá uma janela de preview com a animação do atrator de Lorenz!

## 📚 Comandos Úteis

```bash
# Preview sem renderizar (rápido)
manimgl arquivo.py NomeDaCena -p

# Renderizar em baixa qualidade (mais rápido)
manimgl arquivo.py NomeDaCena -l

# Renderizar em alta qualidade
manimgl arquivo.py NomeDaCena -h

# Modo interativo (como debugger) na linha 50
manimgl arquivo.py NomeDaCena -se 50

# Ver todas as opções
manimgl --help
```

## 🏗️ Estrutura do Projeto

```
visualization_llm/
├── _2015/ até _2025/        # Vídeos organizados por ano
├── custom/                  # Extensões customizadas do manim
│   ├── characters/          # Pi creature e animações
│   ├── backdrops.py         # Fundos e temas visuais
│   └── ...
├── once_useful_constructs/  # Utilitários legados
├── manim_imports_ext.py     # Import universal (use em todos os arquivos)
├── custom_config.yml        # Configurações do manim
├── setup.py                 # Configuração do pacote
└── README_PT.md            # Este arquivo
```

## 🎨 Desenvolvendo Animações

### Criar um Novo Arquivo de Animação

```python
from manim_imports_ext import *

class MinhaAnimacao(InteractiveScene):
    def construct(self):
        # Criar texto
        texto = Tex(R"E = mc^2")
        self.play(Write(texto))
        self.wait()

        # Criar círculo
        circulo = Circle(radius=2, color=BLUE)
        self.play(ShowCreation(circulo))
        self.wait()
```

### Executar

```bash
manimgl meu_arquivo.py MinhaAnimacao -p
```

## 🛠️ Modo Interativo (Desenvolvimento Iterativo)

O modo interativo permite testar código sem re-renderizar tudo:

```bash
manimgl arquivo.py NomeDaCena -se 10
```

Isso abre um shell IPython. Você pode:

1. Escrever código de animação no seu editor
2. Copiar para clipboard
3. No shell IPython, executar: `checkpoint_paste()`
4. Ver o resultado instantaneamente!

**Opções úteis:**
- `checkpoint_paste()` - Executa código do clipboard
- `checkpoint_paste(skip=True)` - Executa sem animação (instantâneo)
- `checkpoint_paste(record=True)` - Grava enquanto executa

## ⚙️ Configuração

O arquivo `custom_config.yml` controla:
- Resolução do vídeo (padrão: 4K)
- FPS (padrão: 30)
- Diretórios de saída
- Fontes e LaTeX

Para mais detalhes, veja `CONFIG.md`

## 🐛 Problemas Comuns

### Erro: `ModuleNotFoundError: No module named 'manim_imports_ext'`

**Solução**: Execute `pip install -e .` no diretório do projeto

### Erro: `OSError: libEGL.so: cannot open shared object file`

**Solução**: Instale as bibliotecas OpenGL:
```bash
sudo apt-get install -y libgl1-mesa-glx libgl1-mesa-dev libegl1-mesa libegl1-mesa-dev
```

### Erro: `pangocairo >= 1.30.0 is required`

**Solução**: Instale Pango:
```bash
sudo apt-get install -y libpango1.0-dev pkg-config
```

### Warning: `pkg_resources is deprecated`

Isso é apenas um aviso (não um erro). Pode ser ignorado.

## 📖 Documentação e Recursos

- **Guia de Instalação Detalhado**: `INSTALL.md`
- **Guia Rápido**: `QUICKSTART.md`
- **Configuração**: `CONFIG.md`
- **Documentação ManimGL**: https://3b1b.github.io/manim/
- **Repositório ManimGL**: https://github.com/3b1b/manim
- **Canal 3Blue1Brown**: https://www.youtube.com/c/3blue1brown

## 💡 Dicas

1. **Sempre comece com** `from manim_imports_ext import *` nos seus arquivos
2. **Use `-p`** para preview rápido durante desenvolvimento
3. **Use `-l`** (low quality) para testes rápidos
4. **Use `-h`** (high quality) apenas para renderização final
5. **Modo interativo** (`-se`) é excelente para experimentar!

## 🤝 Contribuindo

Este é o repositório pessoal do 3Blue1Brown. Para contribuir com a biblioteca Manim em si, veja:
- ManimGL (3b1b): https://github.com/3b1b/manim
- Manim Community: https://github.com/ManimCommunity/manim

## 📝 Notas

- Este repositório usa **ManimGL** (versão do 3Blue1Brown), não o Manim Community
- As configurações estão otimizadas para os workflows do 3Blue1Brown
- Algumas cenas podem ter dependências específicas (imagens, assets)

---

**Criado com** ❤️ **por Grant Sanderson (3Blue1Brown)**

**Configuração de instalação** 🔧 **atualizada em 2025**
