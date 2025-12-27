
document.addEventListener('DOMContentLoaded', () => {
    initStickyHeader();
    initScrollReveal();
    initCartCounter();
    initHeroSlider();
    initProductCarousel();
    initComparisonSlider();
    initFAQ();
    initMobileMenu();
});

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
    const toggleBtn = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    const icon = toggleBtn ? toggleBtn.querySelector('i') : null;

    if (!toggleBtn || !navLinks) return;

    toggleBtn.addEventListener('click', () => {
        navLinks.classList.toggle('active');

        // Toggle Icon
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('ph-list');
            icon.classList.add('ph-x');
            document.body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
        } else {
            icon.classList.remove('ph-x');
            icon.classList.add('ph-list');
            document.body.style.overflow = '';
        }
    });

    // Handle Submenu Toggles on Mobile
    const menuItemsWithChildren = navLinks.querySelectorAll('.nav-item > a');
    menuItemsWithChildren.forEach(link => {
        const nextElement = link.nextElementSibling;
        if (nextElement && nextElement.classList.contains('mega-menu')) {
            link.addEventListener('click', (e) => {
                // Only prevent default if we are in mobile view (navLinks has active class usually implies mobile menu is open)
                // Or check window width
                if (window.innerWidth <= 1024) {
                    e.preventDefault();
                    link.parentElement.classList.toggle('open');
                }
            });
        }
    });

    // Close menu when clicking a link (BUT NOT if it's a toggle link on mobile)
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', (e) => {
            // Check if this link is a toggle (has mega-menu sibling) and we are on mobile
            const nextElement = link.nextElementSibling;
            const isToggle = nextElement && nextElement.classList.contains('mega-menu') && window.innerWidth <= 1024;

            if (!isToggle) {
                // It's a regular link, close the menu
                navLinks.classList.remove('active');
                if (icon) {
                    icon.classList.remove('ph-x');
                    icon.classList.add('ph-list');
                }
                document.body.style.overflow = '';
            }
        });
    });
}


/**
 * Hero Carousel
 */
function initHeroSlider() {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (slides.length === 0) return;

    let currentSlide = 0;
    const intervalTime = 6000; // Increased to 6 seconds for better UX
    let slideInterval;

    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));

        // Handle wrapping
        if (index >= slides.length) {
            currentSlide = 0;
        } else if (index < 0) {
            currentSlide = slides.length - 1;
        } else {
            currentSlide = index;
        }

        slides[currentSlide].classList.add('active');
    }

    function nextSlide() {
        showSlide(currentSlide + 1);
    }

    function prevSlide() {
        showSlide(currentSlide - 1);
    }

    // Event Listeners for Buttons
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetInterval();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetInterval();
        });
    }

    // Auto Play - DISABLED per user request
    // function startInterval() {
    //     slideInterval = setInterval(nextSlide, intervalTime);
    // }

    function resetInterval() {
        // clearInterval(slideInterval);
        // startInterval();
    }

    // startInterval(); 
}


/**
 * Handle Header transparency on scroll
 */
function initStickyHeader() {
    const header = document.querySelector('.header');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(255, 255, 255, 1)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.05)';
        }
    });
}

/**
 * Simple Scroll Reveal Animation
 */
function initScrollReveal() {
    const elementsToReveal = document.querySelectorAll('.collection-card, .product-card, .section-title');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    elementsToReveal.forEach(el => {
        // Only hide if we are sure we can reveal them
        // Add a class 'reveal-pending' via CSS instead of inline style for better separation
        el.classList.add('reveal-pending'); // We will add CSS for this
        observer.observe(el);
    });
}

// Helper to add class via JS for the CSS to pick up
// We use a CSS class logic instead of inline styles to prevent 'stuck' invisible elements
document.head.insertAdjacentHTML("beforeend", `<style>
    .reveal-pending {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .visible {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
</style>`);


/**
 * Mock Cart Interaction
 */
function initCartCounter() {
    const addToCartButtons = document.querySelectorAll('.btn-outline, .btn-primary');
    const cartBadge = document.querySelector('.header-icons .icon-btn span');
    let count = 0;

    addToCartButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Check if it's an "Add to Cart" button (simple check)
            if (btn.textContent.includes('Ajouter') || btn.textContent.includes('Panier')) {
                e.preventDefault();
                count++;
                cartBadge.textContent = count;

                // Visual feedback
                const originalText = btn.textContent;
                btn.textContent = "Ajouté !";
                btn.style.backgroundColor = "var(--color-primary)";
                btn.style.color = "white";

                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.style.backgroundColor = "";
                    btn.style.color = "";
                }, 2000);
            }
        });
    });
}

/**
 * Product Carousel (Infinite Loop)
 */
function initProductCarousel() {
    const carousel = document.querySelector('.product-carousel');
    const prevBtn = document.querySelector('.prev-prod-btn');
    const nextBtn = document.querySelector('.next-prod-btn');

    if (!carousel || !prevBtn || !nextBtn) return;

    // No cloning, no auto-scroll. Just manual navigation.
    const scrollAmount = 300; // Card width + gap

    nextBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
}

/**
 * Before/After Comparison Slider
 */
function initComparisonSlider() {
    const slider = document.querySelector('.comparison-slider');
    if (!slider) return;

    const afterImageContainer = slider.querySelector('.comparison-after');
    const afterImage = afterImageContainer.querySelector('img');
    const handle = slider.querySelector('.comparison-handle');

    function updateDimensions() {
        const sliderWidth = slider.offsetWidth;
        afterImage.style.width = sliderWidth + 'px';
    }

    // Init dimensions
    updateDimensions();
    window.addEventListener('resize', updateDimensions);

    // Interaction Logic
    let isDragging = false;

    function startDrag(e) {
        isDragging = true;
        updatePosition(e);
        e.preventDefault(); // Prevent text selection
    }

    function stopDrag() {
        isDragging = false;
    }

    function doDrag(e) {
        if (!isDragging) return;
        updatePosition(e);
    }

    function updatePosition(e) {
        const rect = slider.getBoundingClientRect();
        let clientX = e.clientX || (e.touches && e.touches[0].clientX);

        // Calculate position relative to slider
        let x = clientX - rect.left;

        // Boundaries
        if (x < 0) x = 0;
        if (x > rect.width) x = rect.width;

        const percentage = (x / rect.width) * 100;

        afterImageContainer.style.width = percentage + '%';
        handle.style.left = percentage + '%';
    }

    // Mouse Events
    slider.addEventListener('mousedown', startDrag);
    window.addEventListener('mouseup', stopDrag);
    window.addEventListener('mousemove', doDrag);

    // Touch Events
    slider.addEventListener('touchstart', startDrag);
    window.addEventListener('touchend', stopDrag);
    window.addEventListener('touchmove', doDrag);
}

/**
 * FAQ Accordion
 */
function initFAQ() {
    const toggles = document.querySelectorAll('.faq-toggle');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const item = toggle.parentElement;
            const content = item.querySelector('.faq-content');

            // Close other items (Optional: for one-open-at-a-time behavior)
            // document.querySelectorAll('.faq-item').forEach(otherItem => {
            //     if (otherItem !== item && otherItem.classList.contains('active')) {
            //         otherItem.classList.remove('active');
            //         otherItem.querySelector('.faq-content').style.maxHeight = null;
            //     }
            // });

            // Toggle current
            item.classList.toggle('active');

            if (item.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + 'px';
            } else {
                content.style.maxHeight = null;
            }
        });
    });
}
