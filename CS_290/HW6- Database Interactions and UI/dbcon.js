var mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit : 10,
  host            : 'localhost',
  user            : 'root',
  password        : 'aaaa',
  database        : 'workbench'
});

module.exports.pool = pool;