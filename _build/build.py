#!/usr/bin/env python3
"""Genera el sitio estático de umartidigital.com.

Uso:  python3 _build/build.py
Edita el contenido en _build/pages/ y los datos en este archivo; nunca los
.html generados en la raíz (se sobrescriben en cada build).
"""
import datetime
import html
import json
import pathlib

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
BASE = "https://www.umartidigital.com"
# True mientras el sitio vive en el subdominio provisorio: agrega "noindex"
# en todas las páginas. Cambiar a False el día del lanzamiento.
STAGING = True
EMAIL = "contacto@umartidigital.com"
# Número en formato internacional sin "+" ni espacios, ej. "5214421234567".
WHATSAPP = ""
WHATSAPP_MSG = "Hola, quiero conversar sobre la consultoría de Umarti Digital."
# URL pública de la Comunidad del marketplace, ej. "https://dominio.com/comunidad".
COMUNIDAD_URL = ""

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(__file__).resolve().parent
YEAR = datetime.date.today().year
VERSION = datetime.datetime.now().strftime("%Y%m%d%H%M")

e = html.escape

# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
# file=None -> página en preparación.
PAGES = [
    dict(path="/", file="home.html", nav="",
         title="Consultoría digital automotriz: procesos, IA y leads | Umarti Digital",
         og_title="Evolución digital para empresas de movilidad | Umarti Digital",
         description="Consultoría de transformación digital para concesionarios, agencias de autos, distribuidores de motos y camiones y grupos automotrices: procesos, automatización con IA y generación de leads."),
    dict(path="/servicios/", file="servicios.html", nav="servicios",
         title="Servicios de consultoría para concesionarios | Umarti Digital",
         description="Método Evolución Digital, automatización con IA, marketing y generación de leads, y gestión de proyectos para empresas de movilidad.",
         h1="Servicios de consultoría para la industria de la movilidad",
         lead="Se contratan por separado o juntos, como un programa de evolución digital completo."),
    dict(path="/servicios/evolucion-digital/", file="evolucion-digital.html", nav="servicios", parent="servicios",
         faq="EVOLUCION",
         title="Plan de transformación digital para concesionarias: método Evolución Digital | Umarti Digital",
         description="Plan de transformación digital y optimización tecnológica para concesionarios y grupos automotrices: relevamiento de procesos, roadmap, automatización, integración de sistemas e inteligencia de negocio.",
         h1="Plan de transformación digital: método Evolución Digital",
         lead="Diseñamos e implementamos procesos digitales que mejoran la eficiencia, ordenan la operación y hacen crecer el negocio, con una hoja de ruta clara de qué hacer primero.",
         crumb="Método Evolución Digital"),
    dict(path="/servicios/automatizacion-ia/", file="automatizacion-ia.html", nav="servicios", parent="servicios",
         faq="IA",
         title="Agentes conversacionales con IA y automatización de procesos para concesionarios | Umarti Digital",
         description="Agentes de inteligencia artificial para WhatsApp, web y redes que atienden, califican y dan seguimiento a leads 24/7, más automatización de cotizaciones, campañas e integración con CRM, DMS y ERP.",
         h1="Agentes conversacionales con IA y automatización de procesos",
         lead="Atienden, califican y dan seguimiento a tus clientes las 24 horas, en WhatsApp, web y redes, y convierten cada conversación en una acción concreta dentro de tu operación.",
         crumb="Automatización e IA"),
    dict(path="/servicios/marketing-leads/", file=None, nav="servicios", parent="servicios",
         title="Marketing digital y generación de leads para agencias de autos | Umarti Digital",
         description="Estrategia digital, campañas y canales conectados al CRM para generar y convertir leads en concesionarios.",
         h1="Marketing digital y generación de leads",
         lead="Campañas y canales conectados al proceso comercial, medidos hasta la venta."),
    dict(path="/servicios/gestion-proyectos/", file=None, nav="servicios", parent="servicios",
         title="Gestión de proyectos y producto digital | Umarti Digital",
         description="Priorización de iniciativas, Scrum, Kanban, OKRs y tableros para llevar proyectos digitales a producción.",
         h1="Gestión de proyectos y producto",
         lead="Del portafolio de iniciativas a los cambios funcionando en el día a día."),
    dict(path="/automotriz/agencias-de-autos/", file=None, nav="automotriz", parent="automotriz",
         title="Consultoría digital para agencias de autos y concesionarios | Umarti Digital",
         description="Más leads atendidos a tiempo, seguimiento comercial ordenado y showroom digital para agencias de autos.",
         h1="Consultoría digital para agencias de autos",
         lead="Más leads atendidos a tiempo y un showroom digital que convierte."),
    dict(path="/automotriz/motos/", file=None, nav="automotriz", parent="automotriz",
         title="Marketing y automatización para distribuidores de motos | Umarti Digital",
         description="Volumen de consultas, financiamiento y posventa sin perder prospectos: consultoría para distribuidores de motos.",
         h1="Consultoría digital para distribuidores de motos",
         lead="Volumen de consultas, financiamiento y posventa sin perder prospectos."),
    dict(path="/automotriz/camiones/", file=None, nav="automotriz", parent="automotriz",
         title="Consultoría digital para distribuidores de camiones y flotillas | Umarti Digital",
         description="Ciclos de venta B2B, cotizaciones complejas y seguimiento a cuentas para distribuidores de camiones.",
         h1="Consultoría digital para camiones y flotillas",
         lead="Ciclos B2B largos, cotizaciones complejas y seguimiento a cuentas."),
    dict(path="/automotriz/grupos-automotrices/", file=None, nav="automotriz", parent="automotriz",
         title="Transformación digital para grupos automotrices | Umarti Digital",
         description="Un solo proceso comercial en todas las sucursales y marcas, integración de sistemas y datos para decidir.",
         h1="Transformación digital para grupos automotrices",
         lead="Un solo proceso en todas las sucursales y marcas, con datos para decidir."),
    dict(path="/hub/", file="hub.html", nav="hub",
         title="Hub Evolución Digital Automotriz: análisis y tendencias | Umarti Digital",
         description="Análisis, guías y benchmarking internacional sobre la evolución digital de la industria automotriz, con debate en la Comunidad Umarti.",
         h1="Hub Evolución Digital Automotriz",
         lead="Análisis, guías y lo que está pasando en otros países. Cada tema se debate después con colegas en la Comunidad Umarti."),
    dict(path="/sobre-umarti/", file="sobre-umarti.html", nav="sobre",
         title="Sobre Umarti Digital: consultoría para la industria de la movilidad",
         description="Umarti Digital es una consultora de evolución digital para la industria de la movilidad, con oficinas en Querétaro, México y Ciudad de Buenos Aires, Argentina.",
         h1="Sobre Umarti",
         lead="Una consultora de evolución digital hecha desde adentro de la industria de la movilidad."),
    dict(path="/contacto/", file="contacto.html", nav="contacto", form=True,
         title="Contacto | Umarti Digital, Querétaro y Buenos Aires",
         description="Agenda una llamada de 20 minutos, escríbenos por WhatsApp o pide la presentación comercial de Umarti Digital.",
         h1="Conversemos", crumb="Contacto",
         lead="Cuéntanos dónde está hoy tu operación. Sin compromiso."),
    dict(path="/privacidad/", file=None, nav="",
         title="Aviso de privacidad | Umarti Digital",
         description="Aviso de privacidad de Umarti Digital.",
         h1="Aviso de privacidad",
         lead="Cómo tratamos los datos que nos compartes."),
]
PAGES[10]["form"] = True  # hub: formulario del newsletter

PARENTS = {
    "servicios": ("Servicios", "/servicios/"),
    "automotriz": ("Para quién", None),
}

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------
FAQ = [
    ("¿Qué hace una consultoría de transformación digital automotriz?",
     "Revisa cómo trabaja hoy una agencia o un grupo automotriz, desde que entra un lead hasta la entrega y la posventa, y define qué cambiar en procesos, tecnología y equipo para vender más y atender mejor. Después acompaña la implementación hasta que los cambios funcionan en el día a día."),
    ("¿Qué procesos de un concesionario se pueden automatizar con inteligencia artificial?",
     "Los más habituales son la primera respuesta a leads de WhatsApp, web y redes, la calificación y el seguimiento de prospectos, el agendamiento de pruebas de manejo y citas de servicio, el envío de cotizaciones, las encuestas de satisfacción y las campañas de recompra. No todo conviene automatizarlo: el diagnóstico define dónde la automatización realmente genera valor."),
    ("¿Necesito cambiar mi CRM o mi DMS?",
     "No necesariamente. Partimos de las herramientas que ya usas y proponemos cambiarlas solo cuando el diagnóstico lo justifica. Muchas mejoras se logran ordenando procesos e integrando los sistemas que ya existen."),
    ("¿Con qué tipo de empresas trabajan?",
     "Con concesionarios y grupos automotrices multimarca, distribuidores de motos, camiones y maquinaria agrícola, talleres y áreas de posventa, importadoras y otras empresas de movilidad de Latinoamérica y España."),
    ("¿Cómo empezamos?",
     "Con una llamada de 20 minutos para entender tu operación, o pidiendo la presentación comercial para ver los servicios y los proyectos en detalle. En ambos casos, sin compromiso."),
]

PAGE_FAQ = {
    "IA": [
        ("¿Qué diferencia hay entre un agente conversacional con IA y un chatbot?",
         "Un chatbot tradicional sigue un menú de opciones fijas. Un agente con inteligencia artificial entiende el contexto de la conversación, interpreta lo que la persona necesita, responde en lenguaje natural y además ejecuta acciones: registra el lead en el CRM, agenda una cita, envía una cotización o deriva a un asesor."),
        ("¿El agente reemplaza al vendedor o al asesor de servicio?",
         "No. Se ocupa de la primera respuesta, las preguntas repetitivas, la calificación y el seguimiento, y entrega al asesor un prospecto ya calificado y con el contexto de la conversación. El equipo dedica su tiempo a cerrar ventas y atender mejor."),
        ("¿En qué canales funciona?",
         "En WhatsApp, el sitio web, redes sociales como Instagram y Facebook, email y plataformas internas. Lo habitual es empezar por el canal donde hoy se pierden más consultas, que en la mayoría de las agencias es WhatsApp."),
        ("¿Se integra con mi CRM, DMS o ERP?",
         "Sí. El agente puede conectarse con CRM, ERP, DMS, calendarios, bases de datos y plataformas de marketing para registrar información y ejecutar acciones sin carga manual. En el diagnóstico definimos qué integraciones generan más valor."),
        ("¿Es difícil de usar para mi equipo?",
         "No. La interfaz es intuitiva y no requiere conocimientos técnicos. Acompañamos la puesta en marcha y capacitamos al equipo para que pueda revisar conversaciones, ajustar respuestas y medir resultados."),
        ("¿Qué plataforma de inteligencia artificial usan?",
         "No dependemos de una única herramienta. Seleccionamos la plataforma más adecuada para cada empresa junto a especialistas tecnológicos, según los canales, el volumen de conversaciones y los sistemas que ya usa."),
    ],
    "EVOLUCION": [
        ("¿Qué es un plan de transformación digital para una concesionaria?",
         "Es una hoja de ruta que define qué procesos digitalizar, qué automatizar, qué sistemas integrar y en qué orden, a partir de un diagnóstico de cómo trabaja hoy la agencia o el grupo. Cada etapa tiene entregables e indicadores para medir el avance."),
        ("¿Por dónde conviene empezar?",
         "Por el diagnóstico. Relevamos los procesos actuales, las herramientas y los resultados, y detectamos dónde se pierden más ventas o más tiempo. Con eso priorizamos las iniciativas de mayor impacto y menor esfuerzo."),
        ("¿Hay que cambiar todos los sistemas?",
         "No. Partimos de lo que ya funciona y proponemos cambios solo cuando el diagnóstico lo justifica. Muchas mejoras salen de ordenar procesos e integrar los sistemas existentes."),
        ("¿Sirve para un grupo con varias sucursales y marcas?",
         "Sí. Uno de los objetivos más frecuentes es homologar un solo proceso comercial y de posventa en todas las sucursales, con datos comparables entre marcas y puntos de venta."),
    ],
}


# Temas del Hub. "comunidad" es la categoría equivalente en la Comunidad Umarti.
HUB = [
    ("Customer Journey y Ventas", "¿Cómo compra hoy un cliente de 0 km?",
     "Del primer clic a la firma del contrato: dónde se informa, dónde compara y qué lo termina de convencer.", "autos"),
    ("Customer Journey y Ventas", "Funnel de venta: ¿dónde se caen más los leads?",
     "Las etapas donde más consultas se pierden en una concesionaria y cómo atacarlas.", "autos"),
    ("Tecnología e IA", "Agentes conversacionales: ¿reemplazan o potencian al vendedor?",
     "Qué funciona y qué no al usar IA para atender y calificar leads.", "autos"),
    ("Marketing y Contenido", "¿Vale más invertir en redes sociales o en portales?",
     "Dónde conviene poner el presupuesto de marketing según el tipo de agencia.", "autos"),
    ("Gestión y Operaciones", "Los indicadores que sí o sí deberías mirar cada semana",
     "Tiempo de respuesta, conversión por vendedor, rotación de stock: qué mirar y por qué.", "autos"),
    ("Radar internacional", "Qué están haciendo las concesionarias en España y Argentina",
     "Formatos, canales y tecnologías que ya funcionan en otros mercados de habla hispana.", "autos"),
]


# ---------------------------------------------------------------------------
# Componentes
# ---------------------------------------------------------------------------
def wa_link():
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(WHATSAPP_MSG)}"


def whatsapp_button():
    if WHATSAPP:
        return (f'<a class="btn btn--wa" href="{wa_link()}" target="_blank" rel="noopener">'
                'Escribir por WhatsApp</a>')
    return '<span class="btn btn--wa btn--off" aria-disabled="true">WhatsApp (número pendiente)</span>'


def whatsapp_footer():
    if WHATSAPP:
        return f'<a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp</a>'
    return ""


def faq_html(items=None):
    return "\n".join(
        f"        <details>\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>"
        for q, a in (items or FAQ))


def hub_cards(n=None):
    out = []
    for cat, title, summary, comunidad in HUB[:n]:
        if COMUNIDAD_URL:
            debate = (f'<a class="topic__debate" href="{COMUNIDAD_URL.rstrip("/")}/{comunidad}" '
                      'target="_blank" rel="noopener">Sumarme al debate en la Comunidad</a>')
        else:
            debate = '<span class="topic__debate topic__debate--off">Debate en la Comunidad Umarti</span>'
        out.append(f"""        <article class="topic">
          <p class="topic__cat">{e(cat)}</p>
          <h3>{e(title)}</h3>
          <p>{e(summary)}</p>
          <div class="topic__foot">
            <span class="badge">Próximamente</span>
            {debate}
          </div>
        </article>""")
    return "\n".join(out)


def crumbs(page):
    items = [("Inicio", "/")]
    if page.get("parent"):
        name, url = PARENTS[page["parent"]]
        items.append((name, url))
    items.append((page.get("crumb", page["h1"]), page["path"]))
    return items


def page_header(page):
    parts = []
    items = crumbs(page)
    for i, (name, url) in enumerate(items):
        last = i == len(items) - 1
        if last or url is None:
            attr = ' aria-current="page"' if last else ""
            parts.append(f"<span{attr}>{e(name)}</span>")
        else:
            parts.append(f'<a href="{url}">{e(name)}</a>')
    trail = ' <span class="crumbs__sep" aria-hidden="true">/</span> '.join(parts)
    return f"""  <section class="page-head">
    <div class="wrap">
      <nav class="crumbs" aria-label="Ruta">{trail}</nav>
      <h1>{e(page["h1"])}</h1>
      <p class="page-head__lead">{e(page["lead"])}</p>
    </div>
  </section>"""


def cta_band():
    wa = ""
    if WHATSAPP:
        wa = f'<a class="link" href="{wa_link()}" target="_blank" rel="noopener">o escríbenos por WhatsApp</a>'
    return f"""  <section class="cta-band">
    <div class="wrap cta-band__inner">
      <div>
        <h2>¿Dónde está hoy tu operación?</h2>
        <p>Una llamada de 20 minutos para entenderla y ver por dónde empezar. Sin compromiso.</p>
      </div>
      <div class="cta-band__actions">
        <a href="/contacto/" class="btn">Agendar una llamada</a>
        {wa}
      </div>
    </div>
  </section>"""


def placeholder(page):
    return f"""{page_header(page)}

  <section class="section section--tight">
    <div class="wrap">
      <div class="wip">
        <p class="eyebrow eyebrow--dark">En preparación</p>
        <p>Estamos escribiendo esta página. Mientras tanto, puedes ver <a href="/servicios/">todos los servicios</a> o <a href="/contacto/">agendar una llamada</a>.</p>
      </div>
    </div>
  </section>

{cta_band()}"""


# ---------------------------------------------------------------------------
# Datos estructurados
# ---------------------------------------------------------------------------
def org_ld():
    data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": f"{BASE}/#organizacion",
        "name": "Umarti Digital",
        "url": f"{BASE}/",
        "logo": f"{BASE}/assets/img/umarti-logo.png",
        "image": f"{BASE}/assets/img/umarti-logo.png",
        "email": EMAIL,
        "description": "Consultoría de evolución digital para la industria de la movilidad: procesos, automatización con IA y generación de leads.",
        "areaServed": ["MX", "AR", "Latinoamérica", "ES"],
        "knowsAbout": ["Consultoría automotriz", "Transformación digital", "Automatización de procesos",
                       "Agentes conversacionales con IA", "CRM para concesionarios", "Generación de leads"],
        "address": [
            {"@type": "PostalAddress", "addressLocality": "Querétaro", "addressRegion": "Querétaro", "addressCountry": "MX"},
            {"@type": "PostalAddress", "addressLocality": "Ciudad de Buenos Aires", "addressCountry": "AR"},
        ],
        "founder": {"@type": "Person", "name": "Marcelo"},
    }
    if WHATSAPP:
        data["telephone"] = f"+{WHATSAPP}"
    return data


def breadcrumb_ld(page):
    items = [(n, u) for n, u in crumbs(page) if u]
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{BASE}{u}"}
            for i, (n, u) in enumerate(items)
        ],
    }


def faq_ld(items=None):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in (items or FAQ)
        ],
    }


def service_ld(page):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": page.get("crumb", page["h1"]),
        "description": page["description"],
        "url": f"{BASE}{page['path']}",
        "serviceType": page.get("crumb", page["h1"]),
        "provider": {"@id": f"{BASE}/#organizacion"},
        "areaServed": ["MX", "AR", "Latinoamérica", "ES"],
        "audience": {"@type": "BusinessAudience", "audienceType": "Concesionarios, grupos automotrices y distribuidores de motos y camiones"},
    }


def ld_tags(blocks):
    return "".join(
        '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + "</script>\n"
        for b in blocks)


FORM_SCRIPT = """<script>
  (function () {
    var q = new URLSearchParams(location.search);
    var ok = document.getElementById('form-ok'), err = document.getElementById('form-error');
    if (ok && q.get('enviado') === '1') ok.hidden = false;
    if (err && q.get('enviado') === '0') err.hidden = false;
    var interes = document.getElementById('interes');
    if (interes && q.get('interes')) interes.value = q.get('interes');
  })();
</script>"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def render(page, layout, content=None):
    if content is not None:
        pass
    elif page["file"]:
        content = (SRC / "pages" / page["file"]).read_text(encoding="utf-8")
    else:
        content = placeholder(page)

    content = (content
               .replace("{{page_header}}", page_header(page) if page["path"] != "/" else "")
               .replace("{{cta_band}}", cta_band())
               .replace("{{faq_html}}", faq_html(PAGE_FAQ.get(page.get("faq"))))
               .replace("{{hub_cards_3}}", hub_cards(3))
               .replace("{{hub_cards_all}}", hub_cards())
               .replace("{{whatsapp_button}}", whatsapp_button())
               .replace("{{email}}", EMAIL))

    ld = []
    if page["path"] in ("/", "/contacto/", "/sobre-umarti/"):
        ld.append(org_ld())
    if page["path"] == "/":
        ld.append(faq_ld())
    else:
        ld.append(breadcrumb_ld(page))
    if page.get("parent") == "servicios":
        ld.append(service_ld(page))
    if page.get("faq"):
        ld.append(faq_ld(PAGE_FAQ[page["faq"]]))

    nav = page.get("nav", "")
    cur = ' aria-current="page"'
    out = (layout
           .replace("{{title}}", e(page["title"]))
           .replace("{{og_title}}", e(page.get("og_title", page["title"])))
           .replace("{{description}}", e(page["description"]))
           .replace("{{robots}}", '<meta name="robots" content="noindex, nofollow">\n' if (STAGING or page.get("noindex")) else "")
           .replace("{{url}}", f"{BASE}{page['path']}")
           .replace("{{base}}", BASE)
           .replace("{{version}}", VERSION)
           .replace("{{jsonld}}", ld_tags(ld))
           .replace("{{body_class}}", "page-home" if page["path"] == "/" else "page-inner")
           .replace("{{cur_servicios}}", cur if nav == "servicios" else "")
           .replace("{{cur_automotriz}}", cur if nav == "automotriz" else "")
           .replace("{{cur_hub}}", cur if nav == "hub" else "")
           .replace("{{cur_sobre}}", cur if nav == "sobre" else "")
           .replace("{{email}}", EMAIL)
           .replace("{{whatsapp_footer}}", whatsapp_footer())
           .replace("{{year}}", str(YEAR))
           .replace("{{scripts}}", FORM_SCRIPT if page.get("form") else "")
           .replace("{{content}}", content))
    assert "{{" not in out, f"Marcador sin reemplazar en {page['path']}"
    return out


def main():
    layout = (SRC / "layout.html").read_text(encoding="utf-8")
    for page in PAGES:
        target = ROOT / page["path"].strip("/") / "index.html" if page["path"] != "/" else ROOT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page, layout), encoding="utf-8")

    # 404
    p404 = dict(path="/404/", nav="", file=None, noindex=True, h1="No encontramos esta página",
                lead="Puede que la dirección haya cambiado con el nuevo sitio.",
                title="Página no encontrada | Umarti Digital", description="Página no encontrada.")
    body = page_header(p404) + """
  <section class="section section--tight"><div class="wrap"><p><a class="btn" href="/">Ir al inicio</a></p></div></section>"""
    (ROOT / "404.html").write_text(render(p404, layout, body), encoding="utf-8")

    today = datetime.date.today().isoformat()
    urls = "\n".join(f"  <url>\n    <loc>{BASE}{p['path']}</loc>\n    <lastmod>{today}</lastmod>\n  </url>"
                     for p in PAGES)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n",
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    print(f"OK: {len(PAGES)} páginas + 404, sitemap y robots. STAGING={STAGING}")


if __name__ == "__main__":
    main()
