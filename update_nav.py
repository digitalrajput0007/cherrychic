import os

new_nav = """    <!-- Navbar -->
    <nav class="w-full border-b border-warmGray-200 bg-white sticky top-0 z-50" id="navbar">
        <div class="cc-container h-20 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-cherry-600 rounded flex items-center justify-center text-white">
                    <i data-lucide="sparkles" class="w-4 h-4"></i>
                </div>
                <span class="font-serif font-bold text-xl tracking-tight text-charcoal">CherryChic</span>
            </a>
            
            <div class="hidden md:flex items-center gap-8">
                <div class="relative group">
                    <button class="text-sm font-medium text-charcoal hover:text-cherry-600 transition-colors flex items-center gap-1 py-4 outline-none">
                        Video & Social <i data-lucide="chevron-down" class="w-3 h-3"></i>
                    </button>
                    <div class="absolute left-0 top-full mt-0 w-48 bg-white border border-warmGray-200 rounded shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 flex flex-col py-2">
                        <a href="/tools/safe-zone-checker/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Safe Zone Checker</a>
                        <a href="/tools/caption-spacer/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Caption Spacer</a>
                        <a href="/tools/carousel-splitter/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Carousel Splitter</a>
                    </div>
                </div>
                
                <div class="relative group">
                    <button class="text-sm font-medium text-charcoal hover:text-cherry-600 transition-colors flex items-center gap-1 py-4 outline-none">
                        Design & Typography <i data-lucide="chevron-down" class="w-3 h-3"></i>
                    </button>
                    <div class="absolute left-0 top-full mt-0 w-48 bg-white border border-warmGray-200 rounded shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 flex flex-col py-2">
                        <a href="/tools/color-extractor/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Color Extractor</a>
                        <a href="/tools/bio-font-styler/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Bio Font Styler</a>
                    </div>
                </div>

                <div class="relative group">
                    <button class="text-sm font-medium text-charcoal hover:text-cherry-600 transition-colors flex items-center gap-1 py-4 outline-none">
                        Business & Legal <i data-lucide="chevron-down" class="w-3 h-3"></i>
                    </button>
                    <div class="absolute left-0 top-full mt-0 w-48 bg-white border border-warmGray-200 rounded shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 flex flex-col py-2">
                        <a href="/tools/rate-calculator/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Rate Calculator</a>
                        <a href="/tools/legal-generator/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Legal Generator</a>
                    </div>
                </div>
            </div>
            
            <div class="flex items-center gap-4">
                <a href="/contact.html" class="cc-btn-primary hidden sm:inline-flex">Contact Us</a>
                <button id="mobile-menu-btn" class="md:hidden text-charcoal">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>
        </div>
    </nav>"""

new_drawer = """    <!-- Mobile Drawer -->
    <div id="mobile-drawer" class="fixed inset-0 z-50 bg-white/95 backdrop-blur-xl transform translate-x-full transition-transform duration-300 lg:hidden flex flex-col">
        <div class="p-4 flex justify-end">
            <button id="mobile-close-btn" class="p-2 text-charcoal hover:text-cherry-600 bg-cream border border-warmGray-200 rounded">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>
        </div>
        <nav class="flex flex-col items-center gap-6 mt-8 text-lg font-bold overflow-y-auto pb-20">
            <h3 class="text-cherry-600 text-sm uppercase tracking-widest font-bold mt-4">Video & Social</h3>
            <a href="/tools/safe-zone-checker/" class="text-charcoal hover:text-cherry-600">Safe Zone Checker</a>
            <a href="/tools/caption-spacer/" class="text-charcoal hover:text-cherry-600">Caption Spacer</a>
            <a href="/tools/carousel-splitter/" class="text-charcoal hover:text-cherry-600">Carousel Splitter</a>

            <h3 class="text-cherry-600 text-sm uppercase tracking-widest font-bold mt-4">Design & Typography</h3>
            <a href="/tools/color-extractor/" class="text-charcoal hover:text-cherry-600">Color Extractor</a>
            <a href="/tools/bio-font-styler/" class="text-charcoal hover:text-cherry-600">Bio Font Styler</a>
            
            <h3 class="text-cherry-600 text-sm uppercase tracking-widest font-bold mt-4">Business & Legal</h3>
            <a href="/tools/rate-calculator/" class="text-charcoal hover:text-cherry-600">Rate Calculator</a>
            <a href="/tools/legal-generator/" class="text-charcoal hover:text-cherry-600">Legal Generator</a>
            
            <div class="w-16 h-px bg-warmGray-200 my-4"></div>
            <a href="/contact.html" class="text-charcoal hover:text-cherry-600">Contact Us</a>
        </nav>
    </div>"""

import re

for root, dirs, files in os.walk('c:/CherryChic'):
    for file in files:
        if file.endswith('.html') and file not in ['privacy-policy.html']:
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # replace navbar
            # Some old files might have <header class="sticky ...">...</header> instead of <nav>
            # Let's match from <!-- Navbar --> or <!-- Global Header --> to the closing </nav> or </header>
            
            # Remove old navbar
            content = re.sub(r'<!-- Navbar -->\s*<nav.*?</nav>', new_nav, content, flags=re.DOTALL)
            content = re.sub(r'<!-- Global Header -->\s*<header.*?</header>', new_nav, content, flags=re.DOTALL)
            
            # Replace or add Mobile drawer
            if '<!-- Mobile Drawer -->' in content:
                content = re.sub(r'<!-- Mobile Drawer -->\s*<div id="mobile-drawer".*?</nav>\s*</div>', new_drawer, content, flags=re.DOTALL)
            else:
                # Add drawer after navbar if not present
                content = content.replace(new_nav, new_nav + "\n\n" + new_drawer)
                
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated", path)
