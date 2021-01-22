var mysql = require('./dbcon.js');

var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');
var path = require('path');

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);



app.get('/reset-table',function(req,res,next){
  var context = {};
  mysql.pool.query("DROP TABLE IF EXISTS workdata", function(err){
  	if(err){
  		next(err);
  		return;
  	}
    var createString = "CREATE TABLE workdata(" +
    "id INT PRIMARY KEY AUTO_INCREMENT," +
    "name VARCHAR(255) NOT NULL," +
    "reps INT," +
    "weight INT," +
    "date DATE," +
    "units INT)";
    mysql.pool.query(createString, function(err){
      context.workoutdata = [];
      res.render('home',context);
    })
  });
});

app.get('/',function(req,res,next){
  var context = {};
  mysql.pool.query('SELECT * FROM workdata', function(err, rows, fields){
    if(err){
      next(err);
      return;
    }
    context.results = JSON.stringify(rows);
    res.render('home', context);
  });
});

app.get('/insert',function(req,res,next){
  var context = {};
  mysql.pool.query("INSERT INTO workdata (`name`, `reps`, `weight`, `date`, `units`) VALUES (?, ?, ?, ?, ?)", [req.query.name, 
  		req.query.reps, req.query.weight, req.query.date, req.query.units], function(err, result){
    if(err){
      next(err);
      return;
    }
    context.workoutdata = [{"id":1,"name":req.query.name,"reps":req.query.reps,"weight":req.query.weight, 
		"date":req.query.date, "units":req.query.units}];
    res.render('home',context);
  });
});

app.get('/delete', function(req,res,next)) {
  var context = {};
  mysql.pool.query("DELETE FROM workdata WHERE id=?", [req.query.id], function(err, result) {
    if(err){
      next(err);
      return;
    }
    //Do I need that context.results here? Just responds back saying row deleted?
    res.render('home',context);
  })
}

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});