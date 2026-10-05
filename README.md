# Radar 25 NM

Aplicación web de radar que muestra aeronaves cercanas y permite centrar la pantalla en tu ubicación actual o en coordenadas personalizadas.

## ¿Qué hace?

- Carga datos ADS-B desde varios proveedores.
- Muestra aeronaves dentro de 25 NM del centro elegido.
- Dibuja un barrido, estela, detalles del avión y filtrado por altitud.
- Usa un proxy local en Python para evitar problemas de CORS.

## Cómo ejecutarlo localmente

1. Abre una terminal en la carpeta del proyecto.
2. Inicia el servidor local:

```bash
python3 server.py
```

3. Abre esta URL en el navegador:

```text
http://localhost:8000/radar.html
```

## Cómo usar la app

- Pulsa `Mi ubicación` para usar la geolocalización del navegador.
- O introduce latitud y longitud manualmente y pulsa `Usar coordenadas`.
- Ajusta los controles:
  - Barrido: velocidad del barrido del radar
  - Estela: longitud de la estela
  - Altitud máx: altitud máxima mostrada
- Haz clic en cualquier marcador para ver los detalles del avión.

## Archivos

- `radar.html`: interfaz del radar y lógica de dibujo
- `server.py`: proxy local para recuperar datos ADS-B desde fuentes externas

## Notas

- La aplicación requiere un servidor local. Abrir el archivo HTML directamente puede fallar por restricciones del navegador.
- Si una fuente de datos no responde, intenta la siguiente automáticamente.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
