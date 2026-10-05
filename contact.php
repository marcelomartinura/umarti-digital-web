<?php
// Recibe los formularios del sitio (contacto y newsletter del Hub) y los envía por email.
// CONFIGURAR: casilla que recibe los contactos.
const DESTINO   = 'contacto@umartidigital.com';
const REMITENTE = 'no-responder@umartidigital.com';

// Página a la que vuelve cada formulario.
const ORIGENES = ['contacto' => '/contacto/', 'hub' => '/hub/'];

$origen = $_POST['origen'] ?? 'contacto';
$volverA = ORIGENES[$origen] ?? '/contacto/';

function volver($ok) {
    global $volverA;
    header('Location: ' . $volverA . '?enviado=' . ($ok ? '1' : '0'), true, 303);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') volver(false);

// Trampa para bots: este campo está oculto para las personas.
if (!empty($_POST['sitio'])) volver(true);

$limpiar = function ($v, $max = 300) {
    $v = trim((string)($v ?? ''));
    $v = str_replace(["\r", "\n"], ' ', $v);
    return mb_substr($v, 0, $max);
};

$nombre = $limpiar($_POST['nombre'] ?? '');
$email  = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$interesRaw = $_POST['interes'] ?? '';

if ($interesRaw === 'newsletter') {
    if ($nombre === '' || !$email) volver(false);
    $asunto = "Nueva suscripción al Radar Automotriz: $nombre";
    $cuerpo = "Suscripción al newsletter Radar Automotriz\nNombre: $nombre\nEmail: $email\n";
} else {
    $empresa  = $limpiar($_POST['empresa'] ?? '');
    $telefono = $limpiar($_POST['telefono'] ?? '', 40);
    $pais     = $limpiar($_POST['pais'] ?? '', 40);
    $interes  = $interesRaw === 'presentacion' ? 'Recibir la presentación comercial' : 'Agendar una llamada de 20 minutos';
    $mensaje  = mb_substr(trim((string)($_POST['mensaje'] ?? '')), 0, 3000);
    if ($nombre === '' || $empresa === '' || !$email) volver(false);
    $asunto = "Nuevo contacto desde umartidigital.com: $empresa ($pais) - $interes";
    $cuerpo = "Quiere: $interes\nNombre: $nombre\nEmpresa: $empresa\nEmail: $email\nWhatsApp: $telefono\nPaís: $pais\n\nMensaje:\n$mensaje\n";
}

$cabeceras = "From: Umarti Digital <" . REMITENTE . ">\r\n"
           . "Reply-To: $email\r\n"
           . "Content-Type: text/plain; charset=UTF-8\r\n";

$ok = mail(DESTINO, '=?UTF-8?B?' . base64_encode($asunto) . '?=', $cuerpo, $cabeceras);
volver($ok);
