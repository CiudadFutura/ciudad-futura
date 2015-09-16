var gulp = require('gulp'),
    less = require('gulp-less'),
    util = require('gulp-util'),
    colors = util.colors,
    path = require('path'),
    fs = require('fs');


var APPS_PATH = 'src/ciudadfutura/apps'
var APPS = fs.readdirSync(APPS_PATH).filter(function(path) {
    return path.indexOf('__init__') === -1
})

gulp.task('less', function () {
    APPS.forEach(function(app) {
        var current = 'src/ciudadfutura/apps/' + app + '/static/' + app;
        try {
            fs.accessSync(current + '/less');
            util.log(colors.green('[less] Compiling static for app: ' + app));

            gulp.src(current + '/less/**/*.less')
                .pipe(less().on('error', function (event) {
                    util.log(colors.cyan('Error while compiling less...'));
                    util.log(colors.red(event.message));
                }))
                .pipe(gulp.dest(current + '/css'));
        } catch(e) {
            util.log(colors.yellow('[less] Empty static for app: ' + app));
        }
    });
});

gulp.task('dev', ['less'], function () {
    gulp.watch(APPS_PATH + '/**/static/**/*.less', ['less'])
        .on('change', function(event) {
            util.log(colors.yellow('[less] (' + event.type + ') ' + event.path.split(APPS_PATH).pop()));
        });
});

gulp.task('default', ['dev'])
