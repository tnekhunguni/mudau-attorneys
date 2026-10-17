<?php
/**
 * Contact form handler for mudauattorneys.com
 *
 * - Accepts POST from /contact/ only
 * - Spam protection: honeypot field, minimum fill time, per-IP rate limit
 * - Strips line breaks from header values (prevents email header injection)
 * - Redirects back with ?sent=1 only when mail() actually succeeded
 */

declare(strict_types=1);

date_default_timezone_set('Africa/Johannesburg');

// Some shared hosts run without the mbstring extension
if (!function_exists('mb_substr')) {
    function mb_substr(string $s, int $start, ?int $len = null): string { return $len === null ? substr($s, $start) : substr($s, $start, $len); }
}
if (!function_exists('mb_strlen')) {
    function mb_strlen(string $s): int { return strlen($s); }
}

const RECIPIENT   = 'info@mudauattorneys.com';
const FROM        = 'no-reply@mudauattorneys.com';
const BACK        = '/contact/';
const RATE_WINDOW = 60;   // seconds between messages from one IP
const MIN_SECONDS = 3;    // forms filled faster than this are bots

// Keep in sync with src/data/practice.ts
const MATTERS = [
    'criminal-litigation' => 'Criminal litigation',
    'civil-litigation'   => 'Civil litigation',
    'labour-disputes'    => 'Dismissals and workplace disputes',
    'medical-negligence' => 'Medical negligence',
    'personal-injury'    => 'Personal injury and unlawful arrest',
    'family-and-estates' => 'Family law, wills and estates',
    'employment-law'     => 'Employment law for employers',
    'litigation'         => 'Civil and High Court litigation',
    'commercial-law'     => 'Commercial, contracts and corporate',
    'debt-recovery'      => 'Debt recovery',
    'public-sector'      => 'Public sector, procurement and administrative law',
    'other'              => 'Something else',
];

function back(string $query): void
{
    header('Location: ' . BACK . '?' . $query, true, 303);
    exit;
}

function field(string $key, int $max): string
{
    $v = isset($_POST[$key]) && is_string($_POST[$key]) ? trim($_POST[$key]) : '';
    return mb_substr($v, 0, $max);
}

function oneLine(string $v): string
{
    // Remove anything that could start a new header line
    return trim(preg_replace('/[\r\n\t]+|%0a|%0d/i', ' ', $v) ?? '');
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: ' . BACK, true, 303);
    exit;
}

// Honeypot: real visitors never see this field. Pretend success to bots.
if (field('website', 200) !== '') {
    back('sent=1');
}

// Minimum time between page load and submit
$ts = (int) field('ts', 20);
if ($ts > 0 && (time() - $ts) < MIN_SECONDS) {
    back('sent=1');
}

// Rate limit per IP using a small file in the system temp folder
$ip       = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$rateFile = sys_get_temp_dir() . '/mma_contact_' . hash('sha256', $ip);
if (is_file($rateFile) && (time() - (int) @filemtime($rateFile)) < RATE_WINDOW) {
    back('error=wait');
}

$name    = oneLine(field('name', 100));
$phone   = oneLine(field('phone', 20));
$email   = oneLine(field('email', 150));
$matter  = field('matter', 40);
$message = field('message', 3000);
$consent = field('consent', 5) === 'yes';

$valid =
    $name !== '' &&
    preg_match('/^[0-9+()\s\-]{9,20}$/', $phone) === 1 &&
    ($email === '' || filter_var($email, FILTER_VALIDATE_EMAIL) !== false) &&
    array_key_exists($matter, MATTERS) &&
    mb_strlen($message) >= 10 &&
    $consent;

if (!$valid) {
    back('error=invalid');
}

$matterLabel = MATTERS[$matter];
$subject     = 'Website enquiry: ' . $matterLabel . ' (' . $name . ')';

$body  = "New enquiry from the website contact form\r\n\r\n";
$body .= "Name:    {$name}\r\n";
$body .= "Phone:   {$phone}\r\n";
$body .= 'Email:   ' . ($email !== '' ? $email : '(not given)') . "\r\n";
$body .= "Matter:  {$matterLabel}\r\n";
$body .= 'Sent:    ' . date('Y-m-d H:i') . "\r\n";
$body .= "Consent: given to process details to respond (POPIA)\r\n\r\n";
$body .= "Message:\r\n" . str_replace(["\r\n", "\r"], "\n", $message) . "\r\n";

$headers = [
    'From'         => 'Mudau Makondelele Attorneys website <' . FROM . '>',
    'Content-Type' => 'text/plain; charset=UTF-8',
    'X-Mailer'     => 'mudauattorneys.com',
];
if ($email !== '') {
    $headers['Reply-To'] = $email;
}

$encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$sent = mail(RECIPIENT, $encodedSubject, $body, $headers);

if (!$sent) {
    error_log('[contact form] mail() failed for enquiry from ' . $ip);
    back('error=send');
}

@touch($rateFile);
back('sent=1');
