const esprima = require('esprima');
const fs = require('fs');

// const js_code = `
// this.stage.vars.y = 0;
// if (this.compare(this.stage.vars.y, 50) < 0) {
//   this.stage.vars.y = y + 1;
// } else {
//   this.stage.vars.x = 1;
// }
// `;

// Read file synchronously (blocking)
try {
    const js_code = fs.readFileSync('leopard.js', 'utf8');
    console.log(js_code);
    const ast = esprima.parseScript(js_code, { loc: true });
fs.writeFileSync('ast.json', JSON.stringify(ast, null, 2));
  } catch (err) {
    console.error(err);
  }


// const ast = esprima.parseScript(js_code, { loc: true });
// fs.writeFileSync('ast.json', JSON.stringify(ast, null, 2));