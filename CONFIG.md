# Configuração do custom_config.yml

Este arquivo explica como configurar o `custom_config.yml` para seu ambiente local.

## Problema Comum: Caminhos Hardcoded

O arquivo `custom_config.yml` original contém caminhos específicos do sistema do Grant (criador do 3Blue1Brown). Isso causa erros como:

```
ValueError: '/seu/caminho/arquivo.py' is not in the subpath of '/Users/grant/cs/videos'
```

## Solução

### Opção 1: Usar Configuração Padrão (Recomendado)

Os caminhos hardcoded já foram comentados no arquivo. O manimgl usará os diretórios padrão:
- Saída de vídeos: `~/manim_videos/`
- Downloads: `~/manim_downloads/`

Nenhuma configuração adicional é necessária.

### Opção 2: Configurar Caminhos Personalizados

Se você quiser especificar seus próprios diretórios, edite o `custom_config.yml`:

```yaml
directories:
  # Descomente e ajuste se você quiser usar mirror_module_path
  # mirror_module_path: True
  # removed_mirror_prefix: "/caminho/para/seu/repositorio"

  # Diretório base para assets e saída
  # base: "/caminho/para/seus/arquivos"

  subdirs:
    raster_images: "images/raster"
    vector_images: "images/vector"
    pi_creature_images: "images/pi_creature/svg"
    downloads: "manim_downloads"
```

### Opção 3: Usar Arquivo de Configuração Local

Você pode criar um arquivo `local_config.yml` que sobrescreve as configurações:

```yaml
# local_config.yml
directories:
  output_directory: "/seu/caminho/de/saida"
```

E executar:
```bash
manimgl arquivo.py NomeDaCena --config_file local_config.yml -p
```

## Configurações Disponíveis

### Janela de Preview
```yaml
window:
  position_string: UR  # UL, UR, DL, DR (cantos da tela)
  monitor_index: 0     # Monitor para exibir (0, 1, 2, ...)
  full_screen: False   # Modo tela cheia
```

### Câmera/Vídeo
```yaml
camera:
  resolution: (3840, 2160)  # 4K - ajuste conforme necessário
  background_color: "#000000"
  fps: 30
  background_opacity: 1.0
```

Resoluções comuns:
- 1080p: `(1920, 1080)`
- 4K: `(3840, 2160)`
- 720p: `(1280, 720)`

### Texto e LaTeX
```yaml
text:
  font: "CMU Serif"  # Fonte padrão para texto
  alignment: "CENTER"

tex:
  template: "default"  # Template LaTeX
```

### File Writer
```yaml
file_writer:
  saturation: 1.5  # Saturação de cor (1.0 = normal)
```

### Modo Interativo
```yaml
embed:
  autoreload: True  # Recarregar automaticamente módulos no modo interativo

ignore_manimlib_modules_on_reload: True
```

## Arquivo de Exemplo Completo

```yaml
# Exemplo de custom_config.yml funcional

directories:
  subdirs:
    raster_images: "images/raster"
    vector_images: "images/vector"
    pi_creature_images: "images/pi_creature/svg"
    downloads: "manim_downloads"

universal_import_line: "from manim_imports_ext import *"

window:
  position_string: UR
  monitor_index: 0
  full_screen: False

camera:
  resolution: (1920, 1080)  # 1080p para desenvolvimento mais rápido
  background_color: "#000000"
  fps: 30
  background_opacity: 1.0

file_writer:
  saturation: 1.5

text:
  font: "CMU Serif"
  alignment: "CENTER"

tex:
  template: "default"

embed:
  autoreload: True

ignore_manimlib_modules_on_reload: True
```

## Testando a Configuração

Após ajustar o `custom_config.yml`, teste com:

```bash
manimgl playground.py TestScene -p
```

Se não houver erros, sua configuração está correta!

## Ignorar Configuração Customizada

Para usar apenas as configurações padrão do manimgl (ignorando custom_config.yml):

```bash
manimgl arquivo.py NomeDaCena -p --config_file ""
```

## Referências

- Documentação do ManimGL: https://3b1b.github.io/manim/
- Configurações padrão: https://github.com/3b1b/manim/blob/master/manimlib/default_config.yml
