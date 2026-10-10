# Mudau Makondelele Attorneys: website (Astro)

The rebuilt site. The old static site in the parent folder stays live until this replaces it.

## Run it locally

```bash
cd web
npm install
npm run dev        # http://localhost:4321
npm run build      # static output in dist/, upload its contents to the host
```

## Where things live

- `src/data/site.ts`: firm details (phones, address, hours, registration number), practice areas, credentials and client names. Change them here and every page updates.
- `src/styles/global.css`: design tokens (colours from the letterhead, type scale) and shared styles.
- `src/components/`: header, footer, phone action bar, page header, practice index, timeline, steps, credentials, call-to-action band, icons.
- `src/layouts/Base.astro`: page shell, SEO and social-sharing tags, LegalService schema.
- `src/pages/`: one file per page; practice area pages are generated from `src/data/practice.ts`.
- `public/`: favicon, social preview image, robots.txt, .htaccess (redirects, HTTPS, caching) and the contact form handler.

## Status

- All pages built: home, practice areas (hub + 10), about, for organisations, contact, privacy, 404.
- To do: Insights (articles), client logos, Google Business Profile link.
- Later: move hosting to Vercel alongside the case management app.

## Deploying to the current host (cPanel)

1. `npm run build`
2. Back up the current `public_html`.
3. Upload the **contents** of `dist/` (including the hidden `.htaccess`) to `public_html`, replacing the old `index.html`, `about.html`, `services.html`, `contact.html`, `styles.css`, `main.js` and `send-contact.php`.
4. Visit an old address such as `/services.html`: it should redirect to `/practice-areas/`.
5. Send a test enquiry from `/contact/` and confirm it arrives at info@mudauattorneys.com.

## Contact form

`public/send-contact.php` validates input, strips line breaks from header values, uses a honeypot, a minimum fill time and a one-minute per-IP rate limit, and only shows "sent" when `mail()` succeeds. If the practice area list changes, update the `MATTERS` list in that file to match `src/data/practice.ts`.
