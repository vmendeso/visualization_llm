# Guia Rápido de Instalação

## Instalação em 2 Passos

### 1. Instalar Dependências do Sistema

**Linux/macOS (Automático):**
```bash
./install_system_deps.sh
```

**OU Manualmente:**

Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install -y libpango1.0-dev pkg-config python3-dev ffmpeg libcairo2-dev texlive
```

macOS:
```bash
brew install ffmpeg mactex pango pkg-config cairo
```

### 2. Instalar o Pacote Python

```bash
pip install -e .
```

Pronto! ✅

## Testar a Instalação

```bash
manimgl --version
```

## Usar uma Cena

```bash
manimgl nome_do_arquivo.py NomeDaCena -p
```

## Mais Informações

- **Instruções Detalhadas**: Veja `INSTALL.md`
- **Uso do ManimGL**: `manimgl --help`
- **Documentação**: https://3b1b.github.io/manim/

## Estrutura do Projeto

```
visualization_llm/
├── _YYYY/           # Vídeos por ano
├── custom/          # Extensões customizadas
├── playground.py    # Arquivo para testes
├── manim_imports_ext.py  # Imports universais
└── custom_config.yml     # Configuração do manim
```

## Comandos Úteis

```bash
# Renderizar uma cena
manimgl arquivo.py NomeDaCena

# Preview sem renderizar
manimgl arquivo.py NomeDaCena -p

# Modo interativo (como debugger)
manimgl arquivo.py NomeDaCena -se 10

# Desenvolvimento interativo
checkpoint_paste()  # No modo interativo
```

## Solução Rápida de Problemas

**Erro de pangocairo?**
```bash
sudo apt-get install libpango1.0-dev pkg-config
```

**Erro de FFmpeg?**
```bash
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```

**Erro de LaTeX?**
```bash
sudo apt-get install texlive-full  # Linux
brew install mactex                # macOS
```
