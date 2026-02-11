# Mudau Makondelele Attorneys Website

A modern, premium WordPress-compatible website for Mudau Makondelele Attorneys, a law firm in South Africa.

## Project Structure

```
mudau-makonde-attorneys/
├── index.html          # Homepage
├── about.html          # About Us page
├── services.html       # Services page
├── contact.html        # Contact page
├── styles.css          # Main stylesheet
├── main.js             # JavaScript for interactivity
├── assets/
│   ├── images/         # Image assets
│   └── icons/          # Icon assets
└── README.md           # This file
```

## Brand Identity

### Colors
- **Primary (Black)**: #1A1A1A (Headings, footer, primary elements)
- **Accent (Red)**: #B22222 (Buttons, links, highlights – from letterhead)
- **Charcoal**: #1E1E1E (Text color)
- **Light Grey**: #F5F6F8 (Section backgrounds)
- **White**: #FFFFFF (Main background)

### Typography
- **Headings**: Playfair Display (serif)
- **Body**: Inter (sans-serif)

## Features

- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ Sticky navigation bar
- ✅ Mobile-friendly hamburger menu
- ✅ Contact form with validation
- ✅ Google Maps integration
- ✅ Modern, premium design aesthetic
- ✅ SEO-friendly semantic HTML
- ✅ Clean, maintainable code structure

## Setup Instructions

1. **Add Images**: Place the following images in `assets/images/`:
   - `hero.jpg` - Hero section background
   - `attorney.jpg` - Attorney headshot

2. **Update Contact Information**: 
   - Edit `contact.html` and `index.html` to add:
     - Actual phone number
     - Physical address
     - Update Google Maps embed with correct location

3. **Customize Content**:
   - Review all pages and update any placeholder content
   - Add actual attorney biography to `about.html`
   - Verify all service descriptions match your practice

4. **Form Integration**:
   - The contact form submits to send-contact.php, which emails info@mudauattorneys.com
   - This opens the user's email client with a pre-filled message
   - For production WordPress site, integrate with:
     - WordPress contact form plugin (Contact Form 7, WPForms)
     - Email service (SMTP)
     - Or custom PHP handler
   - Update the email recipient in main.js if needed

## WordPress Migration

This site is built with clean HTML/CSS/JS that can easily be converted to WordPress:

1. **Theme Structure**: Convert HTML files to WordPress template files
   - `index.html` → `front-page.php` or `page-home.php`
   - `about.html` → `page-about.php`
   - `services.html` → `page-services.php`
   - `contact.html` → `page-contact.php`

2. **Styles**: Move `styles.css` to theme's `style.css` or enqueue it

3. **Scripts**: Enqueue `main.js` in `functions.php`

4. **Navigation**: Convert static nav to `wp_nav_menu()`

5. **Content**: Use WordPress Custom Fields or ACF for dynamic content

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Customization

### Changing Colors
Edit CSS variables in `styles.css` (letterhead brand colors):
```css
:root {
    --primary: #1A1A1A;
    --accent: #B22222;
    /* ... */
}
```

### Adding Pages
1. Create new HTML file following existing structure
2. Add navigation link in all HTML files
3. Style as needed in `styles.css`

## Notes

- All content has been rewritten to be fresh and professional (not copied from old site)
- Placeholder images need to be added
- Contact information needs to be updated with actual details
- Google Maps embed needs actual location coordinates

## License

© 2026 Mudau Makondelele Attorneys. All rights reserved.

