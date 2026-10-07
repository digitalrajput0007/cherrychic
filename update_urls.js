const fs = require('fs');
const path = require('path');

const replacements = [
    { regex: /\/tools\/safe-zone-checker\/?/g, replacement: '/safe-zone-checker/' },
    { regex: /\/tools\/color-extractor\/?/g, replacement: '/color-studio/' },
    { regex: /\/tools\/rate-calculator\/?/g, replacement: '/rate-calculator/' },
    { regex: /\/tools\/legal-generator\/?/g, replacement: '/legal-generator/' },
    { regex: /\/tools\/carousel-splitter\/?/g, replacement: '/carousel-splitter/' },
    { regex: /\/tools\/caption-spacer\/?/g, replacement: '/caption-spacer/' },
    { regex: /\/tools\/bio-font-styler\/?/g, replacement: '/bio-font-styler/' },
    { regex: /http:\/\/localhost:3000/g, replacement: 'https://cherrychic.in' },
    { regex: /\.\.\/\.\.\/global\.css/g, replacement: '../global.css' },
    { regex: /href="https:\/\/cherrychic\.in\/tools\/([^"]+)"/g, replacement: (match, p1) => {
        if(p1 === 'color-extractor/') return 'href="https://cherrychic.in/color-studio/"';
        return `href="https://cherrychic.in/${p1}"`;
    }}
];

function processDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            processDir(fullPath);
        } else if (fullPath.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let originalContent = content;
            
            for (const {regex, replacement} of replacements) {
                content = content.replace(regex, replacement);
            }
            
            if (content !== originalContent) {
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Updated URLs in', fullPath);
            }
        }
    }
}

processDir('c:/CherryChic');
