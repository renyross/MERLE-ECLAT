
document.addEventListener('DOMContentLoaded', () => {
    initStickyHeader();
    initScrollReveal();
    initCartCounter();
    initHeroSlider();
    initProductCarousel();
    initComparisonSlider();
    initFAQ();
    initMobileMenu();
    initStickyMobileBar();
    initCartDrawer();
    initUniversSlider();
});

/**
 * Sticky Mobile Purchase Bar
 */
function initStickyMobileBar() {
    const stickyBar = document.querySelector('.sticky-mobile-bar');
    const mainAddToCartBtn = document.querySelector('.product-info .btn-primary');

    if (!stickyBar || !mainAddToCartBtn || window.innerWidth > 768) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // If the main add to cart button is NOT visible, show the sticky bar
            if (!entry.isIntersecting) {
                stickyBar.classList.add('active');
                document.querySelector('.floating-cart-btn')?.classList.add('hidden');
            } else {
                stickyBar.classList.remove('active');
                document.querySelector('.floating-cart-btn')?.classList.remove('hidden');
            }
        });
    }, {
        threshold: 0,
        rootMargin: "0px"
    });

    observer.observe(mainAddToCartBtn);
}

/**
 * Univers Carousel (Horizontal Scroll)
 */
function initUniversSlider() {
    const slider = document.getElementById('univers-slider');
    const prevBtn = document.querySelector('.univers-prev');
    const nextBtn = document.querySelector('.univers-next');

    if (!slider || !prevBtn || !nextBtn) return;

    const scrollAmount = 300; // Approx one card width + gap
    let autoScrollTimer;

    const startAutoScroll = () => {
        stopAutoScroll();
        autoScrollTimer = setInterval(() => {
            const isAtEnd = slider.scrollLeft + slider.clientWidth >= slider.scrollWidth - 50;
            if (isAtEnd) {
                slider.scrollTo({
                    left: 0,
                    behavior: 'smooth'
                });
            } else {
                slider.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            }
        }, 4000); // 4 second pause
    };

    const stopAutoScroll = () => {
        if (autoScrollTimer) clearInterval(autoScrollTimer);
    };

    // Initialize auto-scroll
    startAutoScroll();

    // Event Listeners
    prevBtn.addEventListener('click', () => {
        stopAutoScroll();
        const isAtStart = slider.scrollLeft <= 10;
        if (isAtStart) {
            slider.scrollTo({
                left: slider.scrollWidth,
                behavior: 'smooth'
            });
        } else {
            slider.scrollBy({
                left: -scrollAmount,
                behavior: 'smooth'
            });
        }
        startAutoScroll();
    });

    nextBtn.addEventListener('click', () => {
        stopAutoScroll();
        const isAtEnd = slider.scrollLeft + slider.clientWidth >= slider.scrollWidth - 50;
        if (isAtEnd) {
            slider.scrollTo({
                left: 0,
                behavior: 'smooth'
            });
        } else {
            slider.scrollBy({
                left: scrollAmount,
                behavior: 'smooth'
            });
        }
        startAutoScroll();
    });

    // Pause on hover
    slider.addEventListener('mouseenter', stopAutoScroll);
    slider.addEventListener('mouseleave', startAutoScroll);

    // Pause on touch (mobile)
    slider.addEventListener('touchstart', stopAutoScroll, { passive: true });
    slider.addEventListener('touchend', startAutoScroll, { passive: true });
}

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
    const toggleBtn = document.querySelector('.mobile-toggle');
    const closeBtn = document.querySelector('.menu-close-btn');
    const navLinks = document.querySelector('.nav-links');
    const overlay = document.querySelector('.menu-overlay') || (() => {
        const div = document.createElement('div');
        div.className = 'menu-overlay';
        document.body.appendChild(div);
        return div;
    })();

    if (!toggleBtn || !navLinks) return;

    function toggleMenu(forceClose = false) {
        if (forceClose) {
            navLinks.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        } else {
            // If opening menu, close cart drawer
            const willOpen = !navLinks.classList.contains('active');
            if (willOpen) {
                const cartDrawer = document.getElementById('cart-drawer');
                const cartOverlay = document.getElementById('drawer-overlay');
                if (cartDrawer) cartDrawer.classList.remove('active');
                if (cartOverlay) cartOverlay.classList.remove('active');
            }

            const isActive = navLinks.classList.toggle('active');
            overlay.classList.toggle('active');
            document.body.style.overflow = isActive ? 'hidden' : '';
        }
    }

    toggleBtn.addEventListener('click', () => toggleMenu());
    if (closeBtn) closeBtn.addEventListener('click', () => toggleMenu(true));
    overlay.addEventListener('click', () => toggleMenu(true));

    // Handle Submenu Toggles on Mobile
    const menuItemsWithChildren = navLinks.querySelectorAll('.nav-item > a');
    menuItemsWithChildren.forEach(link => {
        const nextElement = link.nextElementSibling;
        if (nextElement && nextElement.classList.contains('mega-menu')) {
            link.addEventListener('click', (e) => {
                if (window.innerWidth <= 1024) {
                    e.preventDefault();
                    const parent = link.parentElement;

                    // Close other submenus (optional, but cleaner)
                    navLinks.querySelectorAll('.nav-item.open').forEach(item => {
                        if (item !== parent) item.classList.remove('open');
                    });

                    parent.classList.toggle('open');
                }
            });
        }
    });

    // Close menu when clicking a regular link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', (e) => {
            const nextElement = link.nextElementSibling;
            const isToggle = nextElement && nextElement.classList.contains('mega-menu') && window.innerWidth <= 1024;

            if (!isToggle) {
                toggleMenu(true);
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
        if (window.scrollY > 20) {
            header.style.top = '0';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.top = '0';
            header.style.boxShadow = 'none';
        }
    });
}

/**
 * Simple Scroll Reveal Animation
 */
function initScrollReveal() {
    const elementsToReveal = document.querySelectorAll('.collection-card, .product-card, .section-title, .circle-item, .quality-image, .quality-content');

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
 * Cart Drawer initialization
 */
function initCartDrawer() {
    // Already handled globally by toggleCartDrawer but can add more logic here if needed
}

function toggleCartDrawer() {
    const drawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('drawer-overlay');
    const navLinks = document.querySelector('.nav-links');
    const menuOverlay = document.querySelector('.menu-overlay');

    if (drawer && overlay) {
        // If opening cart, close mobile menu
        if (!drawer.classList.contains('active')) {
            if (navLinks) navLinks.classList.remove('active');
            if (menuOverlay) menuOverlay.classList.remove('active');
        }

        drawer.classList.toggle('active');
        overlay.classList.toggle('active');
        document.body.style.overflow = drawer.classList.contains('active') ? 'hidden' : '';
    }
}

/**
 * Mock Cart Interaction - Updated for Drawer
 */
function initCartCounter() {
    const addToCartButtons = document.querySelectorAll('.btn-outline, .btn-primary, .btn-cart');
    const cartBadges = document.querySelectorAll('.header-icons .icon-btn span, .floating-cart-count');
    let count = parseInt(localStorage.getItem('merle_cart_count')) || 0;

    // Sync initial count
    cartBadges.forEach(b => b.textContent = count);

    addToCartButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (btn.textContent.includes('Ajouter') || btn.textContent.includes('Panier')) {
                e.preventDefault();
                count++;
                localStorage.setItem('merle_cart_count', count);
                cartBadges.forEach(b => b.textContent = count);

                // Show drawer on add
                setTimeout(() => {
                    toggleCartDrawer();
                }, 500);

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
