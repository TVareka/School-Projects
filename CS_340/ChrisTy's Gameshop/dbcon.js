var mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit : 10,
  host            : 'classmysql.engr.oregonstate.edu',
  user            : 'cs340_varekat',
  password        : '2389',
  database        : 'cs340_varekat'
});

module.exports.pool = pool;