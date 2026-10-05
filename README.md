# umartidigital.com · Sitio de la consultora

Sitio estático de Umarti Digital, publicado en Hostinger con despliegue desde GitHub (igual que la landing `umarti-landing`).

## Cómo se edita
- El contenido vive en `_build/pages/` (una página por archivo) y los datos (páginas, títulos SEO, preguntas frecuentes, temas del Hub, WhatsApp) en `_build/build.py`.
- Después de editar: `python3 _build/build.py`. Eso regenera los `index.html`, `sitemap.xml` y `robots.txt`. No editar los `.html` generados a mano.
- Estilos: `assets/css/styles.css` (misma base visual que la landing).
- `contact.php`: recibe el formulario de contacto y el del newsletter del Hub.

## Lanzamiento (pasar de provisorio a www)
1. `STAGING = False` en `_build/build.py` y volver a generar.
2. Borrar el bloque "STAGING" de `.htaccess`.
3. Apuntar `www.umartidigital.com` a este sitio en Hostinger (sin tocar los registros del correo).
4. Enviar `sitemap.xml` en Google Search Console y Bing Webmaster Tools.

## Regla de contenido
No publicar nombres de clientes ni de partners.
