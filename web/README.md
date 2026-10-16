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

- All pages built: home, practice areas (hub + 11), about, for organisations, insights, contact, privacy, 404.
- To do: client logos, Google Business Profile link, more articles.
- Later: move hosting to Vercel alongside the case management app.

## Deploying to the current host (cPanel)

1. `npm run build`
2. Back up the current `public_html`.
3. Upload the **contents** of `dist/` (including the hidden `.htaccess`) to `public_html`, replacing the old `index.html`, `about.html`, `services.html`, `contact.html`, `styles.css`, `main.js` and `send-contact.php`.
4. Visit an old address such as `/services.html`: it should redirect to `/practice-areas/`.
5. Send a test enquiry from `/contact/` and confirm it arrives at info@mudauattorneys.com.

## Contact form

`public/send-contact.php` validates input, strips line breaks from header values, uses a honeypot, a minimum fill time and a one-minute per-IP rate limit, and only shows "sent" when `mail()` succeeds. If the practice area list changes, update the `MATTERS` list in that file to match `src/data/practice.ts`.

## Adding an Insights article

1. Create a new file in `src/content/insights/`, for example `src/content/insights/bail-applications.md`. The file name becomes the address: `/insights/bail-applications/`. Use lowercase words joined by hyphens.
2. Start it with this header, then write the article underneath in Markdown (`## Heading`, `- bullet`, `**bold**`):

   ```markdown
   ---
   title: "How bail applications work"            # up to 90 characters
   description: "One or two sentences for Google and WhatsApp previews."  # up to 170 characters
   date: 2026-11-02
   practice: criminal-litigation                  # optional: links the article to that practice page
   draft: true                                    # optional: true keeps it off the site until ready
   ---
   ```

3. Run `npm run dev` and check it at `http://localhost:4321/insights/`.
4. Commit and push. The article appears on the Insights page, the homepage (latest three), the linked practice page and the sitemap automatically.

Practice slugs: criminal-litigation, labour-disputes, civil-litigation, medical-negligence, personal-injury, family-and-estates, employment-law, litigation, commercial-law, debt-recovery, public-sector.

## Visitor statistics (optional)

Create a free Cloudflare Web Analytics site for mudauattorneys.com, copy its token, and set `PUBLIC_CF_ANALYTICS_TOKEN` when building (for example `PUBLIC_CF_ANALYTICS_TOKEN=abc123 npm run build`, or as a Vercel environment variable). It is cookie-free and never loads on review builds.

## Search profiles

Once the firm has a Google Business Profile, Facebook or LinkedIn page, add their URLs to `profiles` in `src/data/site.ts`. They are passed to Google in the firm's structured data.
