# 🔧 Como Resolver o Erro: "No module named 'manim_imports_ext'"

## O Problema

O erro acontece porque o Python não consegue encontrar o módulo `manim_imports_ext.py` que está no repositório.

## ✅ Solução

No seu terminal, execute os seguintes comandos:

### 1. Ativar seu ambiente virtual (se ainda não estiver ativo)

```bash
# Para pyenv
pyenv activate llm_study

# OU para venv
source /caminho/para/llm_study/bin/activate
```

### 2. Navegar para o diretório do projeto

```bash
cd /home/sakod/Documentos/Visualization_LLM/visualization_llm
```

### 3. Instalar o pacote em modo editável

```bash
pip install -e .
```

Isso vai:
- ✅ Tornar `manim_imports_ext.py` acessível de qualquer lugar
- ✅ Instalar todas as dependências Python necessárias
- ✅ Permitir que você edite arquivos e as mudanças reflitam imediatamente

### 4. Testar

```bash
manimgl attention.py AttentionPatterns -p
```

## ⚠️ Importante

**Você precisa fazer isso PARA CADA ambiente virtual que usar!**

Se você trocar de ambiente virtual (de `vision_llm` para `llm_study`, por exemplo), precisa executar `pip install -e .` novamente nesse novo ambiente.

## 🔍 Como Verificar se Funcionou

Depois de instalar, teste se o módulo está acessível:

```bash
python -c "from manim_imports_ext import *; print('✅ Módulo encontrado!')"
```

Se ver "✅ Módulo encontrado!", está tudo certo!

## 📝 Sobre o pip install -e .

O flag `-e` significa "editable" (editável). Isso cria um link simbólico do código do repositório para o site-packages do Python, permitindo que:

1. Você edite os arquivos no repositório
2. As mudanças reflitam imediatamente (sem reinstalar)
3. O Python encontre os módulos do repositório de qualquer lugar

## 🐛 Se Ainda Não Funcionar

Verifique se você está no ambiente virtual correto:

```bash
which python
# Deve mostrar: /home/sakod/.pyenv/versions/3.12.5/envs/llm_study/bin/python
```

Verifique se está no diretório correto:

```bash
pwd
# Deve mostrar: /home/sakod/Documentos/Visualization_LLM/visualization_llm
```

Verifique se o setup.py existe:

```bash
ls setup.py
# Deve mostrar: setup.py
```

---

**Resumo rápido:**

```bash
cd /home/sakod/Documentos/Visualization_LLM/visualization_llm
pip install -e .
manimgl attention.py AttentionPatterns -p
```
