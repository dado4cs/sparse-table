# Proyecto Final: Anima tu Estructura de Datos — Sparse Table

**Curso:** CS2023 - Algoritmos y Estructuras de Datos  
**Estructura Asignada:** Sparse Table (Tabla Dispersa)  
**Integrantes:**
- Maxwell Lupo Gregorio Collazos Solis
- Renzo Vladimir Cuba Zari
- José Luis Villalobos Jiménez
## Descripción del Proyecto

Este repositorio contiene el código fuente para generar un video educativo y animado sobre la estructura de datos **Sparse Table**. La animación ha sido desarrollada utilizando **Manim** en Python.

## Enlaces importantes
- Video del proyecto: 
- Informe en docs: 

---
## Archivos del Proyecto

El código está modularizado en varias escenas para facilitar el renderizado:
- `estructura.py`: Implementación de una Sparse Table para consultar mínimos.
- `visual_utils.py`: Archivos gráficos compartidos entre módulos.
- `escena1_intro.py`: Presentación, conceptos teóricos y pseudocódigo.
- `escena2_construccion.py`: Animación de el algoritmo con un arreglo de ejemplo.
- `escena3_consultas.py`: Ejecución de consultas sobre dicho arreglo de ejemplo.
- `escena4_complejidad.py`: Análisis de la complejidad temporal del algoritmo.
---

## Software Requerido

Para renderizar las animaciones, se necesita:
1. **Python 3.10** o superior.
2. **Manim Community** (`manim`).
3. **LaTeX** (`texlive` o similar) instalado en tu sistema
---

## Pasos para Compilar / Ejecutar el Código

Se puede compilar los videos usando el gestor de paquetes moderno `uv` (forma recomendada por rapidez) o utilizando el gestor tradicional `pip`.

### Opción A: Usando `uv` (Recomendado)

1. Crear el entorno y activarlo
   ```bash
   uv venv
   source .venv/bin/activate   # En Linux/Mac
   # .venv\Scripts\activate    # En Windows
   uv pip install manim
   ```

2. Para compilar las escenas en alta resolución (1080p, 60fps):
   ```bash
   uv run manim render -qh escena1_intro.py Escena1_Intro
   uv run manim render -qh escena2_construccion.py Escena2_Construccion
   uv run manim render -qh escena3_consultas.py Escena3_Consultas
   uv run manim render -qh escena4_complejidad.py Escena4_Complejidad
   ```

### Opción B: Usando `pip` (Clásico)

1. Crear el entorno y activarlo
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # En Linux/Mac
   # .venv\Scripts\activate    # En Windows
   pip install manim
   ```

   ```bash
   manim render -qh escena1_intro.py Escena1_Intro
   manim render -qh escena2_construccion.py Escena2_Construccion
   manim render -qh escena3_consultas.py Escena3_Consultas
   manim render -qh escena4_complejidad.py Escena4_Complejidad
   ```

---
*Nota: Los videos renderizados se guardarán automáticamente en la carpeta `media/videos/` dentro de este mismo directorio. Para pruebas rápidas a menor calidad, cambiar el flag `-qh` por `-ql` (480p, 15fps).*
