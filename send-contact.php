<?php
// Simple contact form handler for Mudau Makondelele Attorneys

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: contact.html');
    exit;
}

// Helper to safely fetch and trim input
function field($key) {
    return isset($_POST[$key]) ? trim($_POST[$key]) : '';
}

$name    = field('name');
$email   = field('email');
$phone   = field('phone');
$subject = field('subject');
$message = field('message');

if ($name === '' || $email === '' || $message === '') {
    header('Location: contact.html?error=1');
    exit;
}

// Map subject value to human‑friendly label
$subjectLabels = [
    'civil-litigation' => 'Civil Litigation',
    'family-law'       => 'Family Law',
    'criminal-law'     => 'Criminal Law',
    'labour-law'       => 'Labour Law',
    'commercial-law'   => 'Commercial Law',
    'debt-collection'  => 'Debt Collection',
    'contracts'        => 'Contracts & Agreements',
    'raf-claims'       => 'RAF Claims',
    'wills-estates'    => 'Wills & Estates',
    'general'          => 'General Inquiry',
];

$subjectText = isset($subjectLabels[$subject]) ? $subjectLabels[$subject] : 'General Inquiry';

$to      = 'info@mudauattorneys.com';
$subjectLine = 'Website Contact Form: ' . $subjectText;

$body  = "You have received a new enquiry from the website contact form:\r\n\r\n";
$body .= "Name:  {$name}\r\n";
$body .= "Email: {$email}\r\n";
if ($phone !== '') {
    $body .= "Phone: {$phone}\r\n";
}
$body .= "Subject: {$subjectText}\r\n\r\n";
$body .= "Message:\r\n{$message}\r\n";

$headers   = "From: Mudau Makondelele Attorneys Website <no-reply@mudauattorneys.com>\r\n";
$headers  .= "Reply-To: {$name} <{$email}>\r\n";
$headers  .= "Content-Type: text/plain; charset=UTF-8\r\n";

@mail($to, $subjectLine, $body, $headers);

header('Location: contact.html?sent=1');
exit;


