// Single source of truth for firm details. Update here, every page follows.
export const firm = {
  name: 'Mudau Makondelele Attorneys',
  shortName: 'Mudau Makondelele',
  tagline: 'Legal Excellence Is Our Agenda',
  director: 'Makondelele Mudau',
  registration: '2025/416899/21',
  email: 'info@mudauattorneys.com',
  phones: [
    { label: '015 023 1380', href: 'tel:+27150231380', kind: 'Office' },
    { label: '072 054 0722', href: 'tel:+27720540722', kind: 'Mobile' },
  ],
  whatsapp: 'https://wa.me/27720540722?text=' +
    encodeURIComponent("Hello, I'd like to arrange a consultation about a legal matter."),
  address: {
    lines: ['Stand 709, Madanzhe Street', 'P West, Thohoyandou', 'Limpopo, 0950'],
    street: 'Stand 709, Madanzhe Street, P West',
    locality: 'Thohoyandou',
    region: 'Limpopo',
    postalCode: '0950',
    country: 'ZA',
  },
  mapUrl: 'https://www.google.com/maps/search/?api=1&query=' +
    encodeURIComponent('Stand 709 Madanzhe Street, P West, Thohoyandou'),
  hours: [
    { days: 'Monday to Friday', time: '08:00 to 17:00' },
    { days: 'Saturday', time: 'By appointment' },
    { days: 'Sunday and public holidays', time: 'Closed' },
  ],
  url: 'https://mudauattorneys.com',
};

export const timeline = [
  { when: '2012', what: 'LLB, University of Venda' },
  {
    when: '2013 to 2015',
    what: 'Practical legal training at the Polokwane School for Legal Practice, articles with Legal Aid South Africa, then litigation work in Johannesburg',
  },
  { when: '2015 to 2025', what: 'Co-founder and Director, Mudau & Netshipise Attorneys' },
  { when: '2018 to 2023', what: 'Black Lawyers Association, Gauteng: Head of Events and Campaigns, then Treasurer' },
  { when: '2025', what: 'Opens Mudau Makondelele Attorneys in Thohoyandou' },
];

// How a matter runs, taken from the firm's documented workflow.
export const steps = [
  {
    title: 'First consultation',
    body: 'We listen, take your instructions and explain your options, the likely steps and our fees.',
  },
  {
    title: 'A named person on your file',
    body: 'Your matter goes to the most suitable member of the team, supervised by the director. Every document carries the name of the person who prepared it.',
  },
  {
    title: 'Written updates at every step',
    body: 'You hear from us in writing after each step. We ask your permission before briefing an advocate or an expert.',
  },
  {
    title: 'A close-out report',
    body: 'When the matter ends, you receive a report on what was done and the result, with the final account.',
  },
];

export const credentials = [
  { term: 'B-BBEE Level 1', detail: '135% procurement recognition, value-adding supplier' },
  { term: '100% black-owned', detail: 'Owned and directed by Makondelele Mudau' },
  { term: 'Central Supplier Database', detail: 'Registered supplier to organs of state' },
  { term: 'Legal Practice Council', detail: 'Registered, with a Fidelity Fund certificate' },
];

// Names cleared for publication by the clients. Logos to follow.
export const clients = [
  'Thulamela Municipality',
  'City of Ekurhuleni',
  'University of Venda',
  'Vhembe TVET College',
  'FNB Law on Call',
  'LIPCO Law for All',
  'Lawyers Voice',
  'Dumezulu Inc.',
  'Mutupo Legal Guardian',
  'Nungo Health Foods',
  'Takalani Computer Solutions',
  'Debt Guides',
];
