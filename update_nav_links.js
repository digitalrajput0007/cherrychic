const fs = require('fs');
const path = require('path');

const walk = (dir, done) => {
    let results = [];
    fs.readdir(dir, (err, list) => {
        if (err) return done(err);
        let pending = list.length;
        if (!pending) return done(null, results);
        list.forEach((file) => {
            file = path.resolve(dir, file);
            fs.stat(file, (err, stat) => {
                if (stat && stat.isDirectory()) {
                    walk(file, (err, res) => {
                        results = results.concat(res);
                        if (!--pending) done(null, results);
                    });
                } else {
                    if (file.endsWith('.html')) {
                        results.push(file);
                    }
                    if (!--pending) done(null, results);
                }
            });
        });
    });
};

const desktopOld = '<a href="/legal-generator/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Legal Generator</a>';
const desktopNew = `<a href="/privacy-generator/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Privacy Policy Generator</a>
                        <a href="/terms-generator/" class="px-4 py-2 text-sm text-charcoal hover:bg-cream hover:text-cherry-600">Terms Generator</a>`;

const mobileOld = '<a href="/legal-generator/" class="text-charcoal hover:text-cherry-600">Legal Generator</a>';
const mobileNew = `<a href="/privacy-generator/" class="text-charcoal hover:text-cherry-600">Privacy Policy Generator</a>
            <a href="/terms-generator/" class="text-charcoal hover:text-cherry-600">Terms Generator</a>`;

walk('c:\\CherryChic', (err, results) => {
    if (err) throw err;
    results.forEach((file) => {
        let content = fs.readFileSync(file, 'utf8');
        let changed = false;
        if (content.includes(desktopOld)) {
            content = content.replace(desktopOld, desktopNew);
            changed = true;
        }
        if (content.includes(mobileOld)) {
            content = content.replace(mobileOld, mobileNew);
            changed = true;
        }
        if (changed) {
            fs.writeFileSync(file, content, 'utf8');
            console.log('Updated ' + file);
        }
    });
});
