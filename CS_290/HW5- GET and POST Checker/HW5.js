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
app.set('port', 45616);

app.get('/',function(req,res){
  var params = [];
  for (var p in req.query) {
    params.push({'name':p, 'value':req.query[p]})
  }
  var context = {};
  context.qlist = params;
  res.render('get', context);
});

app.post('/',function(req,res){
  var bparams = [];
  var qparams = [];

  for (var p in req.body) {
    bparams.push({'name':p, 'value':req.body[p]})
  }

  for (var p in req.query) {
    qparams.push({'name':p, 'value':req.query[p]})
  }

  var context = {};
  context.blist = bparams;
  context.qlist = qparams;

  res.render('post', context);
});

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
