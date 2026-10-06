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
EMAIL = "hola@umartidigital.com"
# Número en formato internacional sin "+" ni espacios, ej. "5214421234567".
WHATSAPP = "524425307129"
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
         title="Consultoría digital automotriz, movilidad e inmobiliaria: procesos e IA | Umarti Digital",
         og_title="Evolución digital para empresas de movilidad | Umarti Digital",
         description="Consultoría de evolución digital para concesionarios, grupos automotrices, distribuidores de motos y camiones e inmobiliarias: procesos, automatización con IA y gestión digital de ventas."),
    dict(path="/servicios/", file="servicios.html", nav="servicios",
         title="Servicios de consultoría digital: procesos, IA, ventas y software | Umarti Digital",
         description="Método Evolución Digital, automatización con IA, gestión digital de ventas, desarrollo de nuevos productos y Software Factory y Staffing para empresas automotrices, de movilidad e inmobiliarias.",
         h1="Servicios de consultoría digital", crumb="Servicios",
         lead="Se contratan por separado o juntos, como un programa de evolución digital completo."),
    dict(path="/servicios/evolucion-digital/", file="evolucion-digital.html", nav="servicios", parent="servicios",
         faq="EVOLUCION",
         title="Plan de transformación digital: método Evolución Digital | Umarti Digital",
         description="Plan de transformación digital y optimización tecnológica para empresas automotrices, de movilidad e inmobiliarias: relevamiento de procesos, roadmap, automatización, integración de sistemas e inteligencia de negocio.",
         h1="Plan de transformación digital: método Evolución Digital",
         lead="Diseño e implemento procesos digitales que mejoran la eficiencia, ordenan la operación y hacen crecer el negocio, con una hoja de ruta clara de qué hacer primero.",
         crumb="Método Evolución Digital"),
    dict(path="/servicios/automatizacion-ia/", file="automatizacion-ia.html", nav="servicios", parent="servicios",
         faq="IA",
         title="Agentes conversacionales con IA y automatización de procesos | Umarti Digital",
         description="Agentes de inteligencia artificial para WhatsApp, web y redes que atienden, califican y dan seguimiento a leads 24/7 en concesionarios e inmobiliarias, más automatización de cotizaciones, campañas e integración con CRM y ERP.",
         h1="Agentes conversacionales con IA y automatización de procesos",
         lead="Atienden, califican y dan seguimiento a tus clientes las 24 horas, en WhatsApp, web y redes, y convierten cada conversación en una acción concreta dentro de tu operación.",
         crumb="Automatización e IA"),
    dict(path="/servicios/gestion-digital-ventas/", file=None, nav="servicios", parent="servicios",
         title="Gestión digital de ventas: CRM, leads y embudo comercial | Umarti Digital",
         description="Consultoría en gestión digital de ventas: canales, CRM, seguimiento de leads, campañas y métricas del embudo hasta el cierre.",
         h1="Gestión digital de ventas",
         lead="Ordeno el proceso comercial digital de punta a punta, para que cada lead tenga dueño y se mida hasta la venta.",
         crumb="Gestión digital de ventas"),
    dict(path="/servicios/desarrollo-nuevos-productos/", file=None, nav="servicios", parent="servicios",
         title="Desarrollo de nuevos productos y unidades de negocio | Umarti Digital",
         description="Diseño y lanzamiento de nuevos productos, unidades de negocio y MVPs digitales, con su estrategia comercial y gestión del proyecto.",
         h1="Desarrollo de nuevos productos",
         lead="De la idea al lanzamiento: nuevos productos, formatos y unidades de negocio, con su estrategia comercial.",
         crumb="Desarrollo de nuevos productos"),
    dict(path="/servicios/software-factory-staffing/", file=None, nav="servicios", parent="servicios",
         title="Software Factory y Staffing tecnológico | Umarti Digital",
         description="Desarrollo de software a medida y perfiles tecnológicos que se suman a tu equipo, coordinados por un solo interlocutor.",
         h1="Software Factory y Staffing",
         lead="Desarrollo de software a medida y talento tecnológico que se suma a tu equipo, con un solo interlocutor.",
         crumb="Software Factory y Staffing"),
    dict(path="/industrias/", file="industrias.html", nav="industrias",
         title="Industrias: automotriz, motos, camiones, maquinaria e inmobiliarias | Umarti Digital",
         description="Consultoría de evolución digital especializada en la industria automotriz, y aplicada a distribuidores de motos, camiones y maquinaria, posventa, importadoras e inmobiliarias.",
         h1="Para quién trabajo",
         lead="Me especializo en la industria automotriz. Y llevo el mismo método a otros negocios donde vender y atender bien lo es todo.",
         crumb="Para quién"),
    dict(path="/industrias/automotriz/", file=None, nav="industrias", parent="industrias",
         title="Consultoría automotriz para concesionarios y grupos automotrices | Umarti Digital",
         description="Consultoría automotriz: procesos, automatización con IA y gestión digital de ventas para agencias de autos, concesionarios y grupos automotrices en México, Argentina y Latinoamérica.",
         h1="Consultoría automotriz para concesionarios y grupos automotrices",
         lead="Para agencias de autos, concesionarios y grupos automotrices que quieren vender más y atender mejor.",
         crumb="Automotriz"),
    dict(path="/hub/", file="hub.html", nav="hub", form=True,
         title="Hub Evolución Digital Automotriz: análisis y tendencias | Umarti Digital",
         description="Análisis, guías y benchmarking internacional sobre la evolución digital de la industria automotriz, con debate en la Comunidad Umarti.",
         h1="Hub Evolución Digital Automotriz",
         lead="Análisis, guías y lo que está pasando en otros países. Cada tema se debate después con colegas en la Comunidad Umarti."),
    dict(path="/sobre-umarti/", file="sobre-umarti.html", nav="sobre",
         title="Sobre Umarti Digital: consultoría de evolución digital",
         description="Umarti Digital es la marca de consultoría de Marcelo, con 20 años en la industria de la movilidad, en Querétaro, México y Ciudad de Buenos Aires, Argentina.",
         h1="Sobre Umarti",
         lead="Consultoría de evolución digital hecha desde adentro de la industria de la movilidad."),
    dict(path="/contacto/", file="contacto.html", nav="contacto", form=True,
         title="Contacto | Umarti Digital, Querétaro y Buenos Aires",
         description="Agenda una llamada de 20 minutos, escríbeme por WhatsApp o pide mi presentación comercial. Querétaro, México y Ciudad de Buenos Aires, Argentina.",
         h1="Conversemos", crumb="Contacto",
         lead="Cuéntame dónde está hoy tu operación. Sin compromiso."),
    dict(path="/privacidad/", file=None, nav="",
         title="Aviso de privacidad | Umarti Digital",
         description="Aviso de privacidad de Umarti Digital.",
         h1="Aviso de privacidad",
         lead="Cómo tratamos los datos que nos compartes."),
]

PARENTS = {
    "servicios": ("Servicios", "/servicios/"),
    "industrias": ("Para quién", "/industrias/"),
    "hub": ("Hub", "/hub/"),
}

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------
FAQ = [
    ("¿Qué sucede si ya tengo un equipo trabajando en iniciativas digitales?",
     "Mi objetivo es ayudar a identificar y llevar adelante iniciativas comerciales, digitales y tecnológicas que generen impacto en el negocio. Muchas veces trabajo junto a equipos internos que ya tienen la agenda completa, como apoyo en un proyecto puntual, con un diagnóstico independiente o con un análisis de su estrategia digital actual."),
    ("¿De qué manera puedes colaborar con mi empresa?",
     "Colaboro estratégicamente mapeando un proceso actual, diseñando un nuevo proceso, homologando procesos, diseñando una experiencia de cliente phygital (para que la experiencia física y la digital funcionen coordinadas) o una nueva unidad de negocio, o como brazo externo para acelerar una implementación. A su vez, trabajo con partners especializados en inteligencia artificial, automatización, desarrollo tecnológico y generación de demanda."),
    ("¿Necesito cambiar mis plataformas tecnológicas?",
     "No necesariamente. Parto de las herramientas que ya usas, como el CRM, el DMS o el ERP, y propongo cambiarlas solo cuando el diagnóstico lo justifica. Muchas mejoras se logran ordenando procesos e integrando los sistemas que ya existen."),
    ("¿Qué procesos se pueden automatizar con inteligencia artificial?",
     "Los más habituales son la primera respuesta a consultas de WhatsApp, web y redes, la calificación y el seguimiento de prospectos, el agendamiento de citas, pruebas de manejo o visitas, el envío de cotizaciones, las encuestas de satisfacción y las campañas de recompra o reactivación. No todo conviene automatizarlo: el diagnóstico define dónde la automatización realmente genera valor."),
    ("¿Cómo se gestionan las iniciativas?",
     "Cada iniciativa parte de un diagnóstico y de un objetivo medible. Las priorizo según impacto y esfuerzo, las organizo en un plan de trabajo por etapas o sprints, y las sigo con tableros e indicadores compartidos con tu equipo. Así siempre se sabe qué se está haciendo, qué sigue y qué resultado está dando."),
    ("¿Con qué tipo de empresas trabajas?",
     "Con empresas de movilidad, como concesionarios y grupos automotrices, distribuidores de motos, camiones y maquinaria, posventa e importadoras, y con inmobiliarias y desarrolladoras de Latinoamérica y España."),
    ("¿Cómo empezamos?",
     "Con una llamada de 20 minutos para entender tu operación, o pidiendo mi presentación comercial para ver los servicios y los proyectos en detalle. En ambos casos, sin compromiso."),
]

PAGE_FAQ = {
    "IA": [
        ("¿Qué diferencia hay entre un agente conversacional con IA y un chatbot?",
         "Un chatbot tradicional sigue un menú de opciones fijas. Un agente con inteligencia artificial entiende el contexto de la conversación, interpreta lo que la persona necesita, responde en lenguaje natural y además ejecuta acciones: registra el lead en el CRM, agenda una cita, envía una cotización o deriva a un asesor."),
        ("¿El agente reemplaza al vendedor o al asesor de servicio?",
         "No. Se ocupa de la primera respuesta, las preguntas repetitivas, la calificación y el seguimiento, y entrega al asesor un prospecto ya calificado y con el contexto de la conversación. Tu equipo dedica su tiempo a cerrar ventas y atender mejor."),
        ("¿En qué canales funciona?",
         "En WhatsApp, el sitio web, redes sociales como Instagram y Facebook, email y plataformas internas. Lo habitual es empezar por el canal donde hoy se pierden más consultas, que en la mayoría de las agencias es WhatsApp."),
        ("¿Se integra con mi CRM, DMS o ERP?",
         "Sí. El agente puede conectarse con CRM, ERP, DMS, calendarios, bases de datos y plataformas de marketing para registrar información y ejecutar acciones sin carga manual. En el diagnóstico defino qué integraciones generan más valor."),
        ("¿Es difícil de usar para mi equipo?",
         "No. La interfaz es intuitiva y no requiere conocimientos técnicos. Acompaño la puesta en marcha y capacito al equipo para que pueda revisar conversaciones, ajustar respuestas y medir resultados."),
        ("¿Qué plataforma de inteligencia artificial usas?",
         "No dependo de una única herramienta. Selecciono la plataforma más adecuada para cada empresa junto a especialistas tecnológicos, según los canales, el volumen de conversaciones y los sistemas que ya usa."),
    ],
    "EVOLUCION": [
        ("¿Qué es un plan de transformación digital para una concesionaria?",
         "Es una hoja de ruta que define qué procesos digitalizar, qué automatizar, qué sistemas integrar y en qué orden, a partir de un diagnóstico de cómo trabaja hoy la agencia o el grupo. Cada etapa tiene entregables e indicadores para medir el avance."),
        ("¿Por dónde conviene empezar?",
         "Por el diagnóstico. Relevo los procesos actuales, las herramientas y los resultados, y detecto dónde se pierden más ventas o más tiempo. Con eso priorizo las iniciativas de mayor impacto y menor esfuerzo."),
        ("¿Hay que cambiar todos los sistemas?",
         "No. Parto de lo que ya funciona y propongo cambios solo cuando el diagnóstico lo justifica. Muchas mejoras salen de ordenar procesos e integrar los sistemas existentes."),
        ("¿Sirve para un grupo con varias sucursales y marcas?",
         "Sí. Uno de los objetivos más frecuentes es homologar un solo proceso comercial y de posventa en todas las sucursales, con datos comparables entre marcas y puntos de venta."),
    ],
}


# Artículos publicados en el Hub. El cuerpo vive en _build/articulos/<slug>.html.
# "fecha" es la de publicación original (ISO). "old" es la URL del sitio viejo (para la 301).
ARTICULOS = [
    dict(slug="colaboradores-motivados",
         titulo="Colaboradores motivados: el motor silencioso de las empresas que crecen",
         seo_title="Colaboradores motivados: el motor de las empresas que crecen | Umarti Digital",
         descripcion="Por qué los equipos motivados son un diferencial competitivo en la industria automotriz y otros sectores, qué los desmotiva y cómo procesos, tecnología y automatización ayudan a potenciarlos.",
         intro="En un contexto de transformación constante, la competitividad de las empresas ya no depende solo de la tecnología que implementan, los productos que comercializan o los canales que utilizan. Cada vez es más evidente que el verdadero diferencial está en las personas que hacen funcionar la organización día a día. En industrias exigentes como la automotriz, y extensivo a sectores como retail, inmobiliario, educación o servicios, desarrollar colaboradores motivados dejó de ser un concepto aspiracional para convertirse en una necesidad estratégica.",
         resumen="Por qué el verdadero diferencial está en las personas y cómo procesos, tecnología y automatización ayudan a que los equipos crezcan junto con el negocio.",
         categoria="Gestión y Operaciones",
         fecha="2026-10-05",
         imagen="colaboradores-motivados",
         imagen_alt="Equipo de técnicos de un taller automotriz con el pulgar arriba",
         old="/colaboradores-motivados-el-motor-silencioso-de-las-empresas-que-crecen-copy",
         comunidad="",
         relacionados=[("/servicios/evolucion-digital/", "Método Evolución Digital"),
                       ("/servicios/automatizacion-ia/", "Automatización e IA")]),
    dict(slug="movilidad-en-transicion",
         titulo="La movilidad en transición: los retos digitales que marcarán el futuro del sector automotriz",
         seo_title="Retos digitales del sector automotriz: la movilidad en transición | Umarti Digital",
         descripcion="Cómo cambió el cliente automotriz, por qué el desafío de concesionarias y distribuidores no es digitalizar sino ordenar e integrar, y qué separa a los actores más innovadores del sector.",
         intro="La industria automotriz vive uno de los momentos más transformadores de su historia. El comportamiento del consumidor, la digitalización acelerada, la presión competitiva y los nuevos modelos de movilidad están modificando las reglas del juego para concesionarias, talleres, marcas y distribuidores.",
         resumen="El cliente ya decide en entornos digitales. Por qué el desafío del sector no es digitalizar, sino ordenar e integrar marketing, automatización y experiencia.",
         categoria="Customer Journey y Ventas",
         fecha="2026-10-05",
         imagen="movilidad-en-transicion",
         imagen_alt="Ciudad moderna con autos circulando entre edificios y espacios verdes",
         old="/la-movilidad-en-transicion-los-retos-digitales-que-marcaran-el-futuro-del-sector-automotriz",
         comunidad="autos",
         relacionados=[("/industrias/automotriz/", "Consultoría automotriz"),
                       ("/servicios/automatizacion-ia/", "Automatización e IA")]),
    dict(slug="ia-experiencia",
         titulo="Inteligencia artificial: automatizar no es suficiente, la diferencia está en la experiencia",
         seo_title="Inteligencia artificial en ventas: automatizar no alcanza, la clave es la experiencia | Umarti Digital",
         descripcion="Cómo usar la inteligencia artificial para vender más sin perder cercanía: por qué fallan muchas implementaciones de IA y cómo convertir tu sitio web en un canal activo de ventas.",
         intro="La inteligencia artificial dejó de ser una promesa para convertirse en una herramienta concreta de negocio. Hoy, las empresas que están logrando escalar no son necesariamente las que más invierten, sino las que mejor integran la tecnología en sus procesos comerciales.",
         resumen="La IA permite hacer más con menos, pero la venta la cierra la experiencia. Por qué fallan muchas implementaciones y cómo diseñar mejores interacciones.",
         categoria="Tecnología e IA",
         fecha="2026-10-05",
         imagen="ia-experiencia",
         imagen_alt="Asesora de atención al cliente con auriculares junto a un asistente de inteligencia artificial",
         old="/inteligencia-artificial-automatizar-no-es-suficiente-la-diferencia-esta-en-la-experiencia",
         comunidad="autos",
         relacionados=[("/servicios/automatizacion-ia/", "Agentes conversacionales con IA"),
                       ("/servicios/gestion-digital-ventas/", "Gestión digital de ventas")]),
    dict(slug="experiencia-del-cliente",
         titulo="Estrategias para potenciar la experiencia del cliente",
         seo_title="5 estrategias para mejorar la experiencia del cliente | Umarti Digital",
         descripcion="Cinco estrategias para mejorar la experiencia del cliente: el cliente en el centro de la operación, personalización, omnicanalidad, escucha activa y cultura organizacional.",
         intro="En un mercado saturado y altamente volátil, el valor real de una marca ya no reside únicamente en su oferta comercial, sino en la calidad de las interacciones que construye con su audiencia. Hoy, la ventaja competitiva se define por la capacidad de las organizaciones para anticiparse a las necesidades del consumidor y diseñar trayectorias de compra memorables. Para prosperar, las empresas deben evolucionar de un modelo transaccional a uno relacional, transformando cada punto de contacto en una oportunidad para superar expectativas y consolidar una lealtad genuina.",
         resumen="Cinco estrategias para pasar de un modelo transaccional a uno relacional: el cliente en el centro, personalización, omnicanalidad, escucha activa y cultura.",
         categoria="Customer Journey y Ventas",
         fecha="2026-10-05",
         imagen="experiencia-del-cliente",
         imagen_alt="Persona usando un celular con íconos de canales digitales a su alrededor",
         old="/estrategias-para-potenciar-la-experiencia-del-usuario-copy",
         comunidad="autos",
         relacionados=[("/servicios/evolucion-digital/", "Método Evolución Digital"),
                       ("/servicios/automatizacion-ia/", "Automatización e IA")]),    dict(slug="procesos-digitales-seguros",
         titulo="¿Estamos listos para diseñar procesos digitales seguros y transparentes?",
         seo_title="Procesos digitales seguros y transparentes en la industria automotriz | Umarti Digital",
         descripcion="La transformación digital en Latinoamérica avanza, pero de forma desigual. Cómo diseñar procesos digitales seguros, trazables y transparentes, y automatizar sin perder control.",
         intro="La transformación digital en Latinoamérica ya no es una promesa futura: es una realidad en marcha. En la industria automotriz, y también en sectores como retail, inmobiliario, educación o servicios, cada vez más etapas del negocio ocurren en entornos digitales. Ventas, posventa, atención, financiamiento, seguimiento y fidelización dependen hoy de procesos tecnológicos. La pregunta ya no es si debemos digitalizar, sino si estamos preparados para hacerlo de forma segura, transparente y confiable.",
         resumen="La pregunta ya no es si digitalizar, sino cómo hacerlo de forma segura y confiable: confianza, trazabilidad y automatización con criterio.",
         categoria="Gestión y Operaciones",
         fecha="2026-10-05",
         imagen="procesos-digitales-seguros",
         imagen_alt="Manos sosteniendo una tableta con el diseño de un auto e íconos de seguridad digital",
         old="/estamos-listos-para-disenar-procesos-digitales-seguros-y-transparentes-copy",
         comunidad="autos",
         relacionados=[("/servicios/evolucion-digital/", "Método Evolución Digital"),
                       ("/industrias/automotriz/", "Consultoría automotriz")]),    dict(slug="entrega-emotiva",
         titulo="La entrega emotiva: cómo construir una experiencia verdaderamente diferenciada en la industria automotriz",
         seo_title="Entrega emotiva de vehículos: cómo diseñar una experiencia memorable | Umarti Digital",
         descripcion="Cómo convertir la entrega de un vehículo en una experiencia memorable: por qué pesa tanto, qué la vuelve un trámite y cómo diseñarla antes, durante y después para fidelizar al cliente.",
         intro="En la industria automotriz, pocas instancias tienen tanto peso simbólico como el momento de la entrega. No se trata solo de entregar un vehículo: se entrega una decisión importante, una ilusión, un logro personal o profesional. Sin embargo, en muchos casos, este instante clave queda reducido a un trámite operativo. La entrega emotiva propone exactamente lo contrario: transformar ese momento en una experiencia memorable, coherente con todo el journey del cliente.",
         resumen="La entrega es el momento que el cliente más recuerda. Cómo diseñarla antes, durante y después para que deje de ser un trámite y genere clientes fieles.",
         categoria="Customer Journey y Ventas",
         fecha="2026-10-05",
         imagen="entrega-emotiva",
         imagen_alt="Asesor entregando las llaves de un auto nuevo con moño rojo a una pareja",
         old="/la-entrega-emotiva-como-construir-una-experiencia-verdaderamente-diferenciada-en-la-industria-automotriz-copy",
         comunidad="autos",
         relacionados=[("/industrias/automotriz/", "Consultoría automotriz"),
                       ("/hub/experiencia-del-cliente/", "5 estrategias para la experiencia del cliente")]),    dict(slug="automatizacion-procesos-automotriz",
         titulo="Automatización de procesos en la industria automotriz utilizando la tecnología",
         seo_title="Automatización de procesos en la industria automotriz: 7 pasos con IA | Umarti Digital",
         descripcion="Siete pasos para automatizar procesos en concesionarias con inteligencia artificial: digitalización, leads, perfilamiento del cliente, valoración de usados, inventario, firmas digitales y posventa.",
         intro="En un mercado automotriz cada vez más competitivo, la eficiencia en los procesos de compra y venta ya no es una ventaja: es una necesidad. La automatización, potenciada por la inteligencia artificial (IA), está transformando la manera en que las empresas gestionan sus operaciones, reducen costos y mejoran la experiencia del cliente. Pero, ¿cómo dar el primer paso hacia un flujo de trabajo más inteligente y automatizado?",
         resumen="Siete pasos para automatizar una concesionaria con IA: de digitalizar procesos y calificar leads a valorar usados, gestionar inventario y fidelizar en posventa.",
         categoria="Tecnología e IA",
         fecha="2026-10-05",
         imagen="automatizacion-procesos-automotriz",
         imagen_alt="Ilustración de inteligencia artificial con gráficos y mensajes digitales",
         old="/automatizacion-de-procesos-en-la-industria-automotriz-utilizando-la-tecnologia-copy",
         comunidad="autos",
         relacionados=[("/servicios/automatizacion-ia/", "Automatización e IA"),
                       ("/industrias/automotriz/", "Consultoría automotriz")]),    dict(slug="sitio-web-canal-de-ventas",
         titulo="El sitio web como canal de ventas: de presencia digital a motor de crecimiento",
         seo_title="El sitio web como canal de ventas: de presencia digital a crecimiento | Umarti Digital",
         descripcion="Por qué tu sitio web debe funcionar como un canal de ventas y no solo como presencia online: trazabilidad comercial, captación de leads, automatización y la estrategia digital que lo rodea.",
         intro="Actualmente tener un sitio web ya no es simplemente “tener presencia online”. Es, en muchos casos, uno de los principales canales de venta de una empresa. Así como un local físico requiere inversión, estrategia y operación, un sitio web también debe ser pensado como un espacio activo: donde ocurren interacciones, decisiones y conversiones.",
         resumen="Tu sitio web puede ser mucho más que presencia online: un canal de ventas con trazabilidad, captación de leads y automatización, dentro de una estrategia digital.",
         categoria="Marketing y Contenido",
         fecha="2026-10-05",
         imagen="sitio-web-canal-de-ventas",
         imagen_alt="Ilustración de un sitio web con embudo de ventas, megáfono y gráficos de crecimiento",
         old="/el-sitio-web-como-canal-de-ventas-de-presencia-digital-a-motor-de-crecimiento",
         comunidad="autos",
         relacionados=[("/servicios/gestion-digital-ventas/", "Gestión digital de ventas"),
                       ("/hub/ia-experiencia/", "IA: la diferencia está en la experiencia")]),    dict(slug="digitalizar-proceso-venta-automotriz",
         titulo="¿Cómo digitalizar un proceso de venta automotriz?",
         seo_title="Cómo digitalizar el proceso de venta de una agencia automotriz en 5 etapas | Umarti Digital",
         descripcion="Las cinco etapas para digitalizar el proceso de venta de una agencia automotriz: objetivos y KPIs, iniciativas, proceso ideal (To Be), implementación y reportes, y las ventajas de hacerlo.",
         intro="En un mundo donde la digitalización se ha convertido en un factor clave para la competitividad, las agencias automotrices enfrentan el desafío de optimizar sus procesos de venta para mejorar la experiencia del cliente y maximizar su eficiencia operativa. A continuación, describo las cinco etapas esenciales para digitalizar con éxito el proceso de venta en una agencia automotriz.",
         resumen="Las cinco etapas para digitalizar la venta en una agencia: objetivos y KPIs, iniciativas, proceso ideal, implementación y medición.",
         categoria="Customer Journey y Ventas",
         fecha="2026-10-05",
         imagen="digitalizar-proceso-venta-automotriz",
         imagen_alt="Ilustración de un tablero digital con íconos de procesos y una lupa",
         old="/como-digitalizar-un-proceso-de-venta-automotriz",
         comunidad="autos",
         relacionados=[("/servicios/evolucion-digital/", "Método Evolución Digital"),
                       ("/hub/automatizacion-procesos-automotriz/", "Automatización de procesos en la industria automotriz")]),    dict(slug="seminuevos-experiencia-cliente",
         titulo="La nueva experiencia del cliente en seminuevos",
         seo_title="La nueva experiencia del cliente en autos seminuevos | Umarti Digital",
         descripcion="Cómo está cambiando la compra y venta de autos seminuevos: asesoramiento personalizado, transparencia, procesos digitales, agencias más amigables y tecnología al servicio de una experiencia híbrida.",
         intro="El panorama de la compra y venta de autos seminuevos ha evolucionado significativamente en los últimos años, impulsado por la necesidad de los clientes de contar con experiencias basadas en procesos ágiles, seguros y transparentes, poniendo siempre al cliente en el centro.",
         resumen="Asesoramiento personalizado, transparencia, procesos digitales, mejores espacios y tecnología: los cinco componentes de la nueva experiencia en seminuevos.",
         categoria="Customer Journey y Ventas",
         fecha="2026-10-05",
         imagen="seminuevos-experiencia-cliente",
         imagen_alt="Fila de autos seminuevos exhibidos en una agencia",
         old="/la-nueva-experiencia-al-cliente-en-seminuevos",
         comunidad="autos",
         relacionados=[("/industrias/automotriz/", "Consultoría automotriz"),
                       ("/hub/experiencia-del-cliente/", "5 estrategias para la experiencia del cliente")]),
]

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]


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


def fecha_larga(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def minutos_lectura(html_text):
    import re
    palabras = len(re.sub(r"<[^>]+>", " ", html_text).split())
    return max(1, round(palabras / 200))


def articulo_body(a):
    return (SRC / "articulos" / f"{a['slug']}.html").read_text(encoding="utf-8")


def articulos_ordenados():
    return sorted(ARTICULOS, key=lambda a: a["fecha"], reverse=True)


def debate_link(comunidad):
    if COMUNIDAD_URL:
        url = COMUNIDAD_URL.rstrip("/") + (f"/{comunidad}" if comunidad else "")
        return (f'<a class="topic__debate" href="{url}" target="_blank" rel="noopener">'
                "Sumarme al debate en la Comunidad</a>")
    return '<span class="topic__debate topic__debate--off">Debate en la Comunidad Umarti</span>'


def debate_boton(comunidad):
    if COMUNIDAD_URL:
        url = COMUNIDAD_URL.rstrip("/") + (f"/{comunidad}" if comunidad else "")
        return f'<a class="btn btn--ghost" href="{url}" target="_blank" rel="noopener">Sumarme al debate</a>'
    return '<span class="btn btn--off" aria-disabled="true">Comunidad (próximamente)</span>'


def hub_cards(n=None):
    out = []
    for a in articulos_ordenados():
        mins = minutos_lectura(articulo_body(a))
        out.append(f"""        <article class="topic topic--post">
          <a class="topic__img" href="/hub/{a['slug']}/" tabindex="-1" aria-hidden="true">
            <picture><source srcset="/assets/img/hub/{a['imagen']}.webp" type="image/webp"><img src="/assets/img/hub/{a['imagen']}.jpg" alt="" width="1600" height="368" loading="lazy"></picture>
          </a>
          <p class="topic__cat">{e(a['categoria'])}</p>
          <h3><a href="/hub/{a['slug']}/">{e(a['titulo'])}</a></h3>
          <p>{e(a['resumen'])}</p>
          <div class="topic__foot">
            <span class="badge badge--on">{mins} min de lectura</span>
            <a class="topic__debate" href="/hub/{a['slug']}/">Leer nota</a>
          </div>
        </article>""")
    for cat, title, summary, comunidad in HUB:
        out.append(f"""        <article class="topic">
          <p class="topic__cat">{e(cat)}</p>
          <h3>{e(title)}</h3>
          <p>{e(summary)}</p>
          <div class="topic__foot">
            <span class="badge">Próximamente</span>
            {debate_link(comunidad)}
          </div>
        </article>""")
    return "\n".join(out[:n] if n else out)


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
        wa = f'<a class="link" href="{wa_link()}" target="_blank" rel="noopener">o escríbeme por WhatsApp</a>'
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
        <p>Estoy escribiendo esta página. Mientras tanto, puedes ver <a href="/servicios/">todos los servicios</a> o <a href="/contacto/">agendar una llamada</a>.</p>
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
        "description": "Consultoría de evolución digital para la industria automotriz, la movilidad y los bienes raíces: procesos, automatización con IA, gestión digital de ventas y nuevos productos.",
        "areaServed": ["MX", "AR", "Latinoamérica", "ES"],
        "knowsAbout": ["Consultoría automotriz", "Bienes raíces", "Transformación digital", "Automatización de procesos",
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
        "audience": {"@type": "BusinessAudience", "audienceType": "Empresas automotrices, de movilidad e inmobiliarias"},
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


def articulo_page(a):
    return dict(path=f"/hub/{a['slug']}/", file=None, nav="hub", parent="hub",
                title=a["seo_title"], og_title=a["titulo"], description=a["descripcion"],
                h1=a["titulo"], lead="", crumb=a["titulo"], articulo=a)


def articulo_html(a):
    body = articulo_body(a)
    mins = minutos_lectura(body)
    rel = "\n".join(f'        <a href="{u}">{e(t)}</a>' for u, t in a["relacionados"])
    page = articulo_page(a)
    trail = crumbs(page)
    links = ' <span class="crumbs__sep" aria-hidden="true">/</span> '.join(
        f'<a href="{u}">{e(n)}</a>' for n, u in trail[:-1])
    return f"""  <article class="post">
    <header class="post-head">
      <div class="wrap wrap--post">
        <nav class="crumbs" aria-label="Ruta">{links}</nav>
        <p class="eyebrow">{e(a['categoria'])}</p>
        <h1>{e(a['titulo'])}</h1>
        <p class="post-head__meta">Por <a href="/sobre-umarti/">Marcelo</a> · <time datetime="{a['fecha']}">{fecha_larga(a['fecha'])}</time> · {mins} min de lectura</p>
      </div>
    </header>
    <figure class="post-cover">
      <picture><source srcset="/assets/img/hub/{a['imagen']}.webp" type="image/webp"><img src="/assets/img/hub/{a['imagen']}.jpg" alt="{e(a['imagen_alt'])}" width="1600" height="368" fetchpriority="high"></picture>
    </figure>
    <div class="wrap wrap--post">
      <div class="post-body">
        <p class="post-intro">{e(a['intro'])}</p>
{body}
      </div>

      <aside class="post-debate">
        <div>
          <p class="eyebrow eyebrow--dark">Comunidad Umarti</p>
          <h2>¿Cómo lo ves en tu empresa?</h2>
          <p>Este tema también se debate con colegas de la industria en la Comunidad Umarti.</p>
        </div>
        {debate_boton(a['comunidad'])}
      </aside>

      <div class="post-author">
        <picture><source srcset="/assets/img/marcelo.webp" type="image/webp"><img src="/assets/img/marcelo.jpg" alt="" width="72" height="72"></picture>
        <div>
          <p class="post-author__name">Marcelo</p>
          <p>Consultor con 20 años en la industria de la movilidad. Ayudo a empresas automotrices, de movilidad e inmobiliarias a ordenar procesos, automatizar con IA y vender mejor.</p>
        </div>
      </div>

      <nav class="related post-related" aria-label="Relacionado">
        <p class="related__title">Relacionado</p>
{rel}
        <a href="/hub/">Más notas del Hub</a>
      </nav>
    </div>
  </article>

{cta_band()}"""


def articulo_ld(a):
    d = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": a["titulo"],
        "description": a["descripcion"],
        "image": f"{BASE}/assets/img/hub/{a['imagen']}.jpg",
        "datePublished": a["fecha"],
        "dateModified": a.get("modificada", a["fecha"]),
        "inLanguage": "es",
        "articleSection": a["categoria"],
        "mainEntityOfPage": f"{BASE}/hub/{a['slug']}/",
        "author": {"@type": "Person", "name": "Marcelo", "url": f"{BASE}/sobre-umarti/"},
        "publisher": {"@id": f"{BASE}/#organizacion", "@type": "Organization", "name": "Umarti Digital",
                      "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/img/umarti-logo.png"}},
    }
    return d


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
    if page.get("articulo"):
        ld.append(articulo_ld(page["articulo"]))
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
           .replace("{{og_type}}", "article" if page.get("articulo") else "website")
           .replace("{{og_title}}", e(page.get("og_title", page["title"])))
           .replace("{{description}}", e(page["description"]))
           .replace("{{robots}}", '<meta name="robots" content="noindex, nofollow">\n' if (STAGING or page.get("noindex")) else "")
           .replace("{{url}}", f"{BASE}{page['path']}")
           .replace("{{base}}", BASE)
           .replace("{{version}}", VERSION)
           .replace("{{jsonld}}", ld_tags(ld))
           .replace("{{body_class}}", "page-home" if page["path"] == "/" else ("page-post" if page.get("articulo") else "page-inner"))
           .replace("{{cur_servicios}}", cur if nav == "servicios" else "")
           .replace("{{cur_industrias}}", cur if nav == "industrias" else "")
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

    for a in ARTICULOS:
        page = articulo_page(a)
        target = ROOT / "hub" / a["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page, layout, articulo_html(a)), encoding="utf-8")

    # Redirecciones de las notas del sitio viejo (bloque generado dentro de .htaccess)
    ht = ROOT / ".htaccess"
    txt = ht.read_text(encoding="utf-8")
    ini, fin = "# >>> notas del sitio anterior (generado)", "# <<< notas del sitio anterior"
    bloque = ini + "\n" + "".join(f"Redirect 301 {a['old']} /hub/{a['slug']}/\n" for a in ARTICULOS if a.get("old")) + fin
    if ini in txt:
        txt = txt[:txt.index(ini)] + bloque + txt[txt.index(fin) + len(fin):]
    else:
        txt = txt.replace("# No exponer archivos", bloque + "\n\n# No exponer archivos", 1)
    ht.write_text(txt, encoding="utf-8")

    # 404
    p404 = dict(path="/404/", nav="", file=None, noindex=True, h1="No encontramos esta página",
                lead="Puede que la dirección haya cambiado con el nuevo sitio.",
                title="Página no encontrada | Umarti Digital", description="Página no encontrada.")
    body = page_header(p404) + """
  <section class="section section--tight"><div class="wrap"><p><a class="btn" href="/">Ir al inicio</a></p></div></section>"""
    (ROOT / "404.html").write_text(render(p404, layout, body), encoding="utf-8")

    today = datetime.date.today().isoformat()
    entradas = [(p["path"], today) for p in PAGES] + [(f"/hub/{a['slug']}/", a.get("modificada", a["fecha"])) for a in ARTICULOS]
    urls = "\n".join(f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{d}</lastmod>\n  </url>"
                     for u, d in entradas)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n",
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    print(f"OK: {len(PAGES)} páginas + {len(ARTICULOS)} notas + 404, sitemap y robots. STAGING={STAGING}")


if __name__ == "__main__":
    main()
