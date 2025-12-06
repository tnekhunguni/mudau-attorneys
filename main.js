/**
 * Mudau Makonde Attorneys - Main JavaScript
 * Handles mobile menu, form validation, and interactive elements
 */

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Change icon based on menu state
            if (navMenu.classList.contains('active')) {
                mobileMenuToggle.textContent = '✕';
            } else {
                mobileMenuToggle.textContent = '☰';
            }
        });

        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                mobileMenuToggle.textContent = '☰';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target);
            const isClickOnToggle = mobileMenuToggle.contains(event.target);
            
            if (!isClickInsideNav && !isClickOnToggle && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                mobileMenuToggle.textContent = '☰';
            }
        });
    }

    // Contact Form Validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form fields
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value.trim();
            
            // Basic validation
            let isValid = true;
            let errorMessage = '';

            if (!name) {
                isValid = false;
                errorMessage += 'Please enter your full name.\n';
            }

            if (!email) {
                isValid = false;
                errorMessage += 'Please enter your email address.\n';
            } else if (!isValidEmail(email)) {
                isValid = false;
                errorMessage += 'Please enter a valid email address.\n';
            }

            if (!subject) {
                isValid = false;
                errorMessage += 'Please select a subject.\n';
            }

            if (!message) {
                isValid = false;
                errorMessage += 'Please enter your message.\n';
            } else if (message.length < 10) {
                isValid = false;
                errorMessage += 'Please provide more details in your message.\n';
            }

            if (isValid) {
                // Get additional form fields
                const phone = document.getElementById('phone').value.trim();
                const subjectText = document.getElementById('subject').options[document.getElementById('subject').selectedIndex].text;
                
                // Construct email body
                let emailBody = 'Name: ' + encodeURIComponent(name) + '%0D%0A';
                emailBody += 'Email: ' + encodeURIComponent(email) + '%0D%0A';
                if (phone) {
                    emailBody += 'Phone: ' + encodeURIComponent(phone) + '%0D%0A';
                }
                emailBody += 'Subject: ' + encodeURIComponent(subjectText) + '%0D%0A%0D%0A';
                emailBody += 'Message:%0D%0A' + encodeURIComponent(message);
                
                // Construct mailto link
                const mailtoLink = 'mailto:takalaninekhunguni@gmail.com?subject=' + 
                    encodeURIComponent('Contact Form: ' + subjectText) + 
                    '&body=' + emailBody;
                
                // Open email client
                window.location.href = mailtoLink;
                
                // Show confirmation message
                setTimeout(function() {
                    alert('Thank you for your message. Your email client should open. If it doesn\'t, please email us directly at takalaninekhunguni@gmail.com');
                }, 500);
                
                // Note: For production, replace this with backend form handler
                // (WordPress: Contact Form 7, WPForms, or custom PHP handler)
            } else {
                alert('Please correct the following errors:\n\n' + errorMessage);
            }
        });
    }

    // Email validation helper function
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Add animation on scroll (optional enhancement)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe service cards and feature items for fade-in animation
    document.querySelectorAll('.service-card, .feature-item').forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(item);
    });
});

