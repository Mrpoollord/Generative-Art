# 🎨 Procedural Hirst Painting Generator

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white) ![Library](https://img.shields.io/badge/Lib-Turtle-green) ![Category](https://img.shields.io/badge/Category-Generative_Art-orange)

### 📖 Overview
A Python-based **procedural generation engine** that replicates the famous "Spot Paintings" by contemporary artist Damien Hirst.

This project utilizes the Python `turtle` graphics module to programmatically render a symmetric grid of distinct colored dots. It demonstrates the application of **Cartesian coordinate systems**, **RGB color space manipulation**, and **algorithmic logic** to automate artistic creation.

### ⚙️ Technical Highlights
* **Coordinate Systems:** Manages agent positioning using explicit X/Y coordinate checks to handle row wrapping (carriage return logic).
* **RGB Color Space:** Implements `colormode(255)` to handle a custom palette of extracted RGB tuples.
* **Flow Control:** Replaces nested loops with a single linear loop and conditional logic for cleaner execution.

---

### 🚀 Usage

#### Prerequisites
* Python 3.12+ (Required for `.teleport()` method)
* Standard Library (no `pip install` required)

#### Running the script
1.  Clone the repository.
2.  Run the main script:

```bash
python main.py
