# 🤖 Proyecto de Navegación ROS 2 - IngenIA

Este repositorio contiene el entorno de simulación y la configuración de navegación para el robot **TIAGo** (PAL Robotics), desarrollado como parte del proyecto **IngenIA**. El objetivo principal es la creación de un entorno doméstico dinámico para pruebas de **SLAM (Mapeo)**, localización y navegación autónoma.

## 🚀 Características del Escenario (`car.world`)
El mundo de simulación ha sido diseñado con 5 mesas de prueba estratégicamente distribuidas. Sobre estas superficies se han colocado objetos con propiedades específicas para validar algoritmos de visión artificial y sensores láser:

| Objeto | Ubicación (X, Y, Z) | Propósito |
| :--- | :--- | :--- |
| **🕶️ Gafas de sol** | `(-2.0, -2.0, 0.8)` | Objeto pequeño de baja reflectividad para láser. |
| **💧 Botella de agua** | `(-2.0, 2.0, 0.8)` | Geometría vertical para pruebas de aproximación. |
| **🔴 Taza Roja** | `(-2.0, -7.0, 0.8)` | **Target principal** para segmentación por color (HSV). |
| **📘 Libro (Gris)** | `(-2.0, 8.0, 0.8)` | Textura plana (`Gazebo/DarkGrey`) para reconocimiento. |
| **🎾 Pelota de tenis** | `(-2.0, 13.0, 0.8)` | Pruebas de fricción y detección de esferas. |

---

## 🗺️ El Mapa del CAR
El sistema utiliza el stack de **Nav2** y **Slam Toolbox** para gestionar la información espacial:
1.  **Generación:** El mapa se construye mediante el LiDAR del robot mientras es operado manualmente.
2.  **Mapa del CAR:** El resultado es un mapa de ocupación (`.pgm` y `.yaml`) que define las zonas seguras de navegación y la posición de las mesas.
3.  **Localización:** Implementación de **AMCL** para situar al TIAGo con precisión dentro del mapa.

---

## 🛠️ Operación y Comandos Rápidos

Para facilitar la ejecución y el desarrollo del proyecto, se ha incluido un archivo llamado **`comandos.txt`** en la raíz del repositorio. En él encontrarás:

* **Lanzamiento:** Comandos para abrir el mundo en Gazebo con el TIAGo.
* **Operación:** Instrucciones para el Teleop y la visualización en RViz2.
* **Mapeo:** Pasos detallados para generar y guardar el **Mapa del CAR**.
* **Gestión de Git:** La "súper línea" para añadir, hacer commit y subir cambios al repositorio con un solo comando.

### Uso básico:
```bash
# Ver los comandos útiles en la terminal
cat comandos.txt

# Compilación inicial
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash# Mi Proyecto ROS 2 con TIAGo
Simulación en Gazebo con objetos domésticos y mesas.
