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

walk('c:\\CherryChic', (err, results) => {
    if (err) throw err;
    results.forEach((file) => {
        let content = fs.readFileSync(file, 'utf8');
        
        // Find everything from <!-- Responsive Ad Unit Placeholder --> down to the closing </div></div>
        const regex = /<!-- Responsive Ad Unit Placeholder -->[\s\S]*?Advertisement Placeholder[\s\S]*?<\/div>\s*<\/div>/g;
        
        if (regex.test(content)) {
            content = content.replace(regex, '');
            fs.writeFileSync(file, content, 'utf8');
            console.log('Removed ads from ' + file);
        }
    });
});
